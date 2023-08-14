var = lambda x, y: x / y if y != 0 else x
print(var(3, 2))

s1 = 'bcadbjav'


def find_last(s, sub):
    """
    s and sub are non-empty strings
       Returns the index of the last occurrence of sub in s.
       Returns None if sub does not occur in s
   """
    val = s.rfind(sub)
    return None if val == 1 else val


print(find_last(s1, 'b'))
