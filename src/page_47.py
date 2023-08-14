sumprime = 1 + 2
for i in range(3, 999, 2):
    divisible = False
    for j in range(3, 31):
        if j >= i:
            break
        if i % j == 0:
            divisible = True
            break
    if not divisible:
        sumprime += i
        print(f'number {i}, sumprime= {sumprime}')
