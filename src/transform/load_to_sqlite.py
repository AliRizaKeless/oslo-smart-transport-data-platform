import csv
import sqlite3


def load_csv_to_sqlite():
    csv_path = "data/processed/processed_post.csv"
    db_path = "data/processed/posts.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            post_id INTEGER PRIMARY KEY,
            title TEXT,
            body TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT OR REPLACE INTO posts (post_id, title, body)
                VALUES (?, ?, ?)
            """, (row["post_id"], row["title"], row["body"]))

    connection.commit()
    connection.close()

    print("CSV data loaded into SQLite database.")


if __name__ == "__main__":
    load_csv_to_sqlite()