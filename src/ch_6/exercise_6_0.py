def harmonic(n):
    if isinstance(n, int):
        if n != 1:
            return 1 / n + harmonic(n - 1)
        else:
            return n
    else:
        print(f'error: {n} not an integer')
        return None


test_1 = harmonic(1)
test_2 = harmonic(2)
test_3 = harmonic(5)
test_4 = harmonic(1 / 2)
