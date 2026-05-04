import sqlite3


def query_data():
    db_path = "data/processed/posts.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM posts")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


if __name__ == "__main__":
    query_data()