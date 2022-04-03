from flask import Blueprint
from flask import render_template
from flask_login import login_required, current_user

homepage = Blueprint('homepage', __name__)

@homepage.route('/')
def index():	
	return render_template('home.html')

@homepage.route('/profile')
@login_required
def profile():	
	return render_template('profile.html', name=current_user.name)
