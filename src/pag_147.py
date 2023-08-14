def harmonic(n):
    if n == 1:
        return n
    else:
        return harmonic(n - 1) + 1 / n


print(harmonic(3))
