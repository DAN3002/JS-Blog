from flask import Blueprint
from flask import render_template

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():	
	return render_template('blog.html')
