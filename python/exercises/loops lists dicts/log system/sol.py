# Log system

# We need to have a log function or class
# We want a one single factory function that generates new logging functions based on and
# and built above a basic abstract logging function

import time

# log with just a msg - no timestamp
class Logger:
    def log(self, msg):
        print(msg)

my_logger = Logger()
my_logger.log("Hello freaks!")

#  log with msg + timestamp
def loggers_creator(addon):
    def log_w_timestamp(msg):
        print(msg, addon)
    return log_w_timestamp

my_log = loggers_creator(time.time())

my_log("Soo")