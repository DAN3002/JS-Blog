from flask import Blueprint
from flask import render_template

homepage = Blueprint('homepage_blueprint', __name__)

@homepage.route('/')
def index():	
	return render_template('home.html')
