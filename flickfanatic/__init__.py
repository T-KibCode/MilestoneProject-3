#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
if os.path.exists('env.py'):
    import env  # noqa

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tokenSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # type: ignore
login_manager.login_message_category = 'info'

from flickfanatic import routes
