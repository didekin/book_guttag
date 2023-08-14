x = int(input("Number to power: "))

root = 0
pwd = 2
withpower = False

while root ** pwd < abs(x):
    root += 1
    for pwd in range(2, 6):
        if root ** pwd >= abs(x):
            if root ** pwd == abs(x):
                withpower = True
                print(f"root= {root}, pwd= {pwd}")
            break
    if withpower:
        break
    pwd = 2
if not withpower:
    print(f"Number {x} has no power")

