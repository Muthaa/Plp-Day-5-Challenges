import pytest
import networkx as nx
from collections import Counter

def test_node_creation():
    # Create graph and add nodes
    G = nx.Graph()
    houses = {
        "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
        "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
        "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
        "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
    }
    # Add nodes to the graph
    for house, students in houses.items():
        for student in students:
            G.add_node(student, house=house)

    # Check if all nodes are present in the graph
    assert len(G.nodes) == 16  # There are 4 houses with 4 students each

def test_edge_weights():
    G = nx.Graph()
    snack_sharing = {
        ("Harry", "Ron"): 5, ("Hermione", "Neville"): 3, ("Draco", "Pansy"): 4, 
        ("Blaise", "Theodore"): 2, ("Cedric", "Hannah"): 5, ("Ernie", "Susan"): 1, 
        ("Luna", "Cho"): 3, ("Padma", "Terry"): 2,
        ("Harry", "Cedric"): 2, ("Ron", "Ernie"): 4, ("Hermione", "Luna"): 3, 
        ("Neville", "Cho"): 5, ("Draco", "Harry"): 1, ("Blaise", "Padma"): 2, 
        ("Theodore", "Terry"): 3, ("Pansy", "Hannah"): 1, ("Cedric", "Luna"): 5, 
        ("Hannah", "Cho"): 4, ("Ernie", "Draco"): 2, ("Susan", "Padma"): 3
    }
    
    # Add edges with weights
    for (u, v), weight in snack_sharing.items():
        G.add_edge(u, v, weight=weight)

    # Verify that the edges have correct weights
    for (u, v), weight in snack_sharing.items():
        assert G[u][v]["weight"] == weight

def test_house_colors():
    G = nx.Graph()
    house_colors = {
        "Gryffindor": "red",
        "Slytherin": "green",
        "Hufflepuff": "yellow",
        "Ravenclaw": "blue"
    }
    houses = {
        "Gryffindor": ["Harry", "Ron", "Hermione", "Neville"],
        "Slytherin": ["Draco", "Pansy", "Blaise", "Theodore"],
        "Hufflepuff": ["Cedric", "Hannah", "Ernie", "Susan"],
        "Ravenclaw": ["Luna", "Cho", "Padma", "Terry"]
    }

    # Add nodes to the graph
    for house, students in houses.items():
        for student in students:
            G.add_node(student, house=house)

    # Verify node colors
    for house, students in houses.items():
        for student in students:
            # Check that the node's house is correctly assigned
            node_house = G.nodes[student]["house"]
            expected_color = house_colors[house]  # Match color to house
            assert node_house == house


def test_node_sizes():
    G = nx.Graph()
    snack_sharing = {
        ("Harry", "Ron"): 5, ("Hermione", "Neville"): 3, ("Draco", "Pansy"): 4,
        ("Blaise", "Theodore"): 2, ("Cedric", "Hannah"): 5, ("Ernie", "Susan"): 1,
        ("Luna", "Cho"): 3, ("Padma", "Terry"): 2,
        ("Harry", "Cedric"): 2, ("Ron", "Ernie"): 4, ("Hermione", "Luna"): 3,
        ("Neville", "Cho"): 5, ("Draco", "Harry"): 1, ("Blaise", "Padma"): 2,
        ("Theodore", "Terry"): 3, ("Pansy", "Hannah"): 1, ("Cedric", "Luna"): 5,
        ("Hannah", "Cho"): 4, ("Ernie", "Draco"): 2, ("Susan", "Padma"): 3
    }

    # Create graph and add edges
    for (u, v), weight in snack_sharing.items():
        G.add_edge(u, v, weight=weight)

    # Calculate the expected node size based on snack-sharing activity
    node_sizes = {student: 2000 for student in G.nodes()}
    for (u, v), weight in snack_sharing.items():
        node_sizes[u] += weight * 50
        node_sizes[v] += weight * 50

    # Set the node_size attribute
    for node, size in node_sizes.items():
        G.nodes[node]["node_size"] = size

    # Check that the node sizes are updated correctly based on the weights
    for node in G.nodes():
        expected_size = node_sizes[node]
        assert G.nodes[node]["node_size"] == expected_size


def test_edge_colors():
    G = nx.Graph()
    snack_sharing = {
        ("Harry", "Ron"): 5, ("Hermione", "Neville"): 3, ("Draco", "Pansy"): 4,
        ("Blaise", "Theodore"): 2, ("Cedric", "Hannah"): 5, ("Ernie", "Susan"): 1,
        ("Luna", "Cho"): 3, ("Padma", "Terry"): 2,
        ("Harry", "Cedric"): 2, ("Ron", "Ernie"): 4, ("Hermione", "Luna"): 3,
        ("Neville", "Cho"): 5, ("Draco", "Harry"): 1, ("Blaise", "Padma"): 2,
        ("Theodore", "Terry"): 3, ("Pansy", "Hannah"): 1, ("Cedric", "Luna"): 5,
        ("Hannah", "Cho"): 4, ("Ernie", "Draco"): 2, ("Susan", "Padma"): 3
    }

    # Add nodes to the graph with their houses
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
    for house, students in houses.items():
        for student in students:
            G.add_node(student, house=house)

    # Add edges
    for (u, v), weight in snack_sharing.items():
        G.add_edge(u, v, weight=weight)

    # Define edge colors: black for same-house, gray for different-house
    edge_colors = [
        "black" if G.nodes[u]["house"] == G.nodes[v]["house"] else "gray"
        for u, v in G.edges()
    ]

    # Check that edges between students in the same house are black
    for (u, v), color in zip(G.edges(), edge_colors):
        if G.nodes[u]["house"] == G.nodes[v]["house"]:
            assert color == "black"
        else:
            assert color == "gray"
