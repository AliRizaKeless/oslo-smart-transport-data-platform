import csv
from datetime import datetime


def simulate_passenger_demand():
    input_path = "data/processed/oslo_s_departures.csv"
    output_path = "data/processed/simulated_demand.csv"

    rows = []

    with open(input_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            departure_time = datetime.fromisoformat(row["expected_departure_time"])
            hour = departure_time.hour

            base_demand = 100

            if 7 <= hour <= 9:
                base_demand += 80
            elif 15 <= hour <= 17:
                base_demand += 70

            if row["realtime"] == "True":
                base_demand += 10

            rows.append({
                "line_name": row["line_name"],
                "destination": row["destination"],
                "expected_departure_time": row["expected_departure_time"],
                "simulated_passenger_demand": base_demand
            })

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "line_name",
            "destination",
            "expected_departure_time",
            "simulated_passenger_demand"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved simulated passenger demand to {output_path}")


if __name__ == "__main__":
    simulate_passenger_demand()