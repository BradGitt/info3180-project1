from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'prettydlphin'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'e8e9f499da701c'
app.config['MAIL_PASSWORD'] = 'd521e9ecc3b984'
mail = Mail(app)

UPLOAD_FOLDER  = './app/static/uploads' 
ALLOWED_EXTENSIONS = set(['jpg','png','JPG'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER


from app import views

