from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from node import Node
from edge import Edge

from collections import deque


class Graph:

    def __init__(self, name: str = ""):
        self.name = name

        self._nodes = []
        self._edges = []
        self._root = None
        self.directed = True

        self.i = 0

    def DFS_prefix(self, root: Node = None):

        if not root:
            root = self._root

        return self._DFS_prefix(root)

    def _DFS_prefix(self, n, parent = None):

        nodes = [n]
        n['depth'] = self.i

        for c in n.children():
            nodes += self._DFS_prefix(c, n)
            self.i += 1

        return nodes

    def BFS(self, root: Node = None) -> list:
        if not root:
            root = self.root()

        queue = deque()
        queue.append(root)

        nodes = []

        while len(queue) > 0:
            x = queue.popleft()
            nodes.append(x)

            for child in x.children():
                queue.append(child)

        return nodes

    def get_depth(self, node: Node) -> int:
        depth = 0
        while node.parent() and node != self.root():
            node = node.parent()[0]
            depth += 1

        return depth

    def nodes(self) -> list:
        return self._nodes

    def edges(self) -> list:
        return self._edges

    def children(self, node: Node):
        return node.children()

    def add_node(self, label: str = "", id=None) -> Node:
        n = Node(id)
        n['label'] = label
        self._nodes.append(n)

        return n

    def add_edge(self, n1: Node, n2: Node, directed: bool = False) -> Edge:
        e = Edge(n1, n2, directed)
        self._edges.append(e)

        return e

    def add_edge_by_id(self, id1, id2):
        try:
            n1 = next(n for n in self._nodes if n.id == id1)
        except StopIteration:
            raise ValueError('Graph has no node with ID {}'.format(id1))
        try:
            n2 = next(n for n in self._nodes if n.id == id2)
        except StopIteration:
            raise ValueError('Graph has no node with ID {}'.format(id2))
        return self.add_edge(n1, n2)

    def set_root(self, node: Node):
        self._root = node

    def root(self) -> Node:
        return self._root

    def get_attributs(self):
        attr = []
        attr_obj = []
        for n in self.nodes():
            for a in n.attr:
                if a not in attr:
                    attr.append(a)
                    attr_obj.append(n.attr[a])

        for e in self.edges():
            for a in e.attr:
                if a not in attr:
                    attr.append(a)
                    attr_obj.append(e.attr[a])

        return attr_obj


    def show(self, file_name, show_label: bool = False):
        import matplotlib

        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()

        for n in self._nodes:
            if show_label:
                n_label = n['label']
            else:
                n_label = n.id
            G.add_node(n_label)

        for e in self._edges:
            if show_label:
                n1_label = e.node1['label']
                n2_label = e.node2['label']
            else:
                n1_label = e.node1.id
                n2_label = e.node2.id
            G.add_edge(n1_label, n2_label)

        nx.draw(G)

        if show_label:
            nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
        plt.savefig(file_name, format="PNG")
        plt.show()

        return G
