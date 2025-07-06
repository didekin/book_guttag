import example_14_2 as di


class WeightedDigraph(object):

    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to a list of its children
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = {}

    def add_edge(self, w_edge):
        src = w_edge.get_source()
        dest = w_edge.get_destination()
        weigth = w_edge.get_weight()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src][dest] = weigth

    def children_of(self, node):
        return self._edges[node].keys()

    def has_node(self, node):
        return node in self._nodes

    def get_nodes(self):
        return self._nodes

    def weightPath(self, path):
        if path is None:
            return float('inf')
        weight = 0
        for i in range(0, len(path) - 1):
            edge_weigth = self._edges[path[i]][path[i + 1]]
            weight += edge_weigth
        return weight


def WeightedDFS(graph, start, end, path, shortest, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes;
       path and shortest are lists of nodes
       Returns the shortest path from start to end in graph"""
    path = path + [start]
    weigth_path = graph.weightPath(path)
    weigth_shortest = graph.weightPath(shortest)
    if to_print:
        print('Current DFS path:', di.print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:  # avoid cycles
            if weigth_path < weigth_shortest:
                new_path = WeightedDFS(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path if graph.weightPath(new_path) < weigth_shortest else shortest
    return shortest


def shortest_DFSwpath(graph, start, end, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns the shortest path from start to end in graph"""
    return WeightedDFS(graph, start, end, [], None, to_print)


def shortest_BFS(graph, start, end, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns the shortest path from start to end in graph"""
    return di.BFS(graph, start, end, to_print)


def init_weight_testgraph():
    nodes = []
    for name in range(5):  # Create 6 nodes
        nodes.append(di.Node(str(name)))
    g = WeightedDigraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(di.WeightedEdge(nodes[0], nodes[1], 10))
    g.add_edge(di.WeightedEdge(nodes[0], nodes[2], 20))
    g.add_edge(di.WeightedEdge(nodes[0], nodes[3], 30))
    g.add_edge(di.WeightedEdge(nodes[2], nodes[4], 21))
    g.add_edge(di.WeightedEdge(nodes[3], nodes[4], 12))
    return g


def init_testgraph():
    nodes = []
    for name in range(3):  # Create 6 nodes
        nodes.append(di.Node(str(name)))
    g = di.Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(di.Edge(nodes[0], nodes[1]))
    g.add_edge(di.Edge(nodes[0], nodes[2]))
    g.add_edge(di.Edge(nodes[1], nodes[2]))
    return g, nodes


def test_WeightedDFS_SP():
    g = init_weight_testgraph()
    sp = shortest_DFSwpath(g, g.get_nodes()[0], g.get_nodes()[4], to_print=True)
    return sp


def test_BFS_SP():
    g, nodes = init_testgraph()
    sp = shortest_BFS(g, nodes[0], nodes[2], to_print=True)
    return sp


print(di.print_path(test_BFS_SP()))
