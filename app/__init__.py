from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ydp01:ydp01!!!@localhost:3306/diet"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ydp01!!!@13.124.231.43:3306/diet"
app.config['JSON_AS_ASCII'] = False

db.init_app(app)

from app import views, models, utils