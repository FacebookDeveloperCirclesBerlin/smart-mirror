from widgets.abstract_widget import AbstractWidget
from tkinter import Frame, Label, S, TOP
from utils.weather import WeatherAPI


class Weather(AbstractWidget):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.temperatureDisplay = False
        self.locationDisplay = False
        self.weatherDisplay = False
        self.client_weather = None
        self.weather_api_response = None

    def get_client_api(self) -> WeatherAPI:
        if self.client_weather is None:
            self.client_weather = WeatherAPI()
        return self.client_weather

    def get_weatherapi_data(self) -> dict:
        if self.weather_api_response is None:
            self.weather_api_response = self.get_client_api().get_data()
        return self.weather_api_response

    def mount_widget(self, configuration):
        """ add text to display """
        # Todo update the data every hours for every lines
        self.temperatureDisplay = Label(
            self,
            fg=configuration['text-color'],
            bg=configuration['background-color'],
            font=(configuration['font'], configuration['xlarge_text_size'])
        )
        self.temperatureDisplay.pack(side=TOP, anchor=S)

        self.weatherDisplay = Label(
            self,
            fg=configuration['text-color'],
            bg=configuration['background-color'],
            font=(configuration['font'], configuration['small_text_size'])
        )
        self.weatherDisplay.pack(side=TOP, anchor=S)

        self.update_display_weather()

        self.locationDisplay = Label(
            self,
            fg=configuration['text-color'],
            bg=configuration['background-color'],
            font=(configuration['font'], configuration['small_text_size'])
        )

        self.locationDisplay.config(text=self.get_weather_location_text())
        self.locationDisplay.pack(side=TOP, anchor=S)

    def get_weather_temperature_text(self):
        """ get current temperature """
        # Todo the unit sign should come from the API response object
        return self.get_weatherapi_data()['temperature'] + "°C"

    def get_weather_location_text(self):
        """ get current location """
        return self.get_weatherapi_data()['city']

    def get_weather_description_text(self):
        """ get current location """
        return self.get_weatherapi_data()['weather']

    def update_display_weather(self):
        """ update weather every 6hours """
        self.weather_api_response = self.get_client_api().get_data(force=True)

        self.temperatureDisplay.config(text=self.get_weather_temperature_text())
        self.weatherDisplay.config(text=self.get_weather_description_text())
        self.weatherDisplay.after(21600000, self.update_display_weather)

