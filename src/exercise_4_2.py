def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
           x > 1, epsilon > 0
           Returns float y such that base**y is within epsilon of x."""
    if not isinstance(x, int) or (not isinstance(epsilon, int) and not isinstance(epsilon, float)):
        return f'wrong types. x type: {type(x)}. epsilon type: {type(epsilon)}'
    if x <= 1:
        return f'x < 1'
    if epsilon < 0:
        return f'epsilon < 0'
    high = 0
    while base ** high < x:
        high += 1
    low = high - 1
    log_x = (low + high) / 2
    while abs(x - base ** log_x) > epsilon:
        if x < base ** log_x:
            high = log_x
        else:
            low = log_x
        log_x = (low + high) / 2
    return log_x


print(log(.5, 2, 0))
print(log(-1, 2, 0))
print(log(2, 2, -1))
print(log(4,2,.01))
print(log(9,4,.001))

