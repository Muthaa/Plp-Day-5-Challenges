import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Define Hogwarts houses and students (Dictionary[str, List[str]])
houses = {
    "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
    "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
    "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
    "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
}

# Assign colors to houses (Dictionary[str, str])
house_colors = {
    "Gryffindor": "red",
    "Slytherin": "green",
    "Hufflepuff": "yellow",
    "Ravenclaw": "blue"
}

# Add nodes with colors
node_colors = []
labels = {}  # Dictionary[str, str] for labeling nodes
for house, students in houses.items():
    for student in students:
        G.add_node(student, house=house)
        node_colors.append(house_colors[house])
        labels[student] = f"{student}\n({house[:3]})"  # Show student name + house initials

# Define friendships (List[Tuple[str, str]])
friendships = [
    # Intra-house friendships
    ("Harry", "Ron"), ("Harry", "Hermione"), ("Ron", "Hermione"), ("Neville", "Harry"),
    ("Draco", "Pansy"), ("Draco", "Blaise"), ("Pansy", "Blaise"), ("Draco", "Theodore"),
    ("Cedric", "Hannah"), ("Cedric", "Ernie"), ("Hannah", "Ernie"), ("Cedric", "Susan"),
    ("Luna", "Cho"), ("Luna", "Padma"), ("Cho", "Padma"), ("Luna", "Terry"),

    # Inter-house friendships
    ("Harry", "Cedric"), ("Harry", "Luna"), ("Draco", "Harry"),
    ("Hermione", "Luna"), ("Ron", "Ernie"), ("Neville", "Cho"),
    ("Blaise", "Padma"), ("Theodore", "Terry"), ("Pansy", "Hannah")
]

# Add edges
G.add_edges_from(friendships)

# Draw the graph with customizations
plt.figure(figsize=(9, 7))
pos = nx.circular_layout(G)  # Circular layout for clear house separation
nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, 
        node_size=2500, font_size=9, font_weight="bold", edge_color="gray", 
        width=1.5, alpha=0.8)

# Add title
plt.title("Hogwarts House Connections (Enhanced)", fontsize=14, fontweight="bold")
plt.show()
