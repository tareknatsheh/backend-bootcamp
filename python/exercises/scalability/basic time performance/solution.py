from fibonacci import fibo
from number_search import num_search
from word_counter import word_counter
from utils.helper import *

from lorem_text import lorem


def fibonacci():
    """
    Handles invoking and drawing the CPU time for two fibonacci funcitons using different input sizes
    One of them is implemented using recursion O(2^n)
    The other one is using memoization O(n)
    """
    nums = [x for x in range(0, 33)]
    execution_time_memo = get_exe_time(fibo.fib_memo, nums)
    execution_time_rec = get_exe_time(fibo.fibo_rec, nums)
    draw_results(nums, execution_time_rec, execution_time_memo)


def number_search():
    """
    Tests two searching algorithms, one is a simple for loop O(n),
    the other one is using binary search O(logn)
    Note that if the list is not sorted, the normal for loop beats the binary search.
    If the list IS sorted the binary seatch shines
    """
    sizes_of_lists_to_search = [x**2 for x in range(10,150)]
    lists_to_search = []
    for size in sizes_of_lists_to_search:
        result = get_random_list_of_nums_of_size(size)
        lists_to_search.append(result)

    # If you don't sort it, binary search would perform much much worse!
    lists_to_search.sort()
    execution_time_loop = get_exe_time(num_search.num_search_loop, lists_to_search)
    execution_time_binary = get_exe_time(num_search.num_search_binary, lists_to_search)
    draw_results(sizes_of_lists_to_search, execution_time_loop, execution_time_binary)
    pass


def count_word():
    """
    Counts the occurancies of words in provided string of words
    The first brute force function loops over the words one by one and handle a word at a time O(n^2)
    The other one uses memoization with a hash table, it touches every element only once O(n).
    """
    sizes_to_handle = [x for x in range(10, 400)]
    list_of_texts_to_handle: list[str] = [lorem.words(s) for s in sizes_to_handle]

    execution_time_1 = get_exe_time(word_counter.using_brute, list_of_texts_to_handle)
    execution_time_2 = get_exe_time(word_counter.using_memo, list_of_texts_to_handle)
    draw_results(sizes_to_handle, execution_time_1, execution_time_2)
    pass


if __name__ == "__main__":
    fibonacci()
    number_search()
    count_word()