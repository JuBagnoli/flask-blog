from os import getenv

getenv('SECRET_KEY')
getenv('DATABASE_URI')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('DATABASE_URI')
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)
from application import routes
