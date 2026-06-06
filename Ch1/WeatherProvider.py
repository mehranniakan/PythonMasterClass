from abc import ABC, abstractmethod
from requests import get
class WeatherProvider(ABC):

    @abstractmethod
    def get_weather(self,lat,lng):
        pass


class OpenMeteoWeatherProvider(WeatherProvider):
    base_url = 'https://api.open-meteo.com/v1/forecast'

    def get_weather(self,lat,lng):
        params = {
            'latitude': lat,
            'longitude': lng,
            'current': 'temperature_2m,relative_humidity_2m,precipitation,is_day,wind_speed_10m,wind_direction_10m'
        }
        response = get(self.base_url, params=params, verify=False)

        return response.json()


class OpenWeatherProvider(WeatherProvider):
    base_url = 'https://api.openweathermap.org/data/4.0/onecall/current'

    def get_weather(self,lat,lng):
        params = {
            'lat': lat,
            'lon': lng,
            'units' : 'standard',
            'appid': '3dd602f347eb28e75bed50d50a5bd634'
        }
        response = get(self.base_url, params=params, verify=False)

        return response.json()


# provider = OpenMeteoWeatherProvider()
#
# print(provider.get_weather(lat=31.319, lng=48.6842))
