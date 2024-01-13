from operator import mul, add
from functools import reduce


def doubler_premier(myf, param1, *args):
    return reduce(myf, (param1 * 2, *args))


def doubler_premier_kwds(myf, pos, *args, **kwargs):
    listIn = [2 * pos, *args]
    listIn.extend(list(kwargs.values()))
    return reduce(myf, listIn)
