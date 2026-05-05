import sqlite3


def query_departures():
    db_path = "data/processed/transport.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT line_name, destination, expected_departure_time
        FROM departures
        ORDER BY expected_departure_time
        LIMIT 10
    """)

    rows = cursor.fetchall()

    print("Next departures from Oslo S:")
    for row in rows:
        print(row)

    connection.close()


if __name__ == "__main__":
    query_departures()