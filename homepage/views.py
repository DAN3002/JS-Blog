from flask import Blueprint, session
from flask import render_template
from flask_login import login_required, current_user

# Import BlogController
from ..blog.models.Blog import BlogController

homepage = Blueprint('homepage', __name__)

@homepage.route('/')
def index():
	# Get all blog and pass to template
	blogs = BlogController.get_all_blogs()

	print(session.get("status"))

	return render_template('home.html', blogs=blogs)

@homepage.route('/profile')
@login_required
def profile():	
	return render_template('profile.html', name=current_user.name)
