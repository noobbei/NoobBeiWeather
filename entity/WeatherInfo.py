class WeatherInfo:

    def __init__(self, name: str, week: str, weather: str, temperature: str, temperature_range: str, weather_img:
    bytes, humidity: str,
                 wind_direction: bytes, ultraviolet_rays: str, air_quality: str, pm: str, sunrise_time: str,
                 sunset_time: str):
        self.name = name
        self.week = week
        self.weather = weather
        self.temperature = temperature
        self.temperature_range = temperature_range
        self.weather_img = weather_img
        self.humidity = humidity
        self.wind_direction = wind_direction
        self.ultraviolet_rays = ultraviolet_rays
        self.air_quality = air_quality
        self.pm = pm
        self.sunrise_time = sunrise_time
        self.sunset_time = sunset_time

    def __str__(self):
        info = f"""
        name = {self.name}
        week = {self.week}
        weather = {self.weather}
        temperature = {self.temperature}
        temperature_range = {self.temperature_range}
        ultraviolet_ras = {self.ultraviolet_rays}
        air_quality = {self.air_quality}
        pm = {self.pm}
        sunrise_time = {self.sunrise_time}
        sunset_time = {self.sunset_time}
              """
        return info
