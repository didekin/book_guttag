def compare_all(f, g, entrees):
    listout = []
    for entree in entrees:
        listout.append(f(entree) == g(entree))
    return listout

