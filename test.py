from pyvis.network import Network
import networkx as nx

G = nx.Graph()

# Define nodes with their levels
# The format is (node_name, level)
nodes_with_levels = [
    ('A', 1), ('B', 1),
    ('C', 2), ('D', 2),
    ('E', 3), ('F', 3), ('G', 3)
]

# Add nodes to the graph
for node, _ in nodes_with_levels:
    G.add_node(node)

# Define edges (for this example, just connecting nodes sequentially)
edges = [('A', 'C'), ('A', 'D'), ('B', 'D'),
         ('C', 'E'), ('D', 'F'), ('D', 'G')]
for edge in edges:
    G.add_edge(*edge)

nt = Network(notebook=True, width="800px", height="800px")
nt.from_nx(G)

# Calculate positions
level_spacing = 100
max_nodes_per_level = max([level for _, level in nodes_with_levels])
# Adjust as necessary based on canvas width
x_spacing = 700 / max_nodes_per_level

for idx, (node, level) in enumerate(nodes_with_levels):
    count_at_same_level = sum(
        1 for _, lvl in nodes_with_levels if lvl == level)
    first_x_at_level = (max_nodes_per_level -
                        count_at_same_level) / 2 * x_spacing

    nt.nodes[idx]['y'] = (level - 1) * level_spacing
    nt.nodes[idx]['x'] = first_x_at_level + \
        (sum(1 for _, lvl in nodes_with_levels if lvl ==
         level and nodes_with_levels.index((_, lvl)) < idx) * x_spacing)
    nt.nodes[idx]['fixed'] = {'x': True, 'y': True}

# Optionally, you might want to adjust the physics
nt.repulsion("""
var options = {
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -2000,
      "centralGravity": 0.3,
      "springLength": 95
    },
    "minVelocity": 0.75
  }
}
""")

nt.show('test.html')
