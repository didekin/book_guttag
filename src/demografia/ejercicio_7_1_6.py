def defunciones(prob_muerte):
    difuntos_age = []
    supervivientes_age = [100000]
    i = 0
    for q in prob_muerte[0:len(prob_muerte)]:
        difuntos_age.append(supervivientes_age[i] * q)
        supervivientes_age.append(supervivientes_age[i] - difuntos_age[i])
        i += 1
    return difuntos_age, supervivientes_age[:len(difuntos_age)]


def supervivientes(prob_supervivencia):
    supervivientes_age = [100000]
    i = 0
    for p in prob_supervivencia[0:len(prob_supervivencia) - 1]:
        supervivientes_age.append(p * supervivientes_age[i])
    return supervivientes_age


def pob_estacionaria(supervivientesIn, defuncionesIn, mortality_lastgroup):
    pob_estacionariaOut = []
    for i in range(len(supervivientesIn)):
        if i == 0:
            continue
        if i == 1:
            pob_estacionariaOut.append(supervivientesIn[i] + (0.1 * defuncionesIn[i - 1]))
            continue
        if i == 2:
            pob_estacionariaOut.append(4 * (supervivientesIn[i] + (0.4 * defuncionesIn[i - 1])))
            continue
        pob_estacionariaOut.append(5 * (supervivientesIn[i] + supervivientesIn[i - 1]) / 2)
        if i == len(supervivientesIn) - 1:
            pob_estacionariaOut.append(supervivientesIn[i] / mortality_lastgroup)
            break
    return pob_estacionariaOut


pob_male_age_01012004 = [21245, 74864, 94654, 99776, 108410, 130386, 164312, 182068, 179681, 167643, 150924, 132706,
                         117991, 102153, 88105, 78844, 62991, 41681, 30349]
pob_female_age_01012004 = [19953, 70513, 89793, 94411, 102806, 124361, 154546, 171341, 173009, 164606, 150595, 133982,
                           122617, 109042, 100130, 96038, 87318, 69283, 71065]
male_mort_age_2003 = [4.989, 0.681, 0.486, 0.551, 0.876, 0.974, 0.834, 0.956, 1.219, 2.040, 2.717, 4.687, 7.653, 10.093,
                      19.545, 34.993, 53.674, 69.888, 147.451]
male_mort_age_2003_one = [x / 1000 for x in male_mort_age_2003]
female_mort_age_2003 = [3.959, 0.61, 0.334, 0.339, 0.37, 0.33, 0.291, 0.379, 0.474, 0.936, 1.162, 1.881, 2.936, 3.861,
                        7.880, 16.004, 27.875, 43.026, 121.494]
female_mort_age_2003_one = [x / 1000 for x in female_mort_age_2003]

t_fecundidad_age_2003 = [4.41, 29.05, 67.55, 97.56, 47.96, 8.87, 1.45]
t_fecundidad_age_2003_one = [x / 1000 for x in t_fecundidad_age_2003]
ratio_male_female = 105 / 205

ts_male_migrat_age_2003 = [0.00, 0.00, 0.00, 2.33, 15.73, 22.88, 17.17, 8.72, 1.64, 0.91, 0.00, 0.00, 0.00, 0.00, 0.00,
                           0.00, 0.00, 0.00]
ts_female_migrat_age_2003 = [0.00, 0.00, 0.00, 1.38, 11.55, 17.99, 13.82, 6.14, 1.04, 0.31, 0.00, 0.00, 0.00, 0.00,
                             0.00,
                             0.00, 0.00, 0.00]

ages_tab_mortality = list(range(0, 90, 5))
year_interval = 5
q_male_age_0_5 = [male_mort_age_2003_one[0],
                  ((4 * 2) * male_mort_age_2003_one[1]) / (2 + (4 * male_mort_age_2003_one[1]))]
q_male_age_10_80 = [(year_interval * 2) * x / (2 + (year_interval * x)) for x in
                    male_mort_age_2003_one[2:len(male_mort_age_2003_one) - 1]]
q_male_all_ages = q_male_age_0_5 + q_male_age_10_80 + [1]
p_male_all_ages = [1 - x for x in q_male_all_ages]
d_male_age, l_male_age = defunciones(q_male_all_ages)
L_male_age = pob_estacionaria(l_male_age, d_male_age, male_mort_age_2003_one[len(male_mort_age_2003_one) - 1])
S_0_N = [(L_male_age[0] + L_male_age[1]) / 500000]
S_plus_85 = [L_male_age[len(L_male_age) - 1] / (L_male_age[len(L_male_age) - 1] + L_male_age[len(L_male_age) - 2])]
S_5_10 = [L_male_age[2] / (L_male_age[0] + L_male_age[1])]
S_10_85 = [x / y for x, y in zip(L_male_age[3:len(L_male_age) - 1], L_male_age[2:len(L_male_age) - 2])]
S_male_all = S_0_N + S_5_10 + S_10_85 + S_plus_85

