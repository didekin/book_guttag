x = int(input("Number to analyse: "))

smalldiv = 1
for divisor in range(2,x):
    if x%divisor == 0:
        smalldiv = divisor
        break
print(f"smallestdiv = {x if smalldiv ==1 else x/smalldiv}")

