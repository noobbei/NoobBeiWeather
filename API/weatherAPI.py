import json
import os.path

import requests
from bs4 import BeautifulSoup

from entity.WeatherInfo import WeatherInfo
from util import get_base_dir


class WeatherAPI:
    """
    天气API
    """
    homepage_url = 'https://www.tianqi.com'  # 主页
    china_city_url = 'https://www.tianqi.com/chinacity.html'  # 全国城市地址
    city_url_dict = {}  # 城市url字典

    class DataError:
        """
        错误信息
        """
        NO_DATA_ERROR = '查无此城市/区县'
        DATA_REQUEST_ERROR = '请求出错'
        DATA_ANALYSIS_ERROR = '数据解析错误'

    # ua伪装
    headers = {
        "referer": "https://www.tianqi.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54 "
        }

    @classmethod
    def get_weather_by_city_name(cls, name: str) -> WeatherInfo | str:
        url = cls.city_url_dict.get(name)  # 从字典中获取城市对应的url
        if not url:  # 如果为空, 返回数据错误
            return cls.DataError.NO_DATA_ERROR
        try:
            resp = requests.get(url, headers=cls.headers)
            resp.encoding = resp.apparent_encoding
        except Exception as e:
            return cls.DataError.DATA_REQUEST_ERROR + ', 出错信息为:' + str(e)

        if not resp.status_code == 200:
            return cls.DataError.DATA_REQUEST_ERROR + '请求状态码为:' + str(resp.status_code)

        try:
            bs = BeautifulSoup(resp.text, 'html.parser')  # beautifulSoup解析
            name = bs.find('dd', attrs={'class': 'name'}).find('h1').text  # 标题
            week = bs.find('dd', attrs={'class': 'week'}).text  # 日期
            weather_tag = bs.find('dd', attrs={'class': 'weather'})
            weather = weather_tag.find('span').find('b').text  # 天气
            p = weather_tag.find('p')
            temperature = p.find('b').text  # + p.find('i').text  # 当前温度
            temperature_range = str(weather_tag.find('span')).split('</b>')[1].strip('</span>')  # 温度范围
            weather_img_url = 'https:' + weather_tag.find('img')['src']  # 天气图片地址
            weather_img = requests.get(weather_img_url, headers=cls.headers).content  # 天气图片
            shidu = bs.find('dd', attrs={'class': 'shidu'}).findAll('b')
            humidity = shidu[0].text  # 湿度
            wind_direction = shidu[1].text  # 风向
            ultraviolet_rays = shidu[2].text  # 紫外线
            kongqi = bs.find('dd', attrs={'class': 'kongqi'})
            air_quality = kongqi.find('h5').text  # 空气质量
            pm = kongqi.find('h6').text  # pm
            span = str(kongqi.find('span')).split('<br/>')
            sunrise_time = span[0].strip('<span>日出: ')  # 日出时间
            sunset_time = span[1].strip('日落: ').strip('</span>')  # 日落时间
            return WeatherInfo(name, week, weather, temperature, temperature_range, weather_img, humidity,
                               wind_direction, ultraviolet_rays, air_quality, pm, sunrise_time, sunset_time)
        except Exception as e:
            return cls.DataError.DATA_ANALYSIS_ERROR + ', 错误信息为: ' + str(e)

    @classmethod
    def init_city(cls):
        path = os.path.join(get_base_dir(), 'data')
        if not os.path.exists(path):
            os.makedirs(path)
        file = os.path.join(path, 'cities.json')

        if not os.path.exists(file):  # 文件不存在, 就查询, 创建文件
            path = os.path.join(get_base_dir(), 'data/chinacity.html')
            with open(path, 'r', encoding='utf-8') as f:
                china_city_html = f.read()

            bs = BeautifulSoup(china_city_html, 'html.parser')
            a_list = bs.find('div', attrs={'class': 'citybox'}).findAll('a')

            for a in a_list:
                city_name = a.text
                city_url = WeatherAPI.homepage_url + a['href']
                cls.city_url_dict[city_name] = city_url  # 城市名:城市url
            with open(file, 'w', encoding='utf-8') as f:
                f.write(json.dumps(cls.city_url_dict))
        else:
            with open(file, 'r', encoding='utf-8') as f:
                cls.city_url_dict = json.load(f)

        # print(cls.city_url_dict)


WeatherAPI.init_city()

if __name__ == '__main__':
    city_name = '城区'
    print(WeatherAPI.get_weather_by_city_name(city_name))
