from app import db
from sqlalchemy.orm import relationship
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from datetime import datetime



class BlogPost(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return "<{}>".format(self.title)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String,nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    # confirmed = db.Column(db.Boolean, nullable=False, default=False)
    # confirmed_on = db.Column(db.DateTime, nullable=True)
    posts = relationship("BlogPost", backref="author")


    def __init__(self, name, email, password, admin=False, confirmed_on=None):
        self.name = name
        self.email = email
        self.password = password
        self.registered_on = datetime.now()
        self.admin = admin
        # self.confirmed = confirmed
        # self.confirmed_on = confirmed_on #  analyze the difference between the registered_on and confirmed_on dates

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required()
        # validators.EqualTo('confirm', message='Passwords must match')
    ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.Required()])
