from flask import Flask, render_template, send_file, flash, request
import matplotlib.pyplot as plt
from io import BytesIO
import networkx as nx
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from main import *
from graphml_parser import GraphMLParser
from graph import Graph
from node import Node
import fnmatch

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

graph_ml_file_name = 'graphml.graphml'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/complete_graph', methods=['POST'])
def complete_graph():
    nodes = [int(x) for x in request.form.values()]
    node = nodes[0]
    # Creating a networkx complete graph with nodes count as given in the url path.
    G = nx.complete_graph(node)
    nx.draw(G)
    # Saving the png file of the graph visualization to disk.
    plt.savefig('graph.png', format="PNG")

    # Saving the graphml of the created complete graph to graphml file.
    nx.write_graphml(G, graph_ml_file_name)

    img = BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.clf() # clear pyplot

    return send_file(img, mimetype='image/png')

@app.route('/graphml')
def graphml():
    # Opening the recent created complete graph's graphML.
	with open(graph_ml_file_name, 'r') as f: 
		return render_template('graphml.html', text=f.read()) 

@app.route('/file', methods=['POST'])
def file():
    f = request.files['file']
    f_name = str(f.filename)
    G = create_graph_from_file(f_name)
    write_to_graphml_using_networkx(G,'graphml.graphml')
    nx.draw(G)
    # Saving the png file of the graph visualization to disk.
    plt.savefig('graph.png', format="PNG")

    # Saving the graphml of the created complete graph to graphml file.
    nx.write_graphml(G, graph_ml_file_name)

    img = BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.clf() # clear pyplot

    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run()