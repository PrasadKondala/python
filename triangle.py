def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()  # Sort the sides

    # Check if it's a right triangle using the Pythagorean theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Accepting inputs for the sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Checking if it's a right triangle
if is_right_triangle(side1, side2, side3):
    print("It is a right triangle.")
else:
    print("It is not a right triangle.")
