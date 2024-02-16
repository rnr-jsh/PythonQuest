from flask import Flask, jsonify  
import csv

app = Flask(__name__)

csv_file = 'programming_languages.csv'

def read_csv(filename):
    content = {}
    i = 0
    with open('programming_languages.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            content[i] = line
            i += 1
    return content

@app.route('/', methods=['GET'])
def get_langs():
    csv_file = read_csv('programming_languages.csv')
    return jsonify(csv_file)

if __name__ == '__main__':
    app.run(debug=True)