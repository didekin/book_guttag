taxesDic = {(0, 12500): 0, (12500, 50000): 0.2, (50000, 150000): .4, (150000, float('inf')): .45}


def taxes(income):
    for interv in taxesDic.keys():
        if interv[0] <= income < interv[1]:
            return taxesDic[interv] * income


print(taxes(200000))