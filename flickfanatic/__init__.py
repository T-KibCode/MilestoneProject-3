from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
## Good practice to secure session token with secret keys
app.config['SECRET_KEY'] = '79d20b7616702de60f914aabc8b86f78'
## SQL demo database creation
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)

from flickfanatic import routes
