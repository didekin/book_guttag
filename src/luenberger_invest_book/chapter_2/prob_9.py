import luenberger_invest_book.luenberger as lu

rate = 0.05
years_today = 5
nominal = 20000
disc_fromtoday = nominal * (lu.inf_sum_discfactors((1 + rate) ** 20))
disc_from5years = disc_fromtoday * (1+rate)**(-years_today)
print(f'value roof: {disc_fromtoday-disc_from5years}')
