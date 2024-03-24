from word_counter import word_counter

def test_using_brute():
    test_text = "the brown fox is the fox"
    assert word_counter.using_brute(test_text) == {'the': 2, 'brown': 1, 'fox': 2, 'is': 1}

def test_using_memo():
    test_text = "the brown fox is the fox"
    assert word_counter.using_memo(test_text) == {'the': 2, 'brown': 1, 'fox': 2, 'is': 1}