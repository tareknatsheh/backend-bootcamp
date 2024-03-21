import sys
import utils.json_fns as fns

def try_n_times(num_of_attempts, func_to_try, params):
    while num_of_attempts > 0:
        try:
            # print(f"attemp No {num_of_attempts}")
            result = func_to_try(params)
            return result
        except:
            num_of_attempts -= 1
            if num_of_attempts == 0:
                raise Exception("Failed to read")



try:
    if len(sys.argv)>1:
        # Take first arg
        operation = sys.argv[1:][0]
        match operation:
            case 'read':
                try:
                    try_n_times(3, fns.read_from_json, "journal.json")
                except Exception as error:
                    try:
                        print(f"Couldn't read from journal.json, will try to read from 'journal copy.json'")
                        try_n_times(3, fns.read_from_json, "journal copy.json")
                    except Exception as error:
                        print("second read attempt failed!")
            case 'write':
                msg = input("what is your msg? ")
                if msg:
                    if len(msg) <= 3:
                        print("Message should be at least 3 characters")
                    else:
                        fns.write_to_json(msg)
            case _:
                print(f"{operation} is not recognized.")
    else:
        print("no operator")
except Exception as error:
    print("500: Somethine went wrong.")
    print(f"{error}")