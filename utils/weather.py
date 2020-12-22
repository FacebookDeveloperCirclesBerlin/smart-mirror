import os
import requests


class WeatherAPI:
    def __init__(self):
        self.API_response = {}
        self.app_id = os.getenv('API_APP_ID')
        self.update()

    def update(self):
        """ update  the data from weather API """
        # Todo make it from a preference setting
        city = os.getenv('API_CITY')
        units = os.getenv('API_METRICS_UNIT')

        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city \
              + "&APPID=" + self.app_id \
              + "&units=" + units
        r = requests.get(url)
        self.API_response = r.json()

    def get_data(self, force=False):
        if force:
            self.update()
        return {
            'temperature': str(int(self.API_response['main']['temp'])),
            'city': os.getenv('WEATHER_DISPLAY_CITY'),
            'weather': self.API_response['weather'][0]['description']
        }
