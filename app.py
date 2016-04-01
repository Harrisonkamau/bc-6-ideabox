'''This is the application logic'''

# import the Flask class from slask module
from flask import Flask, render_template, request, redirect, url_for, session,flash, g
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import sqlite3
import os
from config import Config # import the Config class from module config


# create the application object
app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS']) # application configuration
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.database = "posts.db"
app.secret_key = "This-is-confidential"

# create and config the database object
db = SQLAlchemy(app)
from models import *
# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

# use  decorators to link a function to url
@app.route('/dashboard')
@login_required
def home():
    return render_template('index.html')


@app.route('/')
def welcome():
    # import ipdb; ipdb.set_trace()

    # Read from database
    g.db = connect_db()
    cur = g.db.execute('select * from posts')

    # create an empty list
    posts = []
    for row in cur.fetchall():
        posts.append(dict(title=row[0],description=row[1]))
    print posts
    g.db.close()
    # Check if logged in
    if 'logged_in' in session:
        render_template('index.html', posts=posts)
    else:
        return render_template("homepage.html", posts=posts)
    return render_template("homepage.html") # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('email') != 'admin@gmail.com' or request.form.get('password') != 'admin':
            error = "Invalid credentials. Please try again"
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None) # pops out the True value of session and deletes the key(logged_in)
    flash('You were just logged out!')
    return redirect(url_for('home'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    # import ipdb; ipdb.set_trace()
    form = RegistrationForm(request.form, PostIdea)
    if request.method == 'POST' and form.validate():
        user = User(request.form['username'] , request.form['password'],request.form['email'])
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

class Vote(object):
    count = 0
    def __init__(self, up, down):
        self.up = up
        self.down = down


    def vote(self):
        if self.up == True:
            count += 1
        else:
            count -= 1





def connect_db():
    return sqlite3.connect(app.database)


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)
