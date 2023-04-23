import requests
from flask import Flask, redirect, url_for, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


## Good practice to secure session token with secret keys
app.config['SECRET_KEY'] = '79d20b7616702de60f914aabc8b86f78'



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

@app.route("/search")
def search():
    return render_template("search.html", title="Film Search")

@app.route("/signup")
def signup():
    form = RegistrationForm()
    return render_template("signup.html", title="Signup", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)



if __name__ == "__main__":
    app.run(debug=True)



