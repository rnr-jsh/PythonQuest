# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.

print("VOWEL COUNTER FOR ALF\n")

str = input("Please, enter a word/s to check: ")

# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.

lower_str = str.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
num = 0

for vowel in vowels:
    num = num + lower_str.count(vowel)


# Write the code ↓ to display the count of vowels in the word.

print("The number of vowels in '%s' is: %d" % (str, num))

# Select and employ a string concatenation method based on your personal preference and comfort level.
        





