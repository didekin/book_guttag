def mean_tuple(tuplein):
    """
    :param tuplein: a tuple of real numbers.
    :return: arithmetic mean
    """
    return sum(tuplein) / len(tuplein)


print(f'meantuple = {mean_tuple((1, 3, 5, 7, 9))}')
