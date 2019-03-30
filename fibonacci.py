def fib(i):
    if 0 < i < 3:
        return 1
    if i > 2:
        return fib(i-1) + fib(i-2)
    return 0
