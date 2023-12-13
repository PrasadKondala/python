# Creating two sets
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# Printing the sets
print("Set A:", set_a)
print("Set B:", set_b)

# Performing set operations
# Union of sets
union_set = set_a.union(set_b)
print("\nUnion of sets A and B:", union_set)

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print("Intersection of sets A and B:", intersection_set)

# Difference between sets
difference_set = set_a.difference(set_b)
print("Difference between set A and set B:", difference_set)

# Checking for subset
is_subset = set_a.issubset(set_b)
print("Is set A a subset of set B?", is_subset)
