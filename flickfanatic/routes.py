import requests
from flask import render_template, url_for, redirect, flash, redirect
from flickfanatic import app, db, bcrypt
from flickfanatic.forms import RegistrationForm, LoginForm
from flickfanatic.models import User, Post
from flask_login import login_user, current_user, logout_user



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("signup.html", title="Signup", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
def account():
    return render_template('account.html', title='Account')
