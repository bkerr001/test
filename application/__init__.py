from flask import Flask,
from flask_sqlalchemy import SQLAlchemy
import pymysql
import application.secrets
from datetime import datetime
import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, current_user, login_fresh
from flask_login import LoginManager

#
app = Flask(__name__)
app.config['SECRET_KEY'] = '38b428042776212a1742ff87938f535b'
conn= 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(secrets.usr, secrets.psswd, secrets.dbhost, secrets.database)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager =  LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from application import routes
