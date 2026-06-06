from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from requests import get


def get_weather_meteo(lat, lng):
    base_url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': lat,
        'longitude': lng,
        'current': 'temperature_2m,relative_humidity_2m,precipitation,is_day,wind_speed_10m,wind_direction_10m'
    }
    response = get(base_url, params=params, verify=False)

    return response.json()


def get_open_weather(lat, lng):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': lng,
        'units': 'metric',
        'appid': '3dd602f347eb28e75bed50d50a5bd634'
    }
    response = get(base_url, params=params, verify=False)

    return response.json()


app = FastAPI()


@app.get("/")
def weather(lat: float, lng: float, provider: str):
    if lat and lng and provider:

        if provider == 'OpenMeteo':

            weather_data = get_weather_meteo(lat, lng)

            last_update = str(weather_data['current']['time']).split('T')

            return JSONResponse(content={
                'temperature': f"{weather_data['current']['temperature_2m']} {weather_data['current_units']['temperature_2m']}",
                'humidity': f"{weather_data['current']['relative_humidity_2m']} {weather_data['current_units']['relative_humidity_2m']}",
                'wind_speed': f"{weather_data['current']['wind_speed_10m']} {weather_data['current_units']['wind_speed_10m']}",
                'wind_direction': f"{weather_data['current']['wind_direction_10m']} {weather_data['current_units']['wind_direction_10m']}",
                'precipitation': f"{weather_data['current']['precipitation']} {weather_data['current_units']['precipitation']}",
                'update date': last_update[0],
                'update time': last_update[1],
            },
                status_code=status.HTTP_200_OK)

        elif provider == 'OpenWeather':

            weather_data = get_open_weather(lat, lng)

            return JSONResponse(content={
                'location':f"{weather_data['sys']['country']} - {weather_data['name']}",
                'sky_situation': weather_data['weather'][0]['description'],
                'temperature': f"{weather_data['main']['temp']} C",
                'feels_like': f"{weather_data['main']['feels_like']} C",
                'humidity': f"{weather_data['main']['humidity']} %",
                'wind_speed': f"{weather_data['wind']['speed']} km/h",
                'wind_direction': f"{weather_data['wind']['deg']} deg",
            },
                status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={'Msg': 'Please enter OpenWeather or OpenMeteo as provider'},
                                status_code=status.HTTP_400_BAD_REQUEST)
