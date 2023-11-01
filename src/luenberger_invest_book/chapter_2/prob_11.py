import luenberger_invest_book.luenberger as lu

project1 = [-100, 30, 30, 30, 30, 30]
project2 = [-150, 42, 42, 42, 42, 42]


def fu1(x):
    return -100 + 30 * (x + x ** 2 + x ** 3 + x ** 4 + x ** 5)


def derfu1(x):
    return 30 * (1 + 2 * x + 3 * x ** 2 + 4 * x ** 3 + 5 * x ** 4)


def irrfunc(init_q, period_q):
    def f1(x):
        return -init_q + period_q * (x + x ** 2 + x ** 3 + x ** 4 + x ** 5)

    return f1


def irr_der_func(period_q):
    def f2(x):
        return period_q * (1 + 2 * x + 3 * x ** 2 + 4 * x ** 3 + 5 * x ** 4)

    return f2


# We apply Newton algorithm to get a root; then the formula rate = 1/root - 1.
irr1 = 1 / lu.newton(.95, irrfunc(100, 30), irr_der_func(30)) - 1
irr2 = 1 / lu.newton(.95, irrfunc(150, 42), irr_der_func(42)) - 1
print(f'irr1: {irr1}')
print(f'irr2: {irr2}')

rate = .064
netpresent1 = -100 + (30 / (1 + rate)) * lu.sum_disc_factors(rate, 5)
netpresent2 = -150 + (42 / (1 + rate)) * lu.sum_disc_factors(rate, 5)
print(f'netpresent1: {netpresent1}')
print(f'netpresent2: {netpresent2}')
