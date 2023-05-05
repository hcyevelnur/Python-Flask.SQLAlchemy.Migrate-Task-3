from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:salam1407@127.0.0.1:3308/Movie_db"
SQLALCHEMY_TRACK_MODIFICATIONS = True


from extensions import *
from controllers import *
from models import *





