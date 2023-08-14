def log(x, base, epsilon):
    """
    Assumes x and epsilon int or float, base an int,
           x > 1, epsilon > 0 & power >= 1
       Returns float y such that base**y is within epsilon
    of x.
    """
    low = 0
    high = x
    y = (low + high) / 2
    while abs(base ** y - x) >= epsilon:
        if base ** y > x:
            high = y
        else:
            low = y
        y = (low + high) / 2
    return y


print(log(2, 2, 0.001))
print(log(8.8, 2, 0.001))

