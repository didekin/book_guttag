# The Empire State Building is 102 stories high. A man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the top floor. If it broke, he would go down a floor,
# and try it again. He would do this until the egg did not break. At worst, this method requires 102 eggs. Implement
# a method that at worst uses seven eggs.

high = 102
low = 0
trial = (high + low) / 2
len_interval = high - low
is_not_broken = True
num_trial = 0
while len_interval >= 2:
    num_trial = num_trial + 1
    if is_not_broken:
        low = trial
        trial = (high + low) / 2
        len_interval = high - low
print(f'number_trials = {num_trial}')

# The worst case for the broken in successive steps is similar.
