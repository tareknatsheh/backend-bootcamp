from fibonacci import fibo

def test_fibo_rec():
    assert fibo.fibo_rec(10) == 55

def test_fibo_memo():
    assert fibo.fib_memo(10) == 55