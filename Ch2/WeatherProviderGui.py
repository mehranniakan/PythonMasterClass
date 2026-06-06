from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from requests import get


class OpenMeteoWeatherProvider():
    base_url = 'https://api.open-meteo.com/v1/forecast'

    def get_weather(self, lat, lng):
        params = {
            'latitude': lat,
            'longitude': lng,
            'current': 'temperature_2m,relative_humidity_2m,precipitation,is_day,wind_speed_10m,wind_direction_10m'
        }
        response = get(self.base_url, params=params, verify=False)

        print(response)

        return response.json()


Window.size = (800, 600)


class WeatherGUIApp(App):
    no_result = None
    result_layout = None
    lon_entry = None
    lat_entry = None

    def build(self):
        main_layout = BoxLayout(orientation="vertical",

                                padding=10, spacing=10)

        self.lat_entry = TextInput(

            hint_text="Enter latitude", padding=10, size_hint_y=None, height=50, multiline=False)

        self.lon_entry = TextInput(

            hint_text="Enter longitude", padding=10, size_hint_y=None, height=50, multiline=False)

        fetch_btn = ToggleButton(

            text="Fetch weather data", size_hint_y=None, height=50)

        fetch_btn.bind(on_press=self.fetch_current_weather)

        self.result_layout = BoxLayout(

            orientation="vertical", padding=10, spacing=10)

        self.no_result = Label(text="no data yet")

        main_layout.add_widget(self.lat_entry)

        main_layout.add_widget(self.lon_entry)

        main_layout.add_widget(fetch_btn)

        main_layout.add_widget(self.result_layout)

        self.result_layout.add_widget(self.no_result)

        return main_layout

    def show_info(self, temp=27, humidity=50):
        self.result_layout.clear_widgets()

        temp_label = Label(

            text=f"Temperature: {temp}", size_hint_y=None, height=30)

        humidity_label = Label(

            text=f"Humidity: {humidity}%", size_hint_y=None, height=30)

        self.result_layout.add_widget(temp_label)

        self.result_layout.add_widget(humidity_label)

    def fetch_current_weather(self, instance):

        provider = OpenMeteoWeatherProvider()

        self.result_layout.clear_widgets()

        loading_label = Label(text="fetching data ...")

        self.result_layout.add_widget(loading_label)

        result = provider.get_weather(

            float(self.lat_entry.text), float(self.lon_entry.text))

        print(result)

        self.show_info(result['current'].get("temperature_2m"), result['current'].get("relative_humidity_2m"))


WeatherGUIApp().run()