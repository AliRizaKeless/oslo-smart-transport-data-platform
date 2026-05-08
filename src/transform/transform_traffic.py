import json
import csv


def transform_traffic():
    input_path = "data/raw/oslo_traffic.json"
    output_path = "data/processed/oslo_traffic.csv"

    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    row = {
        "city": data["city"],
        "traffic_level": data["traffic_level"],
        "congestion_index": data["congestion_index"],
        "timestamp": data["timestamp"]
    }

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        writer.writeheader()
        writer.writerow(row)

    print(f"Saved transformed traffic data to {output_path}")


if __name__ == "__main__":
    transform_traffic()