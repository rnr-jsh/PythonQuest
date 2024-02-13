# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.

print("PALINDROME CHECKER FOR ALF\n")

word = input("Please, enter a word/s to check: ")


# Write the code ↓ to check if the entered word is a palindrome.
# Utilize string functions to compare the original word with its reverse.

reverse = word[::-1]

# Write the code ↓ to display whether the entered word is a palindrome or not.

if(word == reverse):
    print("'%s' is a palindrome." % word)
else:
    print("'%s' is not a palindrome." % word)

# Select and employ a string concatenation method based on your personal preference and comfort level.





