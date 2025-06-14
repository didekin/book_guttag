non_primes_100 = [x for x in range(2, 100) if any(x % y == 0 for y in range(3, x, 2)) or x in range(4, 100, 2)]
print(non_primes_100)
