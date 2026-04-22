import requests
import json


def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print("Failed to fetch data")


if __name__ == "__main__":
    fetch_data()