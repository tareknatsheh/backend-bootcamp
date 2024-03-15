"""
Simulates the truck driving in the provided list of roads (terrain)
After going over each road it calculates the remaining fuel and km in the truck
"""
from importlib import import_module

def simulate(truck_module, roads_list, driver):
    for road in roads_list:
        road_module = import_module(f"plugins.roads.{road["road_type"]}").road
        truck_module.drive_km(road["length"])
        print(f"Truck {truck_module.get_name()} has driven {road["length"]} km in road '{road_module.get_name()}' it now has {truck_module.get_current_fuel_amount()} liter")
