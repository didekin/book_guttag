def geometric_prog(rate, numsums):
    return (1 - rate ** numsums) / (1 - rate)


def inf_geom_prog(rate):
    return 1 / (1 - rate)


def sum_disc_factors(rate, numsums):
    discount = (1 + rate) ** -1
    return geometric_prog(discount, numsums)


def inf_sum_disc_factors(rate):
    discount = (1 + rate) ** -1
    return inf_geom_prog(discount)


# disfactor is the form (1 + r)**n
def inf_sum_discfactors(discfactor):
    discount = discfactor ** -1
    return inf_geom_prog(discount)


def npv_arr(rate, cashflows):
    df = []
    for i in range(len(cashflows)):
        df.append(cashflows[i] / (1 + rate) ** i)
    print(df)
    return sum(df)


# Newton algorithm
def newton(guess0, function, dev_function):
    guess = guess0
    while abs(function(guess)) > 0.001:
        guess = guess - function(guess) / dev_function(guess)
    return guess
