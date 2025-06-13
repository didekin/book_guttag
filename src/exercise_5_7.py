import random
import string


def get_min(d):
    """d a dict mapping letters to ints
       returns the value in d with the key that occurs first in the
       alphabet. E.g., if d = {x = 11, b = 12}, get_min
returns 12."""
    return d[min(list(d.keys()))]


d = {}
letters = random.sample(string.ascii_letters, k=len(string.ascii_letters))
i = 1
for letter in letters:
    d[letter] = i
    i += 1

print(f'min letter value is: {get_min(d)}')