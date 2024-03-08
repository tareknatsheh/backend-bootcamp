import json
import pathlib

def store_data_in_file(file_name: str, data_to_store):
    # First lets create a folder (if it does not exist) to store data in it, call it "data"
    pathlib.Path("./data").mkdir(parents=True, exist_ok=True)
    # dump the data into the file
    with open("./data/" + file_name, "w") as f:
        json.dump(data_to_store, f)