import luenberger_invest_book.luenberger as lu

x0 = 10 ** 7
sales_year = 10 ** 6 * 3.3
cost_year = 10 ** 4 * 30 + 10 ** 4
tax_rate = .34
deprec_year = 0.2
nominal_r = .12
inflation_r = .04
real_r = (nominal_r - inflation_r) / (1 + inflation_r)

profit_year_beftax = sales_year - cost_year
taxes_year = (profit_year_beftax - deprec_year * x0) * tax_rate

cash_year = profit_year_beftax - taxes_year
allcash = [-x0] + [cash_year] * 5
npv1 = lu.npv_arr(nominal_r, allcash)
npv2 = lu.npv_arr(real_r, allcash)
print(npv1)
print(npv2)
