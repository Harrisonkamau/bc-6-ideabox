from iapplication import app
from flask import render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()
