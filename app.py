import requests
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/search")
def search():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)

    