from flask import Flask
from flask import render_template, redirect, url_for, flash, session, Blueprint
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from flask_bootstrap import Bootstrap
from WebForms.User import LoginForm, RegisterForm
from secrets import SECRET_KEY
from WebForms.controller import Controller

# Create the flask app

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

Bootstrap(app)
c = Controller()


@app.route('/test')
def index2():
    return render_template('index.html')

@app.route('/items/<item>')
def item(item):
    return '<h1>THE ITEM PAGE!!! THE ITEM IS: {}.'.format(item)

@app.route('/')
def index():
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


# This route logs in the user to the software system
@app.route('/takeSurvey', methods=['GET', 'POST'])
def survey():
    error = None
    # Create an instance of the log in form
    form = TakeSurveyForm()
    # If the form is submittable, submit it
    user = session.get('user', None)
    if user is not None:
        if s is not None:
            session["user"] = s
            # Redirect back to the home page
            return redirect('/')
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm()
    if form.validate_on_submit():
        # Store the new user
        c.store_user(form.name.data, form.username.data, form.password.data)
        # Redirect to login
        return redirect('/login')
    # If it didn't work, redirect to the registration page
    return render_template('register.html', error=error, form=form)

app.run(debug=True)
