def fibo_rec(n):
    if n <= 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]