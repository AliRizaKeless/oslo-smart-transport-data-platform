import json


def transform_data():
    input_path = "data/raw/sample_response.json"
    output_path = "data/processed/processed_post.json"

    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    transformed_data = {
        "post_id": data["id"],
        "title": data["title"],
        "body": data["body"]
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(transformed_data, file, indent=4)

    print(f"Transformed data saved to {output_path}")


if __name__ == "__main__":
    transform_data()