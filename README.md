# **graph_to_graphml**

## **Topic**: 
### Implement a tool to generate XML document from a graph / business workflow.


### **The keywords relevant to the topic are:**

1. **Graph database:** It is a type of NOSQL database. Information is stored in
nodes and edges. The edges represent the relationship between the nodes.
Neo4j is a graph database.

2. **XML document:** It is a markup language which is both human and machine
readable. Certain set of rules are to be followed for encoding documents in
this language. Different file formats are developed based on XML like
GRAPHML, GXL, XGMML etc. XGMML and GRAPHML are formats
specifically developed for graphs based on XML.

### **The steps to be performed by the application are:**
1. Data should be imported from the graph.
2. The following information must be extracted from the graph.
    1. Nodes
    1. Edges and Weights
    1. Any other information about the connection between nodes.
3. XML encoding should be generated following the well defined set of rules of
XML format.
4. The generated encoding should be saved to disk in a file with .xml extension
in the requested directory.

### **After literature review, the approach to develop an application on this topic is:**
1. The graph data can be taken either from neo4j or networkx to generate the XML file.
    1. **Neo4j:** It is a graph database which also provides native java API to access the database content using java.
    1. **networkx:** It is a Python library for storing and studying graphs and
networks.

2. If Neo4j is taken for the graph data, the application can be written in java. The reasons for choosing java are as follows:
    1. Spring framework which can be used by any java application has support for neo4j for storing and extracting data. With this, the content of a database can be accessed to generate an XML file.
    1. The DOM parser in java supports creating an XML file effortlessly.
3. If networkx is taken for graph data, the application can be written in python
as networkx is a library developed in python. Then the content in networkx
data can be extracted and stored in graphML which is based on XML.

### **Started the project work in python because of the following reasons:**
1. python has additional graph visualization packages like networkx and
matplotlib.
2. It is possible to integrate neo4j with python projects using the official drivers provided by neo4j.
