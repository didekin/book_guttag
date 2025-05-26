num_x = int(input('How many times should I print the letter X? '))
to_print = ''
# concatenate X to to_print num_x times
iterations = 0
while iterations < abs(num_x):
    to_print = to_print + 'X'
    iterations = iterations + 1
print(to_print)

# ==================

iterations = 0
greatest = 0
while iterations < 10:
    number = int(input('Enter an integer number:'))
    if iterations == 0:
        greatest = number
    else:
        if number == greatest:
            continue
        else:
            greatest = number if (number > greatest and number % 2 != 0) else greatest
    iterations = iterations + 1
print(f'Largest odd number = {greatest}' if greatest % 2 != 0 else f'No odd number')
