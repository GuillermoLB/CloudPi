from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Introduce an username.')])
    password = PasswordField('Password', validators=[DataRequired(message='Introduce a password.')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')