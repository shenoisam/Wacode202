# This file defines all of the form classes for the user object in the database

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class TakeSurveyForm(FlaskForm):
    param1 = StringField('param', validators=[DataRequired()])
    submit = SubmitField('Sign In')
