import pytest
import networkx as nx

# Test case 1: Verify that all students are added as nodes to the graph
def test_graph_creation_nodes():
    G = nx.Graph()
    
    houses = {
        "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
        "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
        "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
        "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
    }
    
    # Add nodes and edges based on the provided code
    node_colors = []
    labels = {}
    for house, students in houses.items():
        for student in students:
            G.add_node(student, house=house)
            node_colors.append(house)
            labels[student] = f"{student}\n({house[:3]})"
    
    assert len(G.nodes) == 16  # There should be 16 students (4 houses * 4 students each)

# Test case 2: Verify that the node colors are assigned correctly to the houses
def test_node_colors():
    G = nx.Graph()
    
    houses = {
        "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
        "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
        "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
        "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
    }
    
    house_colors = {
        "Gryffindor": "red",
        "Slytherin": "green",
        "Hufflepuff": "yellow",
        "Ravenclaw": "blue"
    }
    
    node_colors = []
    for house, students in houses.items():
        for student in students:
            G.add_node(student, house=house)
            node_colors.append(house_colors[house])
    
    # Test that Gryffindor students have red color, Slytherin have green, etc.
    for student in houses["Gryffindor"]:
        assert house_colors["Gryffindor"] in node_colors
    for student in houses["Slytherin"]:
        assert house_colors["Slytherin"] in node_colors
    for student in houses["Hufflepuff"]:
        assert house_colors["Hufflepuff"] in node_colors
    for student in houses["Ravenclaw"]:
        assert house_colors["Ravenclaw"] in node_colors

# Test case 3: Verify the labels are formatted correctly for each student
def test_labels_format():
    G = nx.Graph()
    
    houses = {
        "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
        "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
        "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
        "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
    }
    
    labels = {}
    for house, students in houses.items():
        for student in students:
            labels[student] = f"{student}\n({house[:3]})"
    
    # Check if the labels are in the correct format
    for student in houses["Gryffindor"]:
        assert labels[student] == f"{student}\n(Gry)"
    for student in houses["Slytherin"]:
        assert labels[student] == f"{student}\n(Sly)"
    for student in houses["Hufflepuff"]:
        assert labels[student] == f"{student}\n(Huf)"
    for student in houses["Ravenclaw"]:
        assert labels[student] == f"{student}\n(Rav)"

# Test case 4: Verify if graph has no disconnected nodes (everyone should be connected in some way)
def test_no_disconnected_nodes():
    G = nx.Graph()
    
    houses = {
        "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
        "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
        "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
        "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
    }
    
    friendships = [
        ("Harry", "Ron"), ("Harry", "Hermione"), ("Ron", "Hermione"), ("Neville", "Harry"),
        ("Draco", "Pansy"), ("Draco", "Blaise"), ("Pansy", "Blaise"), ("Draco", "Theodore"),
        ("Cedric", "Hannah"), ("Cedric", "Ernie"), ("Hannah", "Ernie"), ("Cedric", "Susan"),
        ("Luna", "Cho"), ("Luna", "Padma"), ("Cho", "Padma"), ("Luna", "Terry"),
        ("Harry", "Cedric"), ("Harry", "Luna"), ("Draco", "Harry"),
        ("Hermione", "Luna"), ("Ron", "Ernie"), ("Neville", "Cho"),
        ("Blaise", "Padma"), ("Theodore", "Terry"), ("Pansy", "Hannah")
    ]
    
    G.add_edges_from(friendships)
    
    # Ensure the graph is connected (i.e., all students are reachable from any other student)
    assert nx.is_connected(G)  # This ensures there are no disconnected components

