from flask import Flask, jsonify  
import csv

app = Flask(__name__)

csv_file = 'programming_languages.csv'

def read_csv(filename):
    content = {}
    i = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            content[i] = line
            i += 1
    return content

@app.route('/', methods=['GET'])
def get_langs():
    csv_data = read_csv(csv_file)
    return jsonify(csv_data)

if __name__ == '__main__':
    app.run(debug=True)
