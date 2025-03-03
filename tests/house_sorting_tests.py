import pytest
from unittest.mock import patch
from collections import Counter
from house_sorting import sort_into_house, house_traits

def test_sort_into_house_tie_breaker():
    student = {"name": "Test Student", "traits": ["brave", "loyal", "cunning"]}  # Could match Gryffindor, Slytherin, and Hufflepuff
    with patch('random.choice') as mocked_random_choice:
        mocked_random_choice.return_value = "Gryffindor"
        house = sort_into_house(student)
        assert house == "Gryffindor", f"Expected Gryffindor, but got {house}"

        mocked_random_choice.return_value = "Slytherin"
        house = sort_into_house(student)
        assert house == "Slytherin", f"Expected Slytherin, but got {house}"

def test_sort_into_house():
    student = {"name": "Alex", "traits": ["brave", "adventurous", "loyal"]}
    house = sort_into_house(student)
    assert house == "Gryffindor", f"Expected Gryffindor, but got {house}"

    student = {"name": "Zara", "traits": ["intelligent", "curious", "analytical"]}
    house = sort_into_house(student)
    assert house == "Ravenclaw", f"Expected Ravenclaw, but got {house}"

    student = {"name": "Leo", "traits": ["cunning", "ambitious", "leader"]}
    house = sort_into_house(student)
    assert house == "Slytherin", f"Expected Slytherin, but got {house}"

    student = {"name": "Mia", "traits": ["kind", "loyal", "patient"]}
    house = sort_into_house(student)
    assert house == "Hufflepuff", f"Expected Hufflepuff, but got {house}"

def test_most_common_trait():
    # Create a mock of all traits for each house
    all_traits = {
        "Gryffindor": ["brave", "adventurous", "brave", "bold", "bold"],
        "Slytherin": ["ambitious", "cunning", "leader", "cunning", "ambitious"],
        "Hufflepuff": ["loyal", "kind", "kind", "loyal"],
        "Ravenclaw": ["intelligent", "curious", "creative", "curious"]
    }
    expected_result = {
        "Gryffindor": "brave",
        "Slytherin": "ambitious",
        "Hufflepuff": "loyal",
        "Ravenclaw": "curious"
    }
    
    for house, traits in all_traits.items():
        most_common_trait = Counter(traits).most_common(1)[0][0]
        assert most_common_trait == expected_result[house], f"Expected {expected_result[house]} for {house}, but got {most_common_trait}"

def test_house_rivalries():
    # Manually define the expected rivalry score based on shared traits.
    house_similarity = {
        ("Gryffindor", "Slytherin"): 0,
        ("Gryffindor", "Hufflepuff"): 1,
        ("Gryffindor", "Ravenclaw"): 1,
        ("Slytherin", "Hufflepuff"): 0,
        ("Slytherin", "Ravenclaw"): 1,
        ("Hufflepuff", "Ravenclaw"): 0
    }

    # Simulate the shared traits calculation
    for (house1, house2), expected_similarity in house_similarity.items():
        shared_traits = len(house_traits[house1] & house_traits[house2])
        assert shared_traits == expected_similarity, f"Expected {house1} & {house2} to have {expected_similarity} shared traits, but got {shared_traits}"

def test_new_student_input():
    student_input = {"name": "Harry", "traits": ["brave", "loyal", "chivalrous"]}
    house = sort_into_house(student_input)
    assert house == "Gryffindor", f"Expected Gryffindor, but got {house}"

    # Simulate user entering a new student
    student_input = {"name": "Luna", "traits": ["wise", "intelligent", "curious"]}
    house = sort_into_house(student_input)
    assert house == "Ravenclaw", f"Expected Ravenclaw, but got {house}"

def test_final_house_assignments():
    sorted_students = {
        "Gryffindor": ["Alex", "Sophia"],
        "Slytherin": ["Leo", "Noah"],
        "Hufflepuff": ["Mia", "Oscar"],
        "Ravenclaw": ["Zara", "Ella"]
    }

    expected_output = """
🏰 **Final Hogwarts House Assignments:**
🔹 Gryffindor: Alex, Sophia
🔹 Slytherin: Leo, Noah
🔹 Hufflepuff: Mia, Oscar
🔹 Ravenclaw: Zara, Ella
    """

    output = "\n🏰 **Final Hogwarts House Assignments:**"
    for house, students in sorted_students.items():
        output += f"\n🔹 {house}: {', '.join(students)}" if students else f"\n🔹 {house}: No students assigned"
    
    assert output.strip() == expected_output.strip(), f"Expected: {expected_output}, but got: {output}"
