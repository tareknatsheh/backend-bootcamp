import os
from importlib import import_module
import pathlib
import json

_all_files_in_roads_folder = os.listdir(f"./plugins/roads")
_all_road_plugins_names = [f.replace(".py","") for f in _all_files_in_roads_folder if f.endswith('.py') and not (f.startswith("__") or f == "Main.py")]

_all_road_modules_list = [import_module(f"plugins.roads.{road_module_name}").road for road_module_name in _all_road_plugins_names]


def get_terrain_file():
    file_path = input("Please provide the path for your terrain file:\n")
    file_path = pathlib.Path(f"{file_path}")
    return _json_file_load(file_path)

def _json_file_load(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    
def get_total_km(terrain_list: list[dict]):
    total = 0
    for road in terrain_list:
        roud_type_module = get_road_type_module(road["road_type"])
        print(roud_type_module.get_hardness_factor())
        total += road["length"] * roud_type_module.get_hardness_factor()
    return total

def get_road_type_module(road_type: str):
    road_type_index = _all_road_plugins_names.index(road_type)
    return _all_road_modules_list[road_type_index] 