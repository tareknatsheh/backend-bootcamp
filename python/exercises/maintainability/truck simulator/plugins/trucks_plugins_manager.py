import os
from importlib import import_module


_all_files_in_truck_folder = os.listdir(f"./plugins/trucks")
_all_truck_plugins_names = [f.replace(".py","") for f in _all_files_in_truck_folder if f.endswith('.py') and not f.startswith("__")]
_all_truck_modules_list = [import_module(f"plugins.trucks.{truck_module_name}") for truck_module_name in _all_truck_plugins_names]

def get_truck(truck_index):
    if truck_index > len(_all_truck_plugins_names):
        raise IndexError("Wrong truck choice")
    return _all_truck_modules_list[truck_index]

def get_names_all_available_trucks() -> list:
    return [truck_module.get_name() for truck_module in _all_truck_modules_list]


def get_full_tank_km(truck_module):
    return truck_module.get_max_km()