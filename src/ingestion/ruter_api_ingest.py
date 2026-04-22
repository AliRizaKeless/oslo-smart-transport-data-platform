import requests
import json


def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open("data/raw/sample_response.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Data saved to data/raw/sample_response.json")
    else:
        print("Failed to fetch data")


if __name__ == "__main__":
    fetch_data()