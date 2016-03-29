# import the Flask class from slask module
from flask import Flask, render_template, request, redirect, url_for, session,flash, g
from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)

app.secret_key = "lilian wanjiru"
app.database = "posts.db"

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
@app.route('/')
@login_required
def home():
    # return "Hello, world!" # returns a string
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    print cur
    print cur.fetchall()
    posts =[dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # print posts
    g.db.close()
    return render_template('index.html', posts=posts)


@app.route('/welcome')

def welcome():
    return render_template("welcome.html") # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
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
    return redirect(url_for('welcome'))

def connect_db():
    return sqlite3.connect(app.database)


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)
