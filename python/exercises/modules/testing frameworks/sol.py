# Testing framework

import testing_package.testing_module as tmd
import to_be_tested.funcs_to_test as f


print(tmd.is_equal(f.func1(), 9)) # should return True
print(tmd.is_greater_than(f.func1(), 9)) # should False
print(tmd.is_less_than(f.func1(), 9)) # should return False
print(tmd.is_in_list("to", f.func2())) # should return True
print(tmd.is_key_in_dict("key2", f.func3())) # should return True
print(tmd.is_value_in_dict("val2", f.func3())) # should return False