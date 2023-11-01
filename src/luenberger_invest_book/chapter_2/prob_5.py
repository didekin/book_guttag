import luenberger_invest_book.luenberger as geo

period_amount = 500000
periods = 20
rate = 0.1
print(geo.sum_disc_factors(rate, periods) * period_amount)

