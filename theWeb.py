#!/usr/bin/env python

# Import statements
from flask import Flask
from flask import render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from WebForms.User import LoginForm
from secrets import SECRET_KEY
from WebForms.controller import Controller
from flask_nav.elements import Navbar, View
from flask_nav import Navigation

# Create the flask app

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)
c = Controller()

nav = Navigation()


@nav.navigation()
def mynavbar():
    return Navbar(
        'mysite',
        View('Home', 'index'),
    )


nav.init_app(app)


@app.route('/')
def hello_world():
    error = None
    form = LoginForm()
    user = session.get('user', None)
    if user is not None:
        return render_template('index.html', error=error)
    else:
        return render_template('login.html', error=error, form=form)


# This route logs in the user to the software system
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # Create an instance of the log in form
    form = LoginForm()
    # If the form is submittable, submit it
    if form.validate_on_submit():
        # Validate the users credentials against the database and store their session
        s = c.validate_user(form.username.data, form.password.data)
        # If the user is validated, save the session
        if s is not None:
            session["user"] = s
            # Redirect back to the home page
            return redirect('/')
    # Otherwise if this is a Get request or the validation failed, render the login template
    return render_template('login.html', error=error, form=form)
