import textwrap
from Services.Formats.formats import convert_to_local_sun, format_timezone
from Services.history_searching import save_city_to_history


def render_weather(data):
    #City and country
    city = data['name']
    country = data['sys']['country']
    #lat,lon
    lat, lon = data['coord']['lat'], data['coord']['lon']
    #wind speed
    speed = data['wind']['speed']
    #sunrise,sunset
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    #time
    timezone = data['timezone']
    #convert to local sunrise,sunset
    local_sunrise = convert_to_local_sun(sunrise, lat, lon)
    local_sunset = convert_to_local_sun(sunset, lat, lon)
    #convert to local time
    local_time = format_timezone(timezone)

    #Phần thời tiết và nhiệt độ
    weather_main = data['weather'][0]['main']
    description = data['weather'][0]['description']
    raw_feels_like = data['main']['feels_like']
    raw_temp = data['main']['temp']
    save_city_to_history(city)
    print(textwrap.dedent(f"""
        🌦 Current Weather Forecast
        📍 City        : {city}, {country}
        🕓 Local Time  : {local_time}
        🌤 Weather     : {weather_main} ({description})
        🌡 Temp        : {raw_temp}°C (Feels like: {raw_feels_like}°C)
        🌅 Sunrise     : {local_sunrise}
        🌇 Sunset      : {local_sunset}
        🌬 Wind Speed  : {speed} m/s
        🗺 Coordinates  : ({lat}, {lon})
    """))

