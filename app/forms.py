from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Form(FlaskForm):
    fname = StringField('First Name')
    # validators=[DataRequired(), Length (max=20)])
    
    lname = StringField('Last Name')
    # validators=[DataRequired()])
    
    gender = SelectField('Gender', choices=[('s',"Select Gender"),('Male', 'Male'), ('Female', 'Female')])
    
    email = StringField('Email')
    # validators=[DataRequired()])
    
    location= StringField('Location')
    # validators=[DataRequired()])
    
    biography = StringField('Biography')
    # validators=[DataRequired()])
    
    upload = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'JPG'], 'Images only!')])
    
    # Submit = SubmitField('Send')