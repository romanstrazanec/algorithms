def phi():
    try:
        return 1 + 1 / phi()
    except RecursionError:
        return 1
