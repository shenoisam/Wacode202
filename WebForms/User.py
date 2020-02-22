# This file defines all of the form classes for the user object in the database

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FormField, SubmitField, SelectField, FileField, FieldList
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign In')


class TakeSurveyForm(FlaskForm):
    param1 = StringField('param', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')



class Geolocate(FlaskForm):
    image = FileField(u'Image File', validators=[DataRequired()])


class Question(FlaskForm):
    question = SelectField(u'Group', coerce=int)


class SurveyForm(FlaskForm):
    questions = FieldList(FormField(Question))
    submit = SubmitField('Submit')