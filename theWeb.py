#!/usr/bin/env python
from werkzeug.utils import redirect

from db import DB_Connection
from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect("/")
    return render_template('login.html', error=error)
