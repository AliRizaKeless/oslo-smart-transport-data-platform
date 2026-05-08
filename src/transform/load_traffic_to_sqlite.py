import csv
import sqlite3


def load_traffic_to_sqlite():
    csv_path = "data/processed/oslo_traffic.csv"
    db_path = "data/processed/transport.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS traffic (
            city TEXT,
            traffic_level TEXT,
            congestion_index INTEGER,
            timestamp TEXT PRIMARY KEY
        )
    """)

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT OR REPLACE INTO traffic (
                    city,
                    traffic_level,
                    congestion_index,
                    timestamp
                )
                VALUES (?, ?, ?, ?)
            """, (
                row["city"],
                row["traffic_level"],
                row["congestion_index"],
                row["timestamp"]
            ))

    connection.commit()
    connection.close()

    print("Loaded Oslo traffic data into SQLite database.")


if __name__ == "__main__":
    load_traffic_to_sqlite()