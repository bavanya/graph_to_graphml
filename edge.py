from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from node import Node
from item import Item

class Edge(Item):

    def __init__(self, node1: Node, node2: Node, directed: bool = False):
        super(Edge, self).__init__()

        self.node1 = node1
        self.node2 = node2

        self.node1._edges.append(self)
        self.node2._edges.append(self)

        self._directed = directed

    def node(self, node: Node):
        if node == self.node1:
            return self.node2
        elif node == self.node2:
            return self.node1
        else:
            return None

    def parent(self) -> Node:
        return self.node1

    def child(self) -> Node:
        return self.node2

    def directed(self):
        return self._directed

    def set_directed(self, dir):
        self._directed = dir

