"""
This will be the file that runs our web server for this project
"""

from flask import Flask, render_template, request
from reader import find_potential, details

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    global recipe_details
    if request.method == "POST":
        if request.form.get("INPUT"):
            words = request.form['INPUT'].lower().split(" ")
            
            potential = find_potential(words)
            recipe_details = details(potential)
        
            cuisines = []
            for recipe in recipe_details:
                if recipe[3] not in cuisines:
                    cuisines.append(recipe[3])
    
            return render_template('index.html', cuisines = cuisines)

        if request.form["cuisine"]:
            cuisine_details = []
            for recipe in recipe_details:
                if recipe[3].split()[0] == request.form["cuisine"]:
                    cuisine_details.append(recipe)
            return render_template('display.html', details = cuisine_details)

    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)
