"""
Sensor iot
Generates data and writes it to the db in random time intervals

Inputs:
    None
Outputs:
    a list of records, example:
    [
        {record 1},
        {record 2}
    ]
    each record looks like this example:
    {
        "Timestamp": "2024-03-09T00:00:00Z",
        "newborn_count": 10,
        "died_count": 3
    }

Algorithm:
Run a while loop that will exit after generating say 200 records
after generating a record immediatly call the DB API to insert the record

"""

import time
from datetime import datetime
from random import randint

import sys
import os
# Remove these two lines after finishing the development of thid module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from DB import db
from fail_handler.db_handle import handle_failure

def generate_record() -> dict:
    timestamp = datetime.now()
    
    return {
        "Timestamp": str(timestamp),
        "newborn_count": randint(0, 20),
        "death_count": randint(0, 10)
    }

def sensor() -> None:
    records_counter = 0
    while records_counter < 200:
        # Generate
        new_record = generate_record()
        # Send to database
        post_response = handle_failure(db.post_data, 5,new_record)
        print(post_response)

        records_counter += 1
        time.sleep(randint(5, 10))


if __name__ == "__main__":
    sensor()