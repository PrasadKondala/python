def findname(name, phonebook):
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name}'s phone number from the phonebook.")
    else:
        print(f"{name} not found in the phonebook.")
# Example phonebook dictionary
phonebook = {
    "prasad": "9878676541",
    "rajesh": "987654676",
    "bharath": "630121212"
}

# Call the function to delete a phone number based on the name
name_to_delete = "bharath"
findname(name_to_delete, phonebook)

print("Updated phonebook:", phonebook)
