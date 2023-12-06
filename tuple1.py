# Creating a tuple
my_tuple = (1, 'apple', True, 3.14)

# Accessing elements of a tuple
print("Elements of the tuple:")
for element in my_tuple:
    print(element)

# Accessing individual elements by index
print("\nAccessing individual elements:")
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])
print("Third element:", my_tuple[2])
print("Fourth element:", my_tuple[3])

# Trying to modify a tuple (This will raise an error as tuples are immutable)
# Uncommenting the below line will result in an error
# my_tuple[0] = 5

# Tuple unpacking
a, b, c, d = my_tuple
print("\nTuple unpacking:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
