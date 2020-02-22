from flask import Flask, request
from flask import render_template, redirect, url_for, flash, session, Blueprint
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from flask_bootstrap import Bootstrap
from WebForms.User import LoginForm, RegisterForm, Geolocate, SurveyForm
from secrets import SECRET_KEY
from WebForms.controller import Controller
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = "/Users/samshenoi/Desktop/Wacode2020/static/images/"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Create the flask app

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Bootstrap(app)
c = Controller()


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
    myquestions = dict()
    myquestions["Are you drunk?"] = ["Yes", "No", "Maybe", "Apply Hadamard to find out"]
    form = SurveyForm( obj={"Are you drunk?"})
    form.questions.choices = myquestions.keys()
    # If the form is submittable, submit it
    user = session.get('user', None)
    if user is not None:
        if form.validate_on_submit():
            redirect(render_template('success.html', error=error))
        return render_template('question.html', error=error, form=form)
    return redirect('/login')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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


@app.route('/checkLocation', methods=['GET', 'POST'])
def upload_file():
    error = None
    GeoForm = Geolocate()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fi = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(fi)
            res = c.Geolocate(fi)
            print(res[0],res[1])
            return render_template('success.html', error=error, v=res, long='%.2f'%(res[0]), lat='%.2f'%(res[1]))
    return render_template('upload_image.html', error=error, form=GeoForm)


app.run(debug=True)
