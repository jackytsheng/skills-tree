# IMPORTS
from IPython.display import HTML
from pyvis import network as net
import networkx as nx


def display_pyvis(pyvis_graph, name):
    filename = f"{name}.html"
    pyvis_graph.save_graph(filename)
    return HTML(filename=filename)


g = net.Network(notebook=True, cdn_resources='in_line')
nxg = nx.complete_graph(5)
g.from_nx(nxg)

display_pyvis(g, "pyvis-example")
