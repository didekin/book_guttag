def effective_rate(nominal, units_in_year):
    return (1 + nominal / units_in_year) ** units_in_year


print(effective_rate(0.03, 12))
print(effective_rate(0.18, 12))
print(effective_rate(0.18, 4))
