# Testing framework

from testing_package import numbers, lists, dicts
import to_be_tested.funcs_to_test as f

test_num = numbers.Numbers()
test_list = lists.Lists()
test_dict = dicts.Dicts()


print(test_num.test(f.get_int()).is_equal(9).is_greater_than(5)) # should return True
print(test_list.test("to").is_in_list(f.get_list())) # should return True
print(test_dict.test("key2").is_key_in_dict(f.get_dict())) # should return True
print(test_dict.test("val2").is_value_in_dict(f.get_dict())) # should return False
print(test_dict.test("key2").is_key_in_dict(f.get_dict()).is_value_in_dict(f.get_dict())) # should return False (first assertion is True but the second one is False)

