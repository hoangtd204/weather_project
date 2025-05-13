import requests


def get_inf(city_name, country_code, apikey):
    q = f"{city_name},{country_code}" if country_code else city_name
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={apikey}&units=metric"
    response= requests.get(url)
    response_json = response.json()
    return response_json