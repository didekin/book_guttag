# Today: 1992
def compound(rate, yearfrom, yearto, amount):
    return (1 + rate)**(yearto - yearfrom) * amount


print(compound(.033, 1776, 1992, 1))
print(compound(.066, 1776, 1992, 1))
