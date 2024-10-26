import sys
import requests
import json

# NASA NEO API base URLs and API key (replace with your actual API key)
API_FEED_URL = "https://api.nasa.gov/neo/rest/v1/feed"
API_LOOKUP_URL = "https://api.nasa.gov/neo/rest/v1/neo/"
API_KEY = "D4niTDBr21h4wX8zlRTl8Zbh3i2NsQFzMOjj8tl2"

def fetch_meteor_by_name(name, start_date, end_date):
    """
    Fetches meteor data from NASA's NEO API by searching NEOs within a date range for a specific name.
    """
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": API_KEY
    }

    try:
        # Request a list of NEOs for the date range
        response = requests.get(API_FEED_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Search through NEOs by name
        for date in data['near_earth_objects']:
            for meteor in data['near_earth_objects'][date]:
                if meteor['name'].lower() == name.lower():
                    # Fetch detailed information using the NEO reference ID if a match is found
                    return fetch_meteor_by_id(meteor['id'])
        
        return json.dumps({"error": "Meteor or asteroid with that name not found in the recent date range."})

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)})

def fetch_meteor_by_id(neo_id):
    """
    Fetches detailed meteor data using NASA's NEO reference ID.
    """
    try:
        response = requests.get(f"{API_LOOKUP_URL}{neo_id}", params={"api_key": API_KEY})
        response.raise_for_status()
        data = response.json()
        
        # Extract relevant details
        meteor_details = {
            "name": data['name'],
            "diameter_km": data['estimated_diameter']['kilometers']['estimated_diameter_max'],
            "is_potentially_hazardous": data['is_potentially_hazardous_asteroid'],
            "close_approach_data": [
                {
                    "date": approach['close_approach_date'],
                    "velocity_kmh": approach['relative_velocity']['kilometers_per_hour'],
                    "miss_distance_km": approach['miss_distance']['kilometers']
                }
                for approach in data['close_approach_data']
            ]
        }

        return json.dumps(meteor_details, indent=4)

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)})

def fetch_meteors_by_date(start_date, end_date):
    """
    Fetches meteor data from NASA's NEO API based on a date range.
    """
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": API_KEY
    }

    try:
        # Request a list of NEOs for the specified date range
        response = requests.get(API_FEED_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        meteors = []
        for date in data['near_earth_objects']:
            for meteor in data['near_earth_objects'][date]:
                meteors.append({
                    "name": meteor['name'],
                    "close_approach_date": date,
                    "diameter_km": meteor['estimated_diameter']['kilometers']['estimated_diameter_max'],
                    "velocity_kmh": meteor['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'],
                    "miss_distance_km": meteor['close_approach_data'][0]['miss_distance']['kilometers']
                })
        
        return json.dumps(meteors, indent=4)

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)})

# Main execution flow
if __name__ == "__main__":
    # The first argument specifies the search type (name, date, or id)
    if len(sys.argv) < 2:
        print("Please provide a search type (name, date, or id).")
        sys.exit(1)

    search_type = sys.argv[1]

    # Process search by name
    if search_type == "name" and len(sys.argv) == 5:
        name = sys.argv[2]
        start_date = sys.argv[3]
        end_date = sys.argv[4]
        print(fetch_meteor_by_name(name, start_date, end_date))

    # Process search by date range
    elif search_type == "date" and len(sys.argv) == 4:
        start_date = sys.argv[2]
        end_date = sys.argv[3]
        print(fetch_meteors_by_date(start_date, end_date))

    # Process search by NEO ID
    elif search_type == "id" and len(sys.argv) == 3:
        neo_id = sys.argv[2]
        print(fetch_meteor_by_id(neo_id))

    else:
        print("Invalid input. Please check the arguments provided.")
