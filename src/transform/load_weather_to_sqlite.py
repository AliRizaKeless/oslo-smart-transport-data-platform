import csv
import sqlite3


def load_weather_to_sqlite():
    csv_path = "data/processed/oslo_weather.csv"
    db_path = "data/processed/transport.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            time TEXT PRIMARY KEY,
            temperature REAL,
            precipitation REAL,
            wind_speed REAL
        )
    """)

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT OR REPLACE INTO weather (
                    time,
                    temperature,
                    precipitation,
                    wind_speed
                )
                VALUES (?, ?, ?, ?)
            """, (
                row["time"],
                row["temperature"],
                row["precipitation"],
                row["wind_speed"]
            ))

    connection.commit()
    connection.close()

    print("Loaded Oslo weather data into SQLite database.")


if __name__ == "__main__":
    load_weather_to_sqlite()