def read_set(filename):
    outset = set()
    with open(filename, 'r', encoding="utf-8") as re:
        for line in re:
            outset.add(line.strip())
    return outset


def search_in_set(filename_reference, filename):
    refset = read_set(filename_reference)
    listout = list()
    with open(filename, 'r', encoding="utf-8") as re:
        for line in re:
            linein = line.strip()
            listout.append((linein, linein in refset))
    return listout


print(search_in_set('files/file_set.txt', 'files/file_is_inset.txt'))
