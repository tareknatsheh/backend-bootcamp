import random

def _loop_search(num_list: list[int], target) -> bool:
    for num in num_list:
        if num == target:
            return True
    
    return False


def rec_binary_search(num_list, target) -> bool:
    if not num_list:
        return False

    middle_index = len(num_list) // 2
    num_at_the_middle = num_list[middle_index]

    if target == num_at_the_middle:
        return True
    elif target > num_at_the_middle:
        return rec_binary_search(num_list[middle_index + 1:], target)
    else:
        return rec_binary_search(num_list[:middle_index], target)


def _binary_search_recursive(nums, target, low, high):
    if high < low:
        return False

    # the middle element
    mid = (low + high) // 2 

    if nums[mid] == target:
        return True
    elif target < nums[mid]:
        return _binary_search_recursive(nums, target, low, mid - 1) 
    else:
        return _binary_search_recursive(nums, target, mid + 1, high)
    

def num_search_binary(num_list: list[int]) -> bool:
    target = random.randint(0, len(num_list) - 1)
    return _binary_search_recursive(num_list, target, 0, len(num_list) - 1)

def num_search_loop(num_list: list[int]) -> bool:
    target = random.randint(0, len(num_list) - 1)
    return _loop_search(num_list, target)
