def is_equal(val_to_test, num):
    if val_to_test == num:
        return True
    else:
        return False

def is_greater_than(val_to_test, num):
    if val_to_test > num:
        return True
    else:
        return False

def is_less_than(val_to_test, num):
    if val_to_test < num:
        return True
    else:
        return False
    
def is_in_list(val_to_test, list = []):
    if val_to_test in list:
        return True
    else:
        return False

def is_key_in_dict(val_to_test, dict = {}):
    if val_to_test in dict:
        return True
    else:
        return False

def is_value_in_dict(val_to_test, dict = {}):
    if val_to_test in dict.values():
        return True
    else:
        return False

if __name__ == "__main__":
    print("You are running code directly")
else:
    print("Imported Testing Module!")