import luenberger_invest_book.luenberger as lu

f_rate = .04
r_rate = .1
real_rate = (r_rate - f_rate) / (1 + f_rate)

CF = [-(10 ** 4), 5 * 10 ** 3, 5 * 10 ** 3, 5 * 10 ** 3, 3 * 10 ** 3]

print(lu.npv_arr(real_rate, CF))
