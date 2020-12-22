import requests
import json

api_key = "2c065577f96a20c5300d6dd9944c16b5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

complete_url = f"{base_url}appid={api_key}&q={city_name}"

response = requests.get(complete_url)

x = response.json()


def miles_to_km(Value):
    return int(Value) * 1.609


def kelvin_to_celsius(Value):
    return int(Value) - 273.15


if x["cod"] != "404":

    main = x["main"]
    wind = x["wind"]
    weather = x["weather"]

    weather_condition = weather[0]["main"]

    temp = round(kelvin_to_celsius(main["temp"]), 1)
    wind_speed = round(miles_to_km(wind["speed"]), 1)

    print(f"\n\nThe weather in {city_name}\n")
    print(f"  Weather condition:   {weather_condition}")
    print(f"  Temperature:         {temp} °C")
    print(f"  Wind speed:          {wind_speed} km/h\n")

else:
    print("City Not Found")
