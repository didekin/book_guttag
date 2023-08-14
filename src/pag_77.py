x = int(input("Number to power: "))

epsilon = 0.01
num_guesses = 0
low = 0
high = max(1,x)
resp = (high + low)/2

while abs((resp**2 - x)) > epsilon and (num_guesses < 5):
    num_guesses += 1
    print(f"high = {high}, low = {low}, resp = {resp}")
    if resp**2 > x:
        high = resp
    if resp**2 < x:
        low = resp
    resp = (high + low) / 2
print(f"num_guesses = {num_guesses}, for x = {x}")



