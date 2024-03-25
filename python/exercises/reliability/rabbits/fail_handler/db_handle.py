"""
Handles the DB read/write failures to make sure that our backend at least tries n more times
before timing out and giving up on the db
"""

def handle_failure(func, num_of_try=5, *args):
    counter = 0
    active = True
    while active:
        counter += 1
        try:
            if len(args):
                return func(*args)
            else:
                return func()
        except Exception as error:
            if counter < num_of_try:
                print(f"failure #: {counter}, let's try again")
            else:
                raise error
        else:
            active = False