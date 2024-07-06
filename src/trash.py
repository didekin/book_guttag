import math as math

pob_01012000 = 4098322
nacimientos_year = [33069, 34901, 37853, 41198]
defunciones_year = [36509, 36724, 37316, 37760]
inmigrantes_year = [3750, 9018, 14346, 20084]
emigrantes_year = [4650, 2819, 1663, 908]
crecimiento_natural_year = [x - y for x, y in zip(nacimientos_year, defunciones_year)]
saldo_mig_year = [x - y for x, y in zip(inmigrantes_year, emigrantes_year)]
crecimiento_year = [x + y for x, y in zip(crecimiento_natural_year, saldo_mig_year)]
crecimiento_tot = sum(crecimiento_year)

pob_01012001 = pob_01012000 + crecimiento_year[0]
pob_01012002 = pob_01012001 + crecimiento_year[1]
pob_01012003 = pob_01012002 + crecimiento_year[2]
pob_01012004 = pob_01012003 + crecimiento_year[3]

pob_by_year = [pob_01012000, pob_01012001, pob_01012002, pob_01012003]
percent_year = [(x / y) * 100 for x, y in zip(crecimiento_year, pob_by_year)]
percent_acum = (math.pow((pob_01012004 / pob_01012000), 1 / 4) - 1) * 100

pob_01012009_ar = pob_01012004 * (1 + percent_year[3] / 100 * 5)
pob_01012009_geo = pob_01012004 * math.pow((1 + percent_year[3] / 100), 5)
pob_01012009_exp = pob_01012004 * math.pow(math.e, percent_year[3] / 100 * 5)
pob_01012009_log = 8000000 / (1 + (math.exp((-percent_year[3] / 100) * 19)))

#  1.6
# Cifras para 2000, 2001, 2002 y 2003
pob_avg_2003 = (pob_01012003 + pob_01012004) / 2
tb_nat_2003 = nacimientos_year[3] / pob_avg_2003
tb_mort_2003 = defunciones_year[3] / pob_avg_2003
tb_migr_2003 = saldo_mig_year[3] / pob_avg_2003
tb_crec_2003 = tb_nat_2003 - tb_mort_2003 + tb_migr_2003
pob_est_year = [pob_01012004 * math.pow((1 + tb_crec_2003), i) for i in range(1, 6)]
