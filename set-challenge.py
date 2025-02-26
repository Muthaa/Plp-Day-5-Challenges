# Define two sets with words
Gamers = {"Mike", "Joe", "Peter", "Lue", "Ann", "Ced", "Chleo"}
BookHeads = {"Chleo", "Sue", "Ben", "Hoser", "Anna", "Joe"}

set1 = Gamers
set2 = BookHeads

# Find common names using intersection
#common_names = set1.intersection(set2)

# Alternatively, you can use the & operator to find common elements
common_names = set1 & set2

# Print the common names 
print("Best of both worlds:", common_names)
