from graphml_parser import GraphMLParser
from graph import Graph
from node import Node
import fnmatch

def main():
    g = Graph()

    number_of_nodes = int(input("Enter the number of nodes in graph: "))

    names_of_nodes = []
    for i in range(number_of_nodes):
        names_of_nodes.append(input("Enter the name of the node: "))

    nodes = []
    for i in range(number_of_nodes):
        nodes.append(g.add_node(names_of_nodes[i]))
    print(len(nodes))

    #n1 = g.add_node("A")
    #n2 = g.add_node("B")
    #n3 = g.add_node("C")
    #n4 = g.add_node("D")
    #n5 = g.add_node("E")
    
    number_of_edges= int(input("Enter the number of edges in graph: "))
    for i in range(number_of_edges):
        edge_nodes_indices = input('Enter indices of nodes of an edge separated by ":" ').split(':')
        g.add_edge(nodes[int(edge_nodes_indices[0])], nodes[int(edge_nodes_indices[1])])
    
    #g.add_edge(n1, n3)
    #g.add_edge(n2, n3)
    #g.add_edge(n3, n4)
    #g.add_edge(n3, n5)
    
    root_node_index = int(input("Enter the index of root node in nodes: "))
    set_root(g, nodes[root_node_index])

    get_breadth_first_search(g)
    get_depth_first_search(g)

    visualize_graph(g)

    fname = input("Enter the GraphML file to save: ") 
    if(not fnmatch.fnmatch(fname, '*.graphml') or fname==''):
        fname = 'graphml.graphml'
    file_name = write_to_graphml(g, fname)

    view_graphml(file_name)


def set_root(g: Graph, n1: Node) -> Graph:
    g.set_root(n1)
    return g

def get_breadth_first_search(g: Graph):
    nodes = g.BFS()
    for node in nodes:
        print(node)

def get_depth_first_search(g: Graph):
    nodes = g.DFS_prefix()
    for node in nodes:
        print(node)   

def visualize_graph(g: Graph):
    g.show()

def write_to_graphml(g: Graph, file_name: str) -> str:
    parser = GraphMLParser()
    parser.write(g, file_name)
    return file_name

def view_graphml(file_name: str):
    with open(file_name) as f:
        print(f.read())


if __name__ == "__main__":
    main()
