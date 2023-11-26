def amortization(rate, numperiods, presentvalue):
    return rate * (1 + rate) ** numperiods * presentvalue / ((1 + rate) ** numperiods - 1)


def presentval(rate, numperiods, annuity):
    return annuity / rate * (1 - (1 + rate) ** (-numperiods))


def presentval_points(presentvalue, points):
    return presentvalue * (1 - points)


presentval_1 = presentval(.07625 / 12, 360, 1474.1)
annuity_1 = amortization(.16, 10, 100000)
print(annuity_1)
