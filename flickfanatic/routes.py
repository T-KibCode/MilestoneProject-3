import requests
from flask import redirect, url_for, render_template, flash, redirect
from flickfanatic import app
from flickfanatic.forms import RegistrationForm, LoginForm
from flickfanatic.models import User, Post

    


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

@app.route("/signup", methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("signup.html", title="Signup", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login", form=form)

#@app.route('/movies')
#def movies():
    
    #movies = Movie.query.all()
    #return render_template('movies.html', movies=movies)


