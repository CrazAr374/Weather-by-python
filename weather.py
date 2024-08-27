import requests
import json
import os
from tabulate import tabulate

city = input("Enter the city: ")
url = f"YOUR PERSONAL API KEY={city}"

r = requests.get(url)
data = r.json()

weather_info = {
    "City": city,
    "Temperature (°C)": data["current"]["temp_c"],
    "Condition": data["current"]["condition"]["text"],
    "Humidity (%)": data["current"]["humidity"],
    "Wind Speed (km/h)": data["current"]["wind_kph"],
    "Feels Like (°C)": data["current"]["feelslike_c"],
    "Last Updated": data["current"]["last_updated"]
}

weather_table = [[key, value] for key, value in weather_info.items()]

print(tabulate(weather_table, headers=["Attribute", "Value"], tablefmt="grid"))
