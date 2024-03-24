from number_search import num_search

def test_num_loop_search():
    test_list = [2, 9, 4, 6, 3, 1, 8, 5, 7]
    
    assert num_search._loop_search(test_list, 8) == True
    assert num_search._loop_search(test_list, 80) == False

def test_binary_search_recursive():
    test_list = [2, 9, 4, 6, 3, 1, 8, 5, 7]

    assert num_search._binary_search_recursive(test_list, 8, 0, len(test_list) - 1) == True
    assert num_search._binary_search_recursive(test_list, 80, 0, len(test_list) - 1) == False