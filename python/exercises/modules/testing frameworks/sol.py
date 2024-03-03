# Testing framework

from testing_package.testing_module import *
import to_be_tested.funcs_to_test as f

tst = Testing_machine()

print(tst.test(f.get_int()).is_equal(9).is_greater_than(5)) # should return True
print(tst.test("to").is_in_list(f.get_list())) # should return True
print(tst.test("key2").is_key_in_dict(f.get_dict())) # should return True
print(tst.test("val2").is_value_in_dict(f.get_dict())) # should return False

print(tst.test("key2").is_key_in_dict(f.get_dict()).is_in_list(f.get_list())) # should return False (first assertion is True but the second one is False)

