import ipywidgets as widgets
from IPython.display import display, HTML, Javascript
from pyvis import network as net
import networkx as nx

# Create Graph
G = nx.DiGraph()

# Same nodes and edges as the previous example
nodes = [
    'Programming Basics', 'Variables & Data Types', 'Control Structures', 'Functions',
    'OOP', 'Classes & Objects', 'Inheritance', 'Polymorphism',
    'Data Structures', 'Lists/Arrays', 'Trees', 'Graphs',
    'Web Development', 'HTML/CSS', 'JavaScript', 'Backend Frameworks',
    'Database Management', 'SQL Basics', 'Database Design', 'ORM'
]
G.add_nodes_from(nodes)
edges = [
    ('Programming Basics', 'Variables & Data Types'),
    ('Programming Basics', 'Control Structures'),
    ('Programming Basics', 'Functions'),
    ('OOP', 'Classes & Objects'),
    ('OOP', 'Inheritance'),
    ('OOP', 'Polymorphism'),
    ('Data Structures', 'Lists/Arrays'),
    ('Data Structures', 'Trees'),
    ('Data Structures', 'Graphs'),
    ('Web Development', 'HTML/CSS'),
    ('Web Development', 'JavaScript'),
    ('Web Development', 'Backend Frameworks'),
    ('Database Management', 'SQL Basics'),
    ('Database Management', 'Database Design'),
    ('Database Management', 'ORM')
]
G.add_edges_from(edges)

nt = net.Network(notebook=True, directed=True)
nt.from_nx(G)
nt.force_atlas_2based()

# Create a button to toggle the sidebar
toggle_button = widgets.Button(description="Toggle Options")
out = widgets.Output(layout={'border': '1px solid black'})

def toggle_options(button):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1, IPython.notebook.get_selected_index()+2)'))

toggle_button.on_click(toggle_options)

# Render the button
display(toggle_button)
display(out)

# Render the graph (this cell will be executed by the button to toggle the display)
with out:
    nt.show("skill_tree.html")
