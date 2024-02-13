# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.

print("PERFECT NUMBER DENOMINATOR FOR ALF\n")
while (True):
    num = int(input("Please, enter a positive integer: "))
    if(num < 0):
        print("Invalid input. Please input a valid positive integer")
    else:
        break


# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.
ans = 0
for i in range(1, num, 1):
    if(num%i == 0):
        ans += i


# Write the code ↓ to display the Perfect Number check result.

if (num == ans):
    print(num, "is a Perfect Number.")
else:
    print(num, "is not a Perfect Number.")

# NOTE : You can use if-else statement or ternary operator to display the result.






