import json

import requests


class IPAPI:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.198 Safari/537.36"
        }
    proxies = {
        # "https": "218.7.171.91:3128"
        # "https": "223.96.90.216:8085"
        "http": "183.148.158.64:9999"
        }

    @classmethod
    def get_my_ip(cls):
        """
        获取本机IP
        :return: str, 本机实际公网IP
        """
        url = "https://httpbin.org/ip"  # 获取ip的url
        resp = requests.get(url)
        return resp.json()["origin"]  # IP

    @classmethod
    def get_location_by_ip(cls, ip):
        """
        根据IP获取地理位置
        :param ip: str, 公网IP
        :return: str, 地理位置
        """
        url = f'https://www.ip138.com/iplookup.asp?ip={ip}&action=2'
        resp = requests.get(url, headers=cls.headers,proxies=cls.proxies)
        resp.encoding = resp.apparent_encoding

        html = resp.text
        # print(html)
        info_dict = json.loads(html.split('var ip_result = ')[1].split(';')[0])['ip_c_list'][0]
        # print(info_dict)
        prov = info_dict['prov']  # 省
        city = info_dict['city']  # 市
        area = info_dict['area']  # 县/区
        # print(prov, city, area)
        if area:
            if len(area) >= 2:
                area = area.replace('县', '').replace('区', "")
            return area
        if city:
            if len(city) >= 2:
                city = city.replace('市', '').replace('区', "")
            return city
        if prov:
            if '特别行政区' in prov:
                prov = prov.replace('特别行政区', '')
            return prov


if __name__ == '__main__':
    my_ip = IPAPI.get_my_ip()
    print('本机IP', my_ip)

    print('ip所在地:', IPAPI.get_location_by_ip(my_ip))  # 本地
    # print(IPAPI.get_location_by_ip("180.149.130.16"))  # 北京
    # print(IPAPI.get_location_by_ip("103.238.227.21"))  # 香港
    # print(IPAPI.get_location_by_ip("119.60.195.191"))  # 宁夏
    # print(IPAPI.get_location_by_ip("114.44.227.87"))  # 台湾
