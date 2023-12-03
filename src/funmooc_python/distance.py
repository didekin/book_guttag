import math


def distance(*args):
    distsqr = 0
    for i in args:
        distsqr += i**2
    return math.sqrt(distsqr)



