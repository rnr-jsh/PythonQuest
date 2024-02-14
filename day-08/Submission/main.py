'''
Create a Python script that does the following:

Reads the "example1.csv" file and prints the values in the first column.
Reads the "example2.json" file and prints its contents.
NOTE: only use built-in libraries of python (do not use pandas etc.)
'''

import csv
import json

with open('example1.csv', 'r') as csvf:
    reader_csv = csv.reader(csvf)

    next(reader_csv) #comment this line if column title should be included

    for line in reader_csv:
        print(line[0])

print('\n\n') # to make the two prints separated

with open('example2.json', 'r') as jsonf:
    reader_json = json.load(jsonf)
    output = json.dumps(reader_json, indent=2)
    print(output)