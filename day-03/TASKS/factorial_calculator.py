# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.

print("FACTORIAL CALCULATOR FOR ALF\n")
while (True):
    num = int(input("Please, enter a non-negative integer: "))
    if(num < 0):
        print("Invalid input. Please enter a valid non-negative integer.\n")
    else:
        break


# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.
ans = int("1")

for i in range(1, num+1, 1):
    ans *= i

# Write the code ↓ to display the factorial result.

print("The factorial of", num, "is:", ans)

# Select and employ a string concatenation method based on your personal preference and comfort level.





