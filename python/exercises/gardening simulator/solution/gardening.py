# Goal: find which plant likes which condition

# Initialize some example trees:
trees_array = [
    {
        "name": "oak",
        "does_like_sun": True,
        "water_consumption": 30,
        "does_like_wind": False,
        "does_like_snow": True
    },
    {
        "name": "neem",
        "does_like_sun": False,
        "water_consumption": 36,
        "does_like_wind": True,
        "does_like_snow": False
    },
    {
        "name": "lemon",
        "does_like_sun": True,
        "water_consumption": 85,
        "does_like_wind": True,
        "does_like_snow": True
    }
]

# Get use input
sun_or_cloud = int(input("How's the weather today, is it sunny or cloudy?\n1) Sunny\n2) Cloudy\n"))
rain_intensity = int(input("What is the rain precipitation number in [mm] between 0 - 100\n"))
wind_intensity = int(input("Is it windy?\n1) Yes\n2) No\n"))
is_snowy = int(input("Is it snowy?\n1) Yes\n2) No\n"))

trees_like_sun_conditions = []
trees_like_rain_conditions = []
trees_like_wind_conditions = []
trees_like_snow_conditions = []


# Loop over the trees array, and print if it likes the condition for each tree:
for tree in trees_array:
    if (sun_or_cloud == 1 and tree["does_like_sun"]) or (sun_or_cloud == 2 and not(tree["does_like_sun"])):
        trees_like_sun_conditions.append(tree["name"])
    
    # Assume that trees would tolerate +-10 of water value:
    if (tree["water_consumption"] <= (rain_intensity + 10) and tree["water_consumption"] >= (rain_intensity - 10)):
        trees_like_rain_conditions.append(tree["name"])

    if (wind_intensity == 1 and tree["does_like_wind"]) or (wind_intensity == 2 and not(tree["does_like_wind"])):
        trees_like_wind_conditions.append(tree["name"])

    if (is_snowy == 1 and tree["does_like_snow"]) or (is_snowy == 2 and not(tree["does_like_snow"])):
        trees_like_snow_conditions.append(tree["name"])




print("\n\n")

print(f"trees who like the {'sunny' if sun_or_cloud==1 else 'cloudy'} sky are:\n{', '.join(trees_like_sun_conditions)}")
print(f"trees who like the {rain_intensity}% rain are:\n{', '.join(trees_like_rain_conditions)}")
print(f"trees who like it {'windy' if wind_intensity==1 else 'not windy'}  are:\n{', '.join(trees_like_wind_conditions)}")
print(f"trees who like the {'snowy' if is_snowy==1 else 'no snow'} condition are:\n{', '.join(trees_like_snow_conditions)}")




