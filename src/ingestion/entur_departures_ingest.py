import requests
import json


ENTUR_ENDPOINT = "https://api.entur.io/journey-planner/v3/graphql"


def fetch_oslo_s_departures():
    query = """
    {
      stopPlace(id: "NSR:StopPlace:59872") {
        id
        name
        estimatedCalls(numberOfDepartures: 5) {
          realtime
          aimedDepartureTime
          expectedDepartureTime
          destinationDisplay {
            frontText
          }
          serviceJourney {
            journeyPattern {
              line {
                id
                name
                transportMode
              }
            }
          }
        }
      }
    }
    """

    headers = {
        "Content-Type": "application/json",
        "ET-Client-Name": "github-oslo-smart-transport-data-platform"
    }

    response = requests.post(
        ENTUR_ENDPOINT,
        headers=headers,
        json={"query": query},
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    with open("data/raw/oslo_s_departures.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Saved real Oslo S departures to data/raw/oslo_s_departures.json")


if __name__ == "__main__":
    fetch_oslo_s_departures()