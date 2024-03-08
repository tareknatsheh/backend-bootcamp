import requests

def get_asteroid_data() -> dict:
    url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"
    res = requests.get(url)
    return res.json()["near_earth_objects"]