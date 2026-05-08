import json


def fetch_oslo_traffic():
    traffic_data = {
        "city": "Oslo",
        "traffic_level": "Moderate",
        "congestion_index": 42,
        "timestamp": "2026-05-04T12:00:00"
    }

    with open("data/raw/oslo_traffic.json", "w", encoding="utf-8") as file:
        json.dump(traffic_data, file, indent=4)

    print("Saved Oslo traffic data to data/raw/oslo_traffic.json")


if __name__ == "__main__":
    fetch_oslo_traffic()