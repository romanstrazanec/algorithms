from fibonacci import fib


def phi():
    try:
        return 1 + 1 / phi()
    except RecursionError:
        return 1


def fi(i=27):
    if i < 3:
        return 0
    return fib(i) / fib(i-1)


def golden_ratio():
    return (1 + 5**(.5))*.5
