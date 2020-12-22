from tkinter import Frame
from unittest.mock import MagicMock

from utils.weather import WeatherAPI
from widgets.weather import Weather


def test_weather_widget(mocker):
    mock_api = mocker.patch.object(
        WeatherAPI,
        'get_data'
    )
    mock_api.get_data = MagicMock(return_value={"city": "Berlin, DE", "weather": "cloudy", "temperature": "21"})

    mock_frame = mocker.patch.object(Frame, "__init__")
    widget = Weather(mock_frame)
    widget.client_weather = mock_api

    txt = widget.get_weather_description_text()
    assert txt == 'cloudy'
