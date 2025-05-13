import requests

class LocationWeather :
    def __init__(self, city, countrycode, apikey):
        self.city_name  = city
        self.country_code = countrycode
        self.apikey = apikey

