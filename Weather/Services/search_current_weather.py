from Configs.config import API_KEY
from Services.render_data import render_weather
from Services.search import get_city,get_country_code
from Services.weather_service import get_inf
from Models.weather import LocationWeather


def search_current_weather():
     city_input = get_city()
     country_code_input = get_country_code()
     api_key= API_KEY
     location = LocationWeather(city_input, country_code_input, api_key)
     weather = get_inf(location.city_name, location.country_code, location.apikey)
     if weather:
          render_weather(weather)

     else:
          print("........")
