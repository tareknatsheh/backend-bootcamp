def clean_asteroid_data(asteroid_data_by_day: dict) -> list:
    """Takes a dict with all original kvps from the source API
    returns a clean list of dicts for each asteroid"""
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

def get_x_y_lists(clean_asteroid_list: list) -> tuple[list, list, list, list]:
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    # Will generate all x and y axes at once to avoid calling a for loop
    # too often
    for asteroid in clean_asteroid_list:
        x1.append(asteroid["estimated_diameter_min"])
        y1.append(asteroid["relative_velocity"])
        x2.append(asteroid["miss_distance"])
        y2.append(asteroid["estimated_diameter_max"])
    return x1, y1, x2, y2

