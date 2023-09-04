from pyvis.network import Network
import networkx as nx
import math

G = nx.Graph()

# Define nodes with their levels
# Format: (node_name, level)
nodes_with_levels = [
    ('A', 1),
    ('B', 2), ('C', 2),
    ('D', 3), ('E', 3), ('F', 3), ('G', 3),
    ('H', 4), ('I', 4), ('J', 4), ('K', 4), ('L', 4)
]

# Add nodes to the graph
for node, _ in nodes_with_levels:
    G.add_node(node)

# Define edges (for this example, connecting nodes in a tree structure)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'),
         ('C', 'G'), ('D', 'H'), ('E', 'I'), ('F', 'J'), ('G', 'K'), ('G', 'L')]
for edge in edges:
    G.add_edge(*edge)

nt = Network(notebook=True, width="800px", height="800px")
nt.from_nx(G)

# Calculate positions
radius_increment = 100

for idx, (node, level) in enumerate(nodes_with_levels):
    count_at_same_level = sum(
        1 for _, lvl in nodes_with_levels if lvl == level)
    angle_increment = 2 * math.pi / count_at_same_level
    angle = angle_increment * sum(1 for _, lvl in nodes_with_levels if lvl ==
                                  level and nodes_with_levels.index((_, lvl)) < idx)

    radius = level * radius_increment

    nt.nodes[idx]['x'] = radius * math.cos(angle)
    nt.nodes[idx]['y'] = radius * math.sin(angle)
    nt.nodes[idx]['fixed'] = {'x': True, 'y': True}

# Optionally, adjust physics to ensure nodes are stationary
nt.set_options("""
var options = {
  "physics": {
    "enabled": false
  }
}
""")

nt.show('test.html')