S_female_all = [0.99547, 0.99731, 0.99832, 0.99823, 0.99825, 0.99845, 0.99833, 0.99787, 0.99648, 0.99477, 0.99243,
                0.98805, 0.98317, 0.97122, 0.94259, 0.89745, 0.83996, 0.59499]
S_female_nacim = S_female_all[0]
S_female_last = S_female_all[len(S_female_all) - 1]
S_female_medium = S_female_all[1:len(S_female_all) - 1]
# Agrupo las edades 0 y 1-4 en 0-4.
pob_female_comp_age_010104 = [sum(pob_female_age_01012004[0:2])] + pob_female_age_01012004[2:]
# población en últimos dos grupos de edad:
pob_female_age_last = pob_female_comp_age_010104[-2:]
pob_female_medium = pob_female_comp_age_010104[:-2]
assert len(pob_female_age_last) == 2
#  Hay que calcular el saldo migratorio para mujer por edad, quitando las 2 últimas.
SM_female_age_medium = [(x * y / 1000) * year_interval for x, y in
                        zip(pob_female_medium, ts_female_migrat_age_2003[0:-2])]
# Estimo población femenina salvo nacimientos y grupo final. Edades 5-84 años.
pob_female_04_09_medium = [p * S + sm for p, S, sm in zip(pob_female_medium, S_female_medium, SM_female_age_medium)]
# Estimo pob. femenina último grupo.
SM_female_age_last = [pob * tm / 1000 for pob, tm in zip(pob_female_age_last, ts_female_migrat_age_2003[-2:])]
pob_female_04_09_last = sum(pob_female_age_last) * S_female_last + sum(SM_female_age_last)
pob_female_04_09_all = pob_female_04_09_medium + [pob_female_04_09_last]

# Con la población estimada femenina, puedo calcular las poblaciones intermedias y aplicarles la tasa de fecundidad.
pob_female_fecunda_010104_age = pob_female_comp_age_010104[3:10]
# la tabla empieza en 5 años, no en 0, porque aún no hay nacimientos.
pob_female_fecunda_010109_age = pob_female_04_09_all[2:9]
pob_female_fecunda_avg = [(x + y) / 2 for x, y in zip(pob_female_fecunda_010104_age, pob_female_fecunda_010109_age)]
# Nacimientos sin coeficiente de masculinidad.
nacimientos_04_08 = [x * y * year_interval for x, y in zip(t_fecundidad_age_2003_one, pob_female_fecunda_avg)]
nacimientos_varon_04_08 = [x * ratio_male_female for x in nacimientos_04_08]
nacimientos_mujer_04_08 = [x * (1 - ratio_male_female) for x in nacimientos_04_08]
pob_female_04_09_gr1 = sum(nacimientos_mujer_04_08) * S_female_nacim + (1 + ts_female_migrat_age_2003[1] / 1000)
pob_female_04_09 = [pob_female_04_09_gr1] + pob_female_04_09_all

# ========================================== Ejercicio 7.1.7 ====================================================

ts_female_migrat_age_2003_B = [1.80, 5.41, 6.54, 4.26, 8.48, 7.30, 6.17, 5.61, 3.99, 1.88, 1.81, 1.51, 4.46, 5.68, 4.83,
                               5.47, 2.86, 0.45]
# Recalculo saldos migratorios.
SM_female_age_medium_B = [(x * y / 1000) * year_interval for x, y in
                          zip(pob_female_medium, ts_female_migrat_age_2003_B[0:-2])]
SM_female_age_last_B = [(pob * tm / 1000) * year_interval for pob, tm in zip(pob_female_age_last, ts_female_migrat_age_2003_B[-2:])]
pob_female_04_09_medium_B = [p * S + sm for p, S, sm in zip(pob_female_medium, S_female_medium, SM_female_age_medium_B)]
pob_female_04_09_last_B = sum(pob_female_age_last) * S_female_last + sum(SM_female_age_last_B)
# Recalculo la población fecunda media.
pob_female_fecunda_010109_age_B = pob_female_04_09_medium_B[2:9]
pob_female_fecunda_avg_B = [(x + y) / 2 for x, y in zip(pob_female_fecunda_010104_age, pob_female_fecunda_010109_age_B)]
# Recalculo nacimientos
nacimientos_04_08_B = [x * y * year_interval for x, y in zip(t_fecundidad_age_2003_one, pob_female_fecunda_avg_B)]
nacimientos_mujer_04_08_B = [x * (1 - ratio_male_female) for x in nacimientos_04_08_B]

pob_female_04_09_gr1_B = sum(nacimientos_mujer_04_08_B) * S_female_nacim + (1 + ts_female_migrat_age_2003_B[1] / 1000)
pob_female_04_09_B = [pob_female_04_09_gr1_B] + pob_female_04_09_medium_B + [pob_female_04_09_last_B]

