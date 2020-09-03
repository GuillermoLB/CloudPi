from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

class FormLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Introduce an username.')])
    password = PasswordField('Password', validators=[DataRequired(message='Introduce a password.')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class FormRegister(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat the password', validators=[DataRequired(),EqualTo('password', 'Passwords don´t meet')])
    submit = SubmitField('Register')