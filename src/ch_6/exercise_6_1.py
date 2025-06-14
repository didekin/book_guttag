def fib(n):
    print(f'number computed: {n}')
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


counter = 0
fib(5)
