def power(x, n):
    print('vuelta')
    sqr = x * x
    return powerec(n, sqr, x)


def powerec(n, sqr, x):
    if not n:
        return 1
    if n == 1:
        return x
    if n == 2:
        return sqr
    if n % 2 == 0:
        return power(x, n - 2) * sqr
    else:
        return power(x, n - 1) * x
