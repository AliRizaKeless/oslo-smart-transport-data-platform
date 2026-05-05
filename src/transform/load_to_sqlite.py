import csv
import sqlite3


def load_entur_to_sqlite():
    csv_path = "data/processed/oslo_s_departures.csv"
    db_path = "data/processed/transport.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departures (
            stop_id TEXT,
            stop_name TEXT,
            line_id TEXT,
            line_name TEXT,
            transport_mode TEXT,
            destination TEXT,
            aimed_departure_time TEXT,
            expected_departure_time TEXT,
            realtime BOOLEAN
        )
    """)

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO departures (
                    stop_id,
                    stop_name,
                    line_id,
                    line_name,
                    transport_mode,
                    destination,
                    aimed_departure_time,
                    expected_departure_time,
                    realtime
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row["stop_id"],
                row["stop_name"],
                row["line_id"],
                row["line_name"],
                row["transport_mode"],
                row["destination"],
                row["aimed_departure_time"],
                row["expected_departure_time"],
                row["realtime"]
            ))

    connection.commit()
    connection.close()

    print("Loaded Entur departures into SQLite database.")


if __name__ == "__main__":
    load_entur_to_sqlite()