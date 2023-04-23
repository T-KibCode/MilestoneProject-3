import requests
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

## Dummy Data 

posts = [
    {
    'author': 'Twaha Kibirige',
    'title': 'Blog Post',
    'content': 'First post content',
    'date_posted': 'January 1st, 2020',
    },
    {
    'author': 'John Smith',
    'title': 'Blog Post',
    'content': 'First post content',
    'date_posted': 'December 12th, 2021',
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", posts=posts)

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/search")
def search():
    return render_template("search.html", title="Film Search")

@app.route("/signup")
def signup():
    return render_template("signup.html", title="Signup")



if __name__ == "__main__":
    app.run(debug=True)



