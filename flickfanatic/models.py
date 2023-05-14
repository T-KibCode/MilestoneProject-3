import os #import os
import jwt
import configparser #import configparser
from datetime import datetime, timezone, timedelta
from flask import app #import datetime
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer #import serializer
from flickfanatic import db, login_manager, app #import db and login manager
from flask_login import UserMixin #import usermixin


@login_manager.user_loader #load user by id
def load_user(user_id): #load user by id
    return User.query.get(int(user_id)) #get user by id


class User(db.Model, UserMixin): #user model
    id = db.Column(db.Integer, primary_key=True) #unique id
    username = db.Column(db.String(20), unique=True, nullable=False) #unique username
    email = db.Column(db.String(120), unique=True, nullable=False) #unique email
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') #profile picture
    password = db.Column(db.String(60), nullable=False) #hash password
    posts = db.relationship('Post', backref='author', lazy=True) #one to many relationship with posts

    def get_reset_token(self, expired_sec=1800): #get reset token
        s = jwt.encode({"exp": datetime.now(tz=timezone.utc) + timedelta(
            seconds=expired_sec), "user_id": self.id}, app.config['SECRET_KEY'], algorithm="HS256") # type: ignore #encode token
        return s #return token

    @staticmethod #static method
    def verify_reset_token(token): #verify reset token
        try:
            s = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"]) # type: ignore #decode token
            user_id = s['user_id'] #get user id
        except: 
            return None #return none if token is invalid
        return User.query.get(user_id) #return user by id


class Post(db.Model): #post model
    id = db.Column(db.Integer, primary_key=True) #unique id
    title = db.Column(db.String(100), nullable=False) #title
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #date posted
    content = db.Column(db.Text, nullable=False) #content
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #user id 

    def __repr__(self): #return post object
        return f"Post('{self.title}', '{self.date_posted}')"

