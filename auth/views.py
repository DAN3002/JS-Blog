from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models.User import User

from .. import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
	return render_template('login.html')

@auth.route('/signup')
def signup():
	return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('homepage.index'))

@auth.route('/signup', methods=['POST'])
def signup_post():
	# code to validate and add user to database goes here
	email = request.form.get('email')
	name = request.form.get('name')
	password = request.form.get('password')

	user = User.query.filter_by(email=email).first()
	if user:
		flash('Email address already exists')
		return redirect(url_for('auth.signup'))

	new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

	db.session.add(new_user)
	db.session.commit()

	return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST'])
def login_post():
	# login code goes here
	email = request.form.get('email')
	password = request.form.get('password')
	remember = True if request.form.get('remember') else False

	user = User.query.filter_by(email=email).first()

	# check if the user actually exists
	# take the user-supplied password, hash it, and compare it to the hashed password in the database
	if not user or not check_password_hash(user.password, password):
		flash('Please check your login details and try again.')
		return redirect(url_for('auth.login'))

	# if the above check passes, then we know the user has the right credentials
	login_user(user, remember=remember)
	return redirect(url_for('homepage.profile'))
