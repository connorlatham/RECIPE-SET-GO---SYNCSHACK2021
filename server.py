"""
This will be the file that runs our web server for this project
"""

from flask import Flask, render_template, request
import csv

f = open("recipes.csv", "r")

lines = csv.reader(f)

recipes = []

for line in lines:
    recipes.append(line)

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    words = request.form['INPUT'].upper().split(" ")
    
    counter = 0
    for recipe in recipes:
        wordcheck = True
        for word in words:
            if word not in recipe[1]:
                wordcheck = False
        if wordcheck:
            counter += 1
    return render_template('index.html', food = words, number = counter)
    
if __name__ == "__main__":
    app.run(debug=True)
