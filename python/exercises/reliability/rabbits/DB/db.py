"""
Database

Responsible for:
a) saving the data in data.json
b) handling the following requests from outside:
    - Read
    - Write

Data in the database file data.json is like this:
{
    "new_records": [{record 7}, {record 8}],
    "logs": [
        {record 1},
        {record 2},
        ... etc
    ]
}

When there is a write request: it handles the data validation and returns a status message when it's done

It provides the following endpoints as a form of functions:
get_logs() -> list[dict]
get_new_records() -> list[dict]  : it automatically deletes records when they are read
post_record({record}) -> dict   : posts it into both "logs" and "new_records"


"""
import json
import DB.utils.json_wrapper as wrapper

_DB_DIR = "./DB/data.json"

@wrapper.db_decorator
def _read_data_from_file(file_path):
    # global _data_cache
    with open(file_path) as f:
        data = f.read()
        # _data_cache = data
        return json.loads(data)

@wrapper.db_decorator
def _write_data_to_file(file_path: str, record: dict) -> None:
    with open(file_path, "r+") as f:
        f.seek(0)
        content = f.read()
        content = json.loads(content)
        content["logs"].append(record)
        content["new_records"].append(record)
        f.seek(0)        
        json.dump(content,f, indent=4, sort_keys=True)
        f.truncate()


def _get_data():
    return _read_data_from_file(_DB_DIR)

def get_logs():
    return _get_data()["logs"]

def get_new_records():
    return _get_data()["new_records"]

def post_data(record: dict) -> str:
    response = {
        "status": "ok",
        "body": str(record)
        }
    try: 
        _write_data_to_file(_DB_DIR, record)
    except Exception as error:
        response = {
            "status": "error",
            "message": str(error)
        }

    return str(response)

@wrapper.db_decorator
def reset_new_records_list() -> None:
    with open(_DB_DIR, "w") as f:
        f.seek(0)
        content = f.read()
        content = json.loads(content)
        content["new_records"].clear()
        print("new cleared list:", content["new_records"])
        f.seek(0)        
        json.dump(content,f, indent=4, sort_keys=True)
        f.truncate()

def reset_all() -> None:
    print("Resetting all data")
    with open(_DB_DIR, "r+") as f:
        f.seek(0)
        content = f.read()
        content = json.loads(content)
        content["logs"].clear()
        content["new_records"].clear()
        f.seek(0)        
        json.dump(content,f, indent=4, sort_keys=True)
        f.truncate()