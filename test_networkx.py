import unittest 
from main import create_graph_from_file
from main import view_graph_from_networkx
from main import write_to_graphml_using_networkx
from collections import Counter

class SimpleTest(unittest.TestCase): 

    def test_create_graph_from_file(self):
        g = create_graph_from_file("input.txt")
        nodes = []
        for node in g.nodes():
            nodes.append(node)
        c1 = Counter(['a', 'c', 'b', 'e', 'd'])
        c2 = Counter(nodes)
        assert c1==c2

        edges = []
        for edge in g.edges():
            edges.append(edge)
        c3 = Counter([('a', 'c'), ('a', 'b'), ('c', 'e'), ('b', 'd')])
        c4 = Counter(edges)
        assert c3==c4

        return g

    def test_write_to_graphml_using_networkx(self):
        import networkx as nx
        import os.path

        G =nx.karate_club_graph()
        view_graph_from_networkx(G)

        file_name = "output.graphml"
        G = write_to_graphml_using_networkx(G,file_name)
        assert os.path.isfile(file_name)

        return file_name


if __name__ == '__main__': 
    unittest.main() 