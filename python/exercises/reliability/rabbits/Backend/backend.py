"""

Keeps checking the db fore new records, when we have >= 10 new records, we recalculate the total num of alive rabbits
Then, ask the db to clear the new records holder.

-- Note that imported handle_failure function --

"""
import time
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DB import db
from fail_handler.db_handle import handle_failure

BANDWIDTH = 5 # the monitoring rate, aka after how many seconds the backend should check for new records
total_num_alive_rabbits = 100

def handle_new_records(new_records: list[dict]) -> bool:
    global total_num_alive_rabbits
    try:
        for record in new_records:
            new_rabbits_total = total_num_alive_rabbits + record["newborn_count"] - record["death_count"]
            if not(total_num_alive_rabbits < 0):
                total_num_alive_rabbits = new_rabbits_total
                print("New total rabbits:", total_num_alive_rabbits)
        return True
    except Exception as error:
        print("Encountered an error in handle_new_records:", error)
        return False


def main() -> None:
    active = True
    while active:
        print(f"Rabbits total #: {total_num_alive_rabbits}")
        # check how many new records we have in the db:
        new_records = handle_failure(db.get_new_records)
        if new_records is not None and len(new_records) >= 10:
            print("Handling new records....")
            success_handling = handle_new_records(new_records)

            if success_handling:
                print("Reset 'new records' list")
                handle_failure(db.reset_new_records_list)
        time.sleep(BANDWIDTH)


if __name__ == "__main__":
    handle_failure(db.reset_all)
    main()