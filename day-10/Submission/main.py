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
