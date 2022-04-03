from flask import Blueprint, render_template
from .. import db

auth = Blueprint('auth_blueprint', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'
