import math

# Write the code ↓ to read the radius and height of a cylinder from the user.
# Be cautious when reading input of various data types.

print("CYLINDER VOLUME CALCULATOR FOR ALF\n")
while(True):
    try:
        r = float(input("Please, enter the radius of the cylinder: "))
        h = float(input("Please, enter the height of the cylinder: "))
        break
    except Exception:
        print("Invalid input. Please input float values only.\n")


# Write the code ↓ to calculate the volume of the cylinder using the formula V = πr^2h.
# Formula to calculate the volume (V) of a cylinder:
# V = π * r^2 * h

pi = math.pi
r = math.pow(r, 2)
volume = pi * r * h

# Write the code ↓ to display the calculated volume with 2 decimal places.

print("The volume of the cylinder is: %.2f" % volume)

# Select and employ a string concatenation method based on your personal preference and comfort level.





