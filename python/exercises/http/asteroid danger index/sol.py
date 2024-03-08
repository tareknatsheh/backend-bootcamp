import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

# Get asteroid data from Nasa API
res = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY")

res_obj = res.json()["near_earth_objects"]
# ["2015-09-08"][0]["name"]
# print(res_obj)


# Save it in a json file
with open("data.json", "w") as f:
    json.dump(res_obj, f)

# Process the data (keep only: id, name, est diameter (min and max), miss distance (km), relative velocity (KM/H))
clean_asteroid_list = []
for day in res_obj:
    asteroids_list = res_obj[day]
    for asteroid in asteroids_list:
        # id name ["estimated_diameter"]["kilometers"]["estimated_diameter_min"]/["estimated_diameter_max"]
        clean_asteroid_list.append({
            "id": asteroid["id"],
            "name": asteroid["name"],
            "estimated_diameter_min": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
            "estimated_diameter_max": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
            "miss_distance": asteroid["close_approach_data"][0]["miss_distance"]["kilometers"],
            "relative_velocity": asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]
        })
    
with open("clean_data.json", "w") as f:
    json.dump(clean_asteroid_list, f)

# Create graphs for each asteroid (min diameter vs velocity AND miss distance vs max diameter)
# Calculate the danger index of each asteroid
# Plot DYNAMICALLY asteroid name vs danger index
