from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "confirme2"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab5:prettydolphin@localhost/lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

UPLOAD_FOLDER  = './app/static/uploads' 
ALLOWED_EXTENSIONS = set(['jpg','png','JPG'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER


from app import views

