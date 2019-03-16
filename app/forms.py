from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    fname = StringField('First Name',
    validators=[DataRequired(), Length (max=20)])
    
    lname = StringField('Last Name',
    validators=[DataRequired()])
    
    gender = SelectField('Gender', choices=[('s',"Select Gender"),('m', 'Male'), ('f', 'Female')])
    
    email = StringField('Email',
    validators=[DataRequired()])
    
    location= StringField('Location',
    validators=[DataRequired()])
    
    biography = StringField('Biography',
    validators=[DataRequired()])
    
    # Submit = SubmitField('Send')