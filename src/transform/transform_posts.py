import json
import csv


def transform_data():
    input_path = "data/raw/sample_response.json"
    output_json_path = "data/processed/processed_post.json"
    output_csv_path = "data/processed/processed_post.csv"

    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    transformed_data = {
        "post_id": data["id"],
        "title": data["title"],
        "body": data["body"]
    }

    with open(output_json_path, "w", encoding="utf-8") as file:
        json.dump(transformed_data, file, indent=4)

    with open(output_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=transformed_data.keys())
        writer.writeheader()
        writer.writerow(transformed_data)

    print(f"Transformed data saved to {output_json_path}")
    print(f"CSV data saved to {output_csv_path}")


if __name__ == "__main__":
    transform_data()