'''
Write a program that prompts the user to input their name, age, and favorite food. Take this input, format it into a dictionary, 
and then encode and save it to a file named "output.json" using the json.dumps function.

NOTE: only use built-in libraries of python (do not use pandas etc.)
'''

import json

name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))
food = input("Please, enter your favorite food: ")

data = {
    "name" : name,
    "age" : age,
    "food" : food
}

values = json.dumps(data, indent=2)

with open('output.json', 'w') as file:
    file.write(values)