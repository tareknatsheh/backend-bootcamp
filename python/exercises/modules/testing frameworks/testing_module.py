def is_equal(tested_val, num):
    if tested_val == num:
        print(f"Test success: {tested_val} == {num}")
    else:
        raise Exception(f"Test failed: {tested_val} == {num}")