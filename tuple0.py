# Creating a tuple
my_tuple = (1, 2, 3, 'hello', 'world')

# Accessing elements of a tuple
print("Tuple elements:", my_tuple)
print("First element:", my_tuple[0])
print("Third element:", my_tuple[2])
print("Last element:", my_tuple[-1])

# Iterating through a tuple
print("\nIterating through the tuple:")
for element in my_tuple:
    print(element)

# Tuple slicing
print("\nTuple slicing:")
print("Elements from index 1 to 3:", my_tuple[1:4])
print("Elements from index 2 to the end:", my_tuple[2:])
print("Elements from the beginning to index 3:", my_tuple[:4])

# Tuple length
print("\nLength of the tuple:", len(my_tuple))

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("\nConcatenated tuple:", concatenated_tuple)

# Nested tuples
nested_tuple = ((1, 2), ('a', 'b'), (True, False))
print("\nNested tuple:", nested_tuple)
