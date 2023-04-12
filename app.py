import os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page" 

if __name__ == "__name__":
    app.run()

