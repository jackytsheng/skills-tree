from pyvis.network import Network
import networkx as nx

G = nx.Graph()
G.add_node(1, label="Click me!")
G.add_node(2, label="Another node")
G.add_edge(1, 2)

nt = Network(notebook=True)
nt.from_nx(G)

# JavaScript to handle the click event on node with id 1
js_code = """
function openNewNetwork(){
    var new_nodes = [
        {id: 3, label: 'New Node 1'},
        {id: 4, label: 'New Node 2'}
    ];
    var new_edges = [
        {from: 3, to: 4}
    ];
    // Clear the old nodes and edges
    this.body.data.nodes.clear();
    this.body.data.edges.clear();
    // Add the new nodes and edges
    this.body.data.nodes.add(new_nodes);
    this.body.data.edges.add(new_edges);
    // Stabilize the network again after changing data
    this.stabilize();
}

network.on("click", function(params) {
    if (params.nodes.includes(1)) {
        openNewNetwork.call(this);
    }
});
"""

nt.show_buttons(filter_=["physics"])
# add a hidden node to be shown later
nt.add_node(3, label="Node 3", hidden=True)
nt.add_edge(1, 3, hidden=True)  # add a hidden edge to be shown later
nt.add_edge(2, 3, hidden=True)  # add another hidden edge
nt.add_edge(3, 3, hidden=True)  # and yet another hidden edge

nt.write_html("network.html", notebook=True)

with open("network.html", "a") as f:
    f.write("<script>{}</script>".format(js_code))
