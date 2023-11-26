def dispatch1(a, b):
    apair = a % 2 == 0
    bpair = b % 2 == 0
    if apair and bpair:
        return a ** 2 + b ** 2
    elif apair and not bpair:
        return a * (b - 1)
    elif not apair and bpair:
        return (a - 1) * b
    else:
        return a ** 2 - b ** 2


print(dispatch1(3, 7))


def dispatch2(a, b, ens1, ens2):
    if a in ens1 and b not in ens2:
        return a * (b - 1)
    elif a not in ens1 and b in ens2:
        return (a - 1) * b
    else:
        return a ** 2 + b ** 2


print(dispatch2(3, 7, (2, 4, 6), {8, 10, 6}))
