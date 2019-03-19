from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "prettydolphin"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:prettydolphin@localhost/profiledb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

UPLOAD_FOLDER  = './app/static/uploads' 
ALLOWED_EXTENSIONS = set(['jpg','png','JPG'])


app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER


from app import views

