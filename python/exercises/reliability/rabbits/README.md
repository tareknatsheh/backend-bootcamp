# Rabbit population monitoring system

It consists of three separated parts:
1) **Sensor**

    Generates data and writes it to the db in random time intervals
2) **DB**

    Handles: receiving, saving and sending the data
3) **Backend**

    Only talks to the DB
    Get's the new data from DB every 10 new records
    plots it


### Points of failure
a) DB: it's programmed to fail every now and then, therefore I've created a failure handler (check Backend/utils/db_handle.py)
b) Backend: It assumes that each record has "newborn_count" and "death_count" keys, if that is not the case, it will fail