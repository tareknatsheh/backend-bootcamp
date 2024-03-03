# Testing framework

import testing_module as tmd

def func1_to_test():
    return 9

tmd.is_equal(9, func1_to_test())
