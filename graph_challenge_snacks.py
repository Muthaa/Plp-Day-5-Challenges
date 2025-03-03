import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Define Hogwarts houses and students
houses = {
    "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
    "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
    "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
    "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
}

# Assign colors to houses
house_colors = {
    "Gryffindor": "red",
    "Slytherin": "green",
    "Hufflepuff": "yellow",
    "Ravenclaw": "blue"
}

# Define snack-sharing relationships with weights
snack_sharing = {
    ("Harry", "Ron"): 5, ("Hermione", "Neville"): 3, ("Draco", "Pansy"): 4, ("Blaise", "Theodore"): 2,
    ("Cedric", "Hannah"): 5, ("Ernie", "Susan"): 1, ("Luna", "Cho"): 3, ("Padma", "Terry"): 2,

    # Inter-house snack sharing
    ("Harry", "Cedric"): 2, ("Ron", "Ernie"): 4, ("Hermione", "Luna"): 3, ("Neville", "Cho"): 5,
    ("Draco", "Harry"): 1, ("Blaise", "Padma"): 2, ("Theodore", "Terry"): 3, ("Pansy", "Hannah"): 1,
    ("Cedric", "Luna"): 5, ("Hannah", "Cho"): 4, ("Ernie", "Draco"): 2, ("Susan", "Padma"): 3
}

# Add nodes and assign colors
node_colors = []
labels = {}
node_sizes = {}  # To scale node sizes based on popularity
for house, students in houses.items():
    for student in students:
        G.add_node(student, house=house)
        node_colors.append(house_colors[house])
        labels[student] = f"{student} 🍪"
        node_sizes[student] = 2000  # Default node size

# Add weighted edges & calculate popularity
for (u, v), weight in snack_sharing.items():
    G.add_edge(u, v, weight=weight)
    node_sizes[u] += weight * 50  # Increase node size based on activity
    node_sizes[v] += weight * 50  # Both sharers get the size boost

# Extract edge weights
edge_weights = [G[u][v]["weight"] for u, v in G.edges()]
max_weight = max(edge_weights)  # Get the highest weight

# Define edge colors and thickness based on weight
edge_colors = [
    "black" if G.nodes[u]["house"] == G.nodes[v]["house"] else "gray"
    for u, v in G.edges()
]
edge_thickness = [((w / max_weight) * 5) for w in edge_weights]  # Scale thickness

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Force-directed layout

# Draw edges with varying thickness
nx.draw_networkx_edges(G, pos, width=edge_thickness, edge_color=edge_colors, alpha=0.8)

# Draw nodes with varying sizes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=[node_sizes[n] for n in G.nodes()], edgecolors="black")

# Draw labels
nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, font_weight="bold")

# Add title
plt.title("Hogwarts Snack-Sharing Network (Weighted) 🍫🍪", fontsize=14, fontweight="bold")
plt.show()
