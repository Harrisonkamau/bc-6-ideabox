from sqlalchemy.orm import relationship
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms.validators import InputRequired
from datetime import datetime
from wtforms.fields.html5 import EmailField
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask.ext.security import Security, SQLAlchemyUserDatastore
from app import db



class PostIdea(db.Model):
    # __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __init__(self, title, description, user_id):
    #     self.title = title
    #     self.description = description
    #     self.user_id = user_id

    # A method to reprensent a query when called
    def __repr__(self):
        return "<{}>".format(self.title)


# Create a class User
class User(db.Model):
    # __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String,nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    # posts = relationship("PostIdea", backref="user")


    # def __init__(self, name, email, password):
    #     self.name = name
    #     self.email = email
    #     self.password = password



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

# create a Votes class
# class VotesCount(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20), nullable=False)
#     description = db.Column(db.String, nullable=False)
#     post_id = db.Column(db.Integer, db.ForeignKey('postidea.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class RegistrationForm(Form):
    username = TextField('Username', validators = [InputRequired('Please enter your name')])
    email = EmailField('Email Address', validators = [InputRequired('Please enter your email address')])
    password = PasswordField('New Password', [
        validators.Required()
    ])


# create a class for social authentication
# class SocialOauth(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     provider_id = db.Column(db.String(255))
#     provider_user_id = db.Column(db.String(255))
#     access_token = db.Column(db.String(255))
#     secret = db.Column(db.String(255))
#     display_name = db.Column(db.String(255))
#     profile_url = db.Column(db.String(512))
#     image_url = db.Column(db.String(512))
#     rank = db.Column(db.Integer)

# Security(app, SQLAlchemyUserDatastore(db, User, PostIdea))
# Social(app, SQLAlchemyConnectionDatastore(db, SocialOauth))
