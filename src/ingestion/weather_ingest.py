import requests
import json


def fetch_oslo_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=59.9139"
        "&longitude=10.7522"
        "&current=temperature_2m,precipitation,wind_speed_10m"
        "&timezone=Europe%2FOslo"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    with open("data/raw/oslo_weather.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Saved Oslo weather data to data/raw/oslo_weather.json")


if __name__ == "__main__":
    fetch_oslo_weather()