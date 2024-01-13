def aplatir(conteneurs):
    return [c[i] for c in conteneurs for i in range(len(c))]


def alternat(c1, c2):
    return [c[i] for c in zip(c1, c2) for i in range(2)]


def intersect(A, B):
    return {c[1] for c in A | B if c[0] in {e[0] for e in A} & {e[0] for e in B}}
