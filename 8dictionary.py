# Creating a dictionary
my_dict = {
    'apple': 5,
    'banana': 7,
    'cherry': 3,
    'mango': 9,
    'grapes': 6,
    'orange': 4
}

# Accessing elements of a dictionary
print("Dictionary elements:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Accessing value by key
print("\nAccessing value by key:")
print("Number of bananas:", my_dict['banana'])
print("Number of mangoes:", my_dict['mango'])

# Adding a new key-value pair
my_dict['pineapple'] = 8
print("\nAfter adding pineapple:", my_dict)

# Modifying a value in the dictionary
my_dict['apple'] = 10
print("\nAfter modifying apple value:", my_dict)

# Removing an element from the dictionary
removed_value = my_dict.pop('cherry')
print("\nRemoved cherry from dictionary:", removed_value)
print("Dictionary after removing cherry:", my_dict)

# Checking if a key exists in the dictionary
key_to_check = 'orange'
if key_to_check in my_dict:
    print(f"\n'{key_to_check}' exists in the dictionary.")
else:
    print(f"\n'{key_to_check}' does not exist in the dictionary.")

# Finding the length of the dictionary
print("\nLength of the dictionary:", len(my_dict))

# Getting all keys and values separately
print("\nAll keys in the dictionary:", my_dict.keys())
print("All values in the dictionary:", my_dict.values())

# Clearing the entire dictionary
my_dict.clear()
print("\nDictionary after clearing all elements:", my_dict)
