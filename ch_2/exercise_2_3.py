# Finger exercise: Write a program that examines three variables— x, y, and z—and prints the largest odd number among
# them. If none of them are odd, it should print the smallest value of the three.

def function_A(x, y, z):
    largest = max(x, y, z)
    smallest = min(x, y, z)
    if largest % 2 != 0:
        print(largest)
    else:
        print(smallest)


function_A(4, 2, 6)
