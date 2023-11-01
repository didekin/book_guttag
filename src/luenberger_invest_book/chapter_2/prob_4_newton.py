import luenberger_invest_book.luenberger as lu


def func_1(x):
    return -1 + x + x ** 2


def dev_func_1(x):
    return 1 + 2 * x


root = lu.newton(1, func_1, dev_func_1)
print(f'root: {root}')
print(f'value f(root): {func_1(root)}')
