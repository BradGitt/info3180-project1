from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    name = StringField('Name',
    validators=[DataRequired(), Length (max=20)])
    
    email = StringField('E-mail',
    validators=[DataRequired()])
    
    subject = StringField('Subject',
    validators=[DataRequired()])
    
    message = StringField('Message',
    validators=[DataRequired()])
    
    # Submit = SubmitField('Send')