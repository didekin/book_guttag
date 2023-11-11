def amortization(rate, numperiods, presentval):
    return rate * (1 + rate) ** numperiods * presentval / ((1 + rate) ** numperiods - 1)


print(amortization(.01, 60, 1000))
