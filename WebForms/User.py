# This file defines all of the form classes for the user object in the database

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FileField
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


class SurveyForm(FlaskForm):
    question1 = StringField('Name', validators=[DataRequired()])
    '''
    question1 =
    question2 = SelectField(myQuestion[1], choices=[(choiceList[1][0], 1), (choiceList[1][1], 2), (choiceList[1][2], 3),
                                                    (choiceList[1][3], 4)])
    question3 = SelectField(myQuestion[2], choices=[(choiceList[2][0], 1), (choiceList[2][1], 2), (choiceList[2][2], 3),
                                                    (choiceList[2][3], 4)])
    question4 = SelectField(myQuestion[3], choices=[(choiceList[3][0], 1), (choiceList[3][1], 2), (choiceList[3][2], 3),
                                                    (choiceList[3][3], 4)])
    question5 = SelectField(myQuestion[4], choices=[(choiceList[4][0], 1), (choiceList[4][1], 2), (choiceList[4][2], 3),
                                                    (choiceList[4][3], 4)])
    question6 = SelectField(myQuestion[5], choices=[(choiceList[5][0], 1), (choiceList[5][1], 2), (choiceList[5][2], 3),
                                                    (choiceList[5][3], 4)])
    question7 = SelectField(myQuestion[6], choices=[(choiceList[6][0], 1), (choiceList[6][1], 2), (choiceList[6][2], 3),
                                                    (choiceList[6][3], 4)])
    question8 = SelectField(myQuestion[7], choices=[(choiceList[7][0], 1), (choiceList[7][1], 2), (choiceList[7][2], 3),
                                                    (choiceList[7][3], 4)])
    question9 = SelectField(myQuestion[8], choices=[(choiceList[8][0], 1), (choiceList[8][1], 2), (choiceList[8][2], 3),
                                                    (choiceList[8][3], 4)])
    question10 = SelectField(myQuestion[9],
                             choices=[(choiceList[9][0], 1), (choiceList[9][1], 2), (choiceList[9][2], 3),
                                      (choiceList[9][3], 4)])
    
    '''