x = int(input("Number to analyse: "))

smalldiv, greatdiv = 1, 1
for divisor in range(2, x):
    if x % divisor == 0:
        smalldiv = divisor
        greatdiv = int(x / smalldiv)
        break
print(f"smallestdiv = {smalldiv}")
print(f"greatdiv = {greatdiv}")
