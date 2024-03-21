"""
Rabbit population monitoring system

It consists of three separated parts:
1) Sensor
    Generates data and writes it to the db in random time intervals
2) DB
    Handles: receive, save and send the data
3) Backend
    Only talks to the DB
    Get's the new data from DB every 10 new records
    plots it

"""
import sys


def main():
    pass

if __name__ == "__main__":
    print(sys.path)
    main()