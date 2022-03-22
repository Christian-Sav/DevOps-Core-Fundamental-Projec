from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{getenv('MYSQL_ROOT_PASSWORD')}@mysql/app-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv ('SECRET_KEY')

db = SQLAlchemy(app)

import Project.routes