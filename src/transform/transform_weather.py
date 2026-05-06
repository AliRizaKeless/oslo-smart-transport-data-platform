import json
import csv


def transform_weather():
    input_path = "data/raw/oslo_weather.json"
    output_path = "data/processed/oslo_weather.csv"

    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    current = data["current"]

    row = {
        "time": current["time"],
        "temperature": current["temperature_2m"],
        "precipitation": current["precipitation"],
        "wind_speed": current["wind_speed_10m"]
    }

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        writer.writeheader()
        writer.writerow(row)

    print(f"Saved transformed weather data to {output_path}")


if __name__ == "__main__":
    transform_weather()