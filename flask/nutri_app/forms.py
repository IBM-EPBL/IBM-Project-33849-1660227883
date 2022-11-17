from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email
class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField(label='email',validators=[DataRequired(),Email()])
    password = PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password=PasswordField(label='confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='Sign Up')

class LoginForm(FlaskForm):
    email = StringField(label='email',validators=[DataRequired(),Email()])
    password = PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=16)])
    submit=SubmitField(label='Login')