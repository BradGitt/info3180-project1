from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "prettydolphin"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bradgitt:prettydolphin@localhost/profiledb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning



app.config['UPLOAD_FOLDER']= './app/static/uploads' 
# ALLOWED_EXTENSIONS = set(['jpg','png','JPG'])
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config.from_object(__name__)

from app import views

