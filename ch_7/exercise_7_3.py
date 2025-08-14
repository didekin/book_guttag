from modules import guttag_module as gu

fib_numbers = [gu.fibonannci_gen(n) for n in range(1, 11)]
with open('./fib_10_numbers', "w") as fib_handle:
    for n in fib_numbers:
        fib_handle.write(str(n) + '\n')
with open('./fib_10_numbers', 'r') as fib_handle:
    for line in fib_handle:
        print(line[:-1])


