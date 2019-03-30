def fib(i: int) -> int:
    if 0 < i < 3:
        return 1
    if i > 2:
        return fib(i-1) + fib(i-2)
    return 0


def difffib(i: int, d: int = 0) -> int:
    return fib(1+d)*fib(i-2-d) + fib(2+d)*fib(i-1-d)


def effib(i: int) -> int:
    if i == 1:
        return 1
    if i < 1:
        return 0
    hi = i // 2
    f = effib(hi)
    return f*f + effib(hi+1)**2 if i % 2 else f*f + 2*f*effib(hi-1)
