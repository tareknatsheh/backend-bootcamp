

def clean_asteroid_data(asteroid_data_by_day: dict) -> list:
    clean_asteroid_list = []
    for day in asteroid_data_by_day:
        asteroids_list = asteroid_data_by_day[day]
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
    return clean_asteroid_list