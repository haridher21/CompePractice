def getNthFib(n):
    a, b, c = 0, 1, 1
    while n - 1 > 0:
        a, b, c = b, c, b + c
        n -= 1
    return a
