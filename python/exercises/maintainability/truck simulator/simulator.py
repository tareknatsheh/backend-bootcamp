"""
Simulates the truck driving in the provided list of roads (terrain)
After going over each road it calculates the remaining fuel and km in the truck
"""

def simulate(truck_module, roads_list):
    for road in roads_list:
        print(road)
        truck_module.drive_km(road["length"])
        print(f"Truck {truck_module.get_name()} has driven {road["length"]} it now has {truck_module.get_current_fuel_amount()} liter")
