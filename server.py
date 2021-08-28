"""
This will be the file that runs our web server for this project
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

#def home():
#    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)
