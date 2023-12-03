def numbers(*args):
    if len(args) == 0:
        return 0, 0, 0
    somme, minim, maxim = sum(args), min(args), max(args)
    return somme, minim, maxim


numbers()
