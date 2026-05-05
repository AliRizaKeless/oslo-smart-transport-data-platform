import json
import csv


def transform_entur_departures():
    input_path = "data/raw/oslo_s_departures.json"
    output_path = "data/processed/oslo_s_departures.csv"

    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    stop_place = data["data"]["stopPlace"]
    rows = []

    for call in stop_place["estimatedCalls"]:
        line = call["serviceJourney"]["journeyPattern"]["line"]

        rows.append({
            "stop_id": stop_place["id"],
            "stop_name": stop_place["name"],
            "line_id": line["id"],
            "line_name": line["name"],
            "transport_mode": line["transportMode"],
            "destination": call["destinationDisplay"]["frontText"],
            "aimed_departure_time": call["aimedDepartureTime"],
            "expected_departure_time": call["expectedDepartureTime"],
            "realtime": call["realtime"]
        })

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved transformed Entur departures to {output_path}")


if __name__ == "__main__":
    transform_entur_departures()