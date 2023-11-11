import collections as co


def graph_dict(filename):
    graphdict = co.defaultdict(list)
    with open(filename, 'r', encoding="utf-8") as re:
        for line in re:
            node, longueur, suivante = line.split()
            graphdict[node].append((suivante, longueur))
    return dict(graphdict.items())


print(graph_dict('files/graph1.txt'))
