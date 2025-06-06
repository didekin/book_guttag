trialnum = int(input('Number, please: '))
isPrime = True
greatestDiv = trialnum
for divisor in range(2, trialnum, 1):
    if trialnum % divisor == 0:
        isPrime = False
        greatestDiv = trialnum / divisor
        break
print(f'Is prime = {isPrime}; greatest divisor = {greatestDiv}')

# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a
# message to that effect

power = 1
trialnum = int(input('Please, number:'))
root = int(trialnum / 2 if trialnum % 2 == 0 else (trialnum + 1) / 2)
hasRoot = False
for r in range(2, root + 1):
    if hasRoot:
        break
    p = 1
    while r ** p < trialnum and p < 6:
        p = p + 1
        if r ** p == trialnum:
            power = p
            root = r
            hasRoot = True
            break
print(f'root = {root}, power = {power}' if hasRoot else f'No root')
