from flask import Blueprint
from flask import render_template

homepage_blueprint = Blueprint('homepage_blueprint', __name__)

@homepage_blueprint.route('/')
def index():	
	return render_template('home.html')
