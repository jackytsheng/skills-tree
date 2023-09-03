from pyvis import network as net
import networkx as nx

# Create Graph
G = nx.DiGraph()

# Same nodes and edges as the previous example
nodes = [
    'Tries',
    'Linked List',
    'Math',
    'Geometry',
    'Two Pointers',
    '1-D DP',
    'Sliding Window',
    'Bit Manipulation',
    'Stack',
    'Queue',
    'Greedy',
    'Arrays',
    'Hashing',
    '2-D DP',
    'Advanced Graphs',
    'Graphs',
    'Intervals',
    'Backtracking',
    'Heap',
    'Priority Queue',
    'Binary Search',
    'Trees']
G.add_nodes_from(nodes)
edges = [
    ('Arrays', 'Stack'),
    ('Arrays', 'Queue'),
    ('Arrays', 'Two Pointers'),
    ('Hashing', 'Stack'),
    ('Hashing', 'Queue'),
    ('Hashing', 'Two Pointers'),
    ('Two Pointers', 'Binary Search'),
    ('Two Pointers', 'Sliding Window'),
    ('Two Pointers', 'Linked List'),
    ('Linked List', 'Trees'),
    ('Binary Search', 'Trees'),
    ('Trees', 'Tries'),
    ('Trees', 'Heap'),
    ('Trees', 'Backtracking'),
    ('Trees', 'Priority Queue'),
    ('Heap', 'Intervals'),
    ('Heap', 'Advanced Graphs'),
    ('Heap', 'Greedy'),
    ('Priority Queue', 'Intervals'),
    ('Priority Queue', 'Advanced Graphs'),
    ('Priority Queue', 'Greedy'),
    ('Backtracking', 'Graphs'),
    ('Backtracking', '1-D DP'),
    ('Graphs', '2-D DP'),
    ('Graphs', 'Advanced Graphs'),
    ('Graphs', 'Math'),
    ('Graphs', 'Geometry'),
    ('1-D DP', '2-D DP'),
    ('Bit Manipulation', 'Math'),
    ('Bit Manipulation', 'Geometry'),
]
G.add_edges_from(edges)

nt = net.Network("400px", notebook=True, directed=True,
                 neighborhood_highlight=True, filter_menu=True, select_menu=True)
nt.from_nx(G)
nt.force_atlas_2based()
file_name = 'algorithm.html'
# nt.show_buttons()
nt.show(file_name)
print("Successfully Generated HTML File {}".format(file_name))
