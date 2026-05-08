import sqlite3


def query_combined_insights():
    db_path = "data/processed/transport.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    print("Next departures from Oslo S:")
    cursor.execute("""
        SELECT line_name, destination, expected_departure_time
        FROM departures
        ORDER BY expected_departure_time
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(row)

    print("\nCurrent Oslo weather:")
    cursor.execute("""
        SELECT temperature, precipitation, wind_speed
        FROM weather
        LIMIT 1
    """)
    print(cursor.fetchone())

    print("\nCurrent Oslo traffic:")
    cursor.execute("""
        SELECT traffic_level, congestion_index
        FROM traffic
        LIMIT 1
    """)
    print(cursor.fetchone())

    connection.close()


if __name__ == "__main__":
    query_combined_insights()