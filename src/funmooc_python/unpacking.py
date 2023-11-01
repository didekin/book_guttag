def surgery(liste):
    if len(liste) <= 1:
        return liste
    elif len(liste) % 2 == 0:
        a, b, *_ = liste
        liste[0:2] = b, a
        return liste
    else:
        *_, b, c = liste
        liste[-2:] = c, b
        return liste


print(surgery([1, 2, 3, 4]))
print(surgery([1, 2, 3, 4, 5]))
