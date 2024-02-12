# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.

print("SIMPLE CALCULATOR FOR ALF\n")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")



# Write the code ↓ to perform the calculations based on the selected operation.

if(operator == "+"):
    ans = num1 + num2
elif(operator == "-"):
    ans = num1 - num2
elif(operator == "x"):
    ans = num1 * num2
elif(operator == "/"):
    ans = num1/num2
else:
    ans = 'invalid'
    print("Invalid operator. Choose only between +, -, x, /")

 
# Write the code ↓ to display the result.

print("\nThe result of", num1, operator, num2, "is", ans)

# Select and employ a string concatenation method based on your personal preference and comfort level.







