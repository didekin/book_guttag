def p_x(x_in, k_in):
    return x_in ** 2 - k_in


def p_dev_x(x_in):
    return 2 * x_in


epsilon = 0.02
k = 24
guess = k / 2
num_trials = 0
while abs(p_x(guess, k)) > epsilon:
    num_trials = num_trials + 1
    guess = guess - p_x(guess, k) / p_dev_x(guess)
print(f'num_trials = {num_trials}, guess = {guess}')