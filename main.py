from graphml_parser import GraphMLParser
from graph import Graph
from node import Node
import fnmatch

def main():

    from_prompt = int(input("Enter 0 to give information from file or 1 to use prompt"))

    if(not from_prompt):
        file_name = input("Enter the name of the input file: ")
        fname = input("Enter the GraphML file to save: ")
        G = main_using_networkx(file_name, fname)

    if(from_prompt):
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

        png_file_name = input("Enter the PNG file to save: ") 
        if(not fnmatch.fnmatch(png_file_name, '*.png') or png_file_name==''):
            png_file_name = 'graph.png'

        G = visualize_graph(g, png_file_name)

        fname = input("Enter the GraphML file to save: ") 
        if(not fnmatch.fnmatch(fname, '*.graphml') or fname==''):
            fname = 'graphml.graphml'

        flag = int(input("Enter 0 to generate graphml from networkx or 1 to use minidom"))

        if(flag):
            file_name = write_to_graphml(g, fname)
            view_graphml(fname)
        else:
            write_to_graphml_using_networkx(G,fname)
            view_graphml(fname)

def main_using_networkx(file_name, fname):
    G = create_graph_from_file(file_name)
    view_graph_from_networkx(G) 
    if(not fnmatch.fnmatch(fname, '*.graphml') or fname==''):
        fname = 'graphml.graphml'
    write_to_graphml_using_networkx(G,fname)
    return G

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

def visualize_graph(g: Graph, png_file_name: str):
    G = g.show(png_file_name)
    return G

def write_to_graphml(g: Graph, file_name: str) -> str:
    parser = GraphMLParser()
    parser.write(g, file_name)
    return file_name

def view_graphml(file_name: str):
    with open(file_name) as f:
        print(f.read())

def write_to_graphml_using_networkx(G,file_name: str):
    import networkx as nx

    nx.write_graphml(G, file_name)

def create_graph_from_file(file_name: str):
    import networkx as nx

    with open(file_name) as f:
        lines = f.readlines()

    edges_list = [line.strip().split() for line in lines]

    G = nx.Graph()
    G.add_edges_from(edges_list)

    print(G.nodes())

    print(G.edges())

    return G

def view_graph_from_networkx(G):
    import networkx as nx
    import matplotlib.pyplot as plt

    nx.draw(G)
    nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
    plt.show()

if __name__ == "__main__":
    main()
