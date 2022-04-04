from flask import Blueprint, render_template, request, redirect, url_for

quest = Blueprint('quest', __name__)

@quest.route('/', methods = ['GET'])
def index():
	type = request.args.get('type', None)

	# redirect to the homepage if type is None
	if type is None:
		return redirect(url_for('homepage.index'))


	return type

