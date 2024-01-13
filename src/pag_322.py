def print_path(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


class Node(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, source, destination):
        self.src = source
        self.dest = destination


class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, edge):
        self.edges[edge.src].append(edge.dest)

    def children_of(self, node):
        return self.edges[node]


# noinspection PyPep8Naming
def BFS(graph, start, end):
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)
        print('Current BSF path: ', print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None


def test_bfs():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for node in nodes:
        g.add_node(node)
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    bfs = BFS(g, nodes[0], nodes[5])
    print('Shortest BSF path', print_path(bfs))


test_bfs()
