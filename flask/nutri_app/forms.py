from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email
class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField(label='Email',validators=[DataRequired(),Email()]) 
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign up')
    
class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email()]) 
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    submit = SubmitField(label='Login')
    