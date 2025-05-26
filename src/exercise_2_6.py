sum_primes = 0
for number in range(3, 1000, 2):
    isprime = True
    for i in range(3, number):
        if number % i == 0:
            isprime = False
            break
    sum_primes = sum_primes + number if isprime else sum_primes
print(sum_primes)
