import random
from collections import Counter

# House trait definitions
house_traits = {
    "Gryffindor": {"brave", "adventurous", "chivalrous", "bold", "daring"},
    "Slytherin": {"ambitious", "cunning", "resourceful", "strategic", "leader", "independent"},
    "Hufflepuff": {"loyal", "kind", "hardworking", "patient", "friendly"},
    "Ravenclaw": {"intelligent", "creative", "curious", "wise", "analytical", "philosophical"}
}

# Sorting Hat messages
sorting_messages = {
    "Gryffindor": "Ah, a heart full of courage! You belong in **Gryffindor!** 🦁",
    "Slytherin": "A sharp mind and a thirst to prove yourself... **Slytherin!** 🐍",
    "Hufflepuff": "A kind soul, loyal and hardworking. Welcome to **Hufflepuff!** 🦡",
    "Ravenclaw": "A brilliant mind with endless curiosity. You are a **Ravenclaw!** 🦅"
}

def sort_into_house(student):
    """Sorts a student into a Hogwarts house based on their traits."""
    scores = {house: len(set(student["traits"]) & traits) for house, traits in house_traits.items()}
    
    # Find the house(s) with the highest score
    max_score = max(scores.values())
    best_matches = [house for house, score in scores.items() if score == max_score]

    # If there's a tie, choose randomly
    chosen_house = random.choice(best_matches)

    # Sorting Hat speaks!
    print(f"\n🎩 Sorting Hat: {student['name']}...")
    print(f"🎩 Sorting Hat: {sorting_messages[chosen_house]}")
    
    return chosen_house

# Store sorted students
sorted_students = {house: [] for house in house_traits.keys()}
all_traits = {house: [] for house in house_traits.keys()}  # Store all traits for stats

# Existing students
new_students = [
    {"name": "Alex", "traits": ["brave", "adventurous", "loyal"]},
    {"name": "Zara", "traits": ["intelligent", "curious", "analytical"]},
    {"name": "Leo", "traits": ["cunning", "ambitious", "leader"]},
    {"name": "Mia", "traits": ["kind", "loyal", "patient"]},
    {"name": "Felix", "traits": ["resourceful", "strategic", "bold"]},
    {"name": "Ella", "traits": ["creative", "wise", "philosophical"]},
    {"name": "Oscar", "traits": ["hardworking", "loyal", "friendly"]},
    {"name": "Sophia", "traits": ["bold", "chivalrous", "brave"]},
    {"name": "Noah", "traits": ["strategic", "cunning", "independent"]},
    {"name": "Luna", "traits": ["wise", "philosophical", "intelligent"]}
]

# Sort existing students
for student in new_students:
    house = sort_into_house(student)
    sorted_students[house].append(student["name"])
    all_traits[house].extend(student["traits"])

# 📝 User Input for Custom Sorting
while True:
    add_custom = input("\nDo you want to enter a new student? (yes/no): ").strip().lower()
    if add_custom != "yes":
        break

    name = input("Enter student name: ").strip()
    traits = input("Enter personality traits (comma-separated): ").strip().lower().split(",")
    traits = [t.strip() for t in traits]

    student = {"name": name, "traits": traits}
    house = sort_into_house(student)
    sorted_students[house].append(name)
    all_traits[house].extend(traits)

# 📊 Most Common Trait Per House
print("\n📊 **Most Common Traits Per House:**")
for house, traits in all_traits.items():
    if traits:
        most_common_trait = Counter(traits).most_common(1)[0][0]
        print(f"🔹 {house}: {most_common_trait}")

# 💬 House Rivalries (Trait Similarities)
print("\n💬 **House Rivalries (Most Similar Houses):**")
house_similarity = {}
house_list = list(house_traits.keys())

for i in range(len(house_list)):
    for j in range(i + 1, len(house_list)):
        house1, house2 = house_list[i], house_list[j]
        shared_traits = len(house_traits[house1] & house_traits[house2])
        house_similarity[(house1, house2)] = shared_traits

# Sort by most similar houses
sorted_similarities = sorted(house_similarity.items(), key=lambda x: x[1], reverse=True)

for (house1, house2), similarity in sorted_similarities:
    print(f"🔗 {house1} & {house2}: {similarity} shared traits")

# 🏰 Final Hogwarts House List
print("\n🏰 **Final Hogwarts House Assignments:**")
for house, students in sorted_students.items():
    print(f"🔹 {house}: {', '.join(students) if students else 'No students assigned'}")
