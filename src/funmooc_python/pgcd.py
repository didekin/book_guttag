def pgcd(a, b):
    """Le PGCD (minimum common divisor) avec une fonction iterative"""
    if b == 0:
        return a
    while a % b:
        a, b = b, a % b
    return b


print(pgcd(56, 8))
