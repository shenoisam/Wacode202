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
    question = SelectField('Are you drunk', choices=[("Yes", "Yes"),("No", "No"), ("POTATOES", "NO")])
    submit = SubmitField('Submit')


class SurveyForm(FlaskForm):
    question1 = SelectField('What is the weather like?', choices=[("4","great!"),("0", "too drunk to tell"),("4", "snowing"), ("4", "rainy hard")], validators=[DataRequired()])
    question2 = SelectField('How many drink did you have??',
                            choices=[("0", "Can't even keep track"), ("1", "More than 3"), ("3", "1-2"),
                                     ("4", "None")], validators=[DataRequired()])
    question3 = SelectField('Count the number of bars |||||||||||||||||',
                            choices=[("0", "There are bars?"), ("1", "15"), ("3", "16"),
                                     ("4", "17")], validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddTrustedContacts(FlaskForm):
    TrustedContactEmail = StringField('TrustedContactEmail', validators=[DataRequired()])
    submit = SubmitField('Submit')