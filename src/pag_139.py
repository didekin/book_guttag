def get_min(d):
    """
    d a dict mapping letters to ints
    returns the value in d with the key that occurs first
    in the alphabet. E.g., if d = {x = 11, b = 12}, get_min
    returns 12.
    """
    return d[min(d.keys())]


dd = {'x': 11, 'b': 12, 'a': 23, 'c': 1, 'z': 2}
print(get_min(dd))
