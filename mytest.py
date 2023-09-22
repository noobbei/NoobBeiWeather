from API.IPAPI import IPAPI
from API.weatherAPI import WeatherAPI

# 获取本地天气
print(WeatherAPI.get_weather_by_city_name(IPAPI.get_location_by_ip(IPAPI.get_my_ip())))
