#write a progra to demonstrate  working with tuplein python
T = ("apple", "banana", "cherry", "mango", "grapes", "orange")
print("\nCreated tuple is:", T)
print("\nSecond fruit is:", T[1])
print("\nFrom 3-6 fruits are:", T[3:6])
print("\nList of all items in Tuple is:")
for x in T:
    print(x)
    if "apple" in T:
        print("\nYes, 'apple' is in the fruits tuple")
print("\nLength of Tuple is:", len(T))
