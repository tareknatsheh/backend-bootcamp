"""
Database

Responsible for:
a) saving the data in data.json
b) handling the following requests from outside:
    - Read
    - Write

Data in the database file data.json is like this:
{
    "total_num_of_rabbits": 23,
    "logs": [
        {record 1},
        {record 2},
        ... etc
    ]
}

When there is a write request: it handles the data validation and returns a status message when it's done

It provides the following endpoints as a form of functions:
get_total_num_rabbits() -> int
post_record({record}) -> dict

When post_record is called, don't update the databse but rather:
put them in a "cache" list. Then, when total items in the cache is >= 10:
    loop over them and update the "total_num_of_rabbits" at the end and store them in "logs"

"""
import json
import DB.utils.json_wrapper as wrapper

_DB_DIR = "./DB/data.json"
# _data_cache = dict()


@wrapper.db_decorator
def _read_data_to_file(file_path):
    # global _data_cache
    with open(file_path) as f:
        data = f.read()
        # _data_cache = data
        return data

@wrapper.db_decorator
def _write_data_to_file(file_path, record):
    with open(file_path, "r+") as f:
        f.seek(0)
        content = f.read()
        content = json.loads(content)
        content["logs"].append(record)
        f.seek(0)        
        json.dump(content,f, indent=4, sort_keys=True)
        f.truncate()


def get_data() -> str:
    return _read_data_to_file(_DB_DIR)

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
