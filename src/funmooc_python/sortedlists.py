def multi_tri(listes):
    for l in listes:
        l.sort()
    return listes


def multi_tri_reverse(listes, reverses):
    for i in range(0, len(listes)):
        listes[i].sort(reverse=reverses[i])
    return listes


def tri_custom(liste):
    return sorted(liste, key=lambda d: (d.get('p'), d.get('n'), d.get('p2', '')))

