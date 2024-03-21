import os.path
import json
import pathlib

def _json_file_load(file_path: pathlib.Path):
    with open(file_path, "r") as f:
        return json.load(f)
    
def _is_file_exist(file_name):
    return os.path.isfile(file_name)

def get_plugin(file_name: str) -> list:
    file_path = pathlib.Path(file_name)

    try_getting_places_file = True
    while try_getting_places_file:
        if _is_file_exist(file_path):
            try_getting_places_file = False
        else:
            print(f"Error: file {file_name} not found")
            user_input = input("Do you want to specify the path? (y/n)")
            if user_input.lower() == "y":
                file_path = pathlib.Path(str(input(f"Please enter {file_path.name} path:\n")))
            else:
                raise FileNotFoundError(f"Can't find {file_name} in this directlry: {file_path}")
    
    return _json_file_load(file_path)


_DEFAULT_LISTS = {     }
def get_default_list(list_name: list):
    pass