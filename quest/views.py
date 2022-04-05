from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from .enum import get_quest_info

quest = Blueprint('quest', __name__)

@quest.route('/', methods = ['GET'])
@login_required
def index():
	type = request.args.get('type', None)

	# redirect to the homepage if type is None
	if type is None:
		return redirect(url_for('homepage.index'))

	# Get and check quest info
	quest_info = get_quest_info(type)
	if quest_info is None:
		return redirect(url_for('homepage.index'))

	

	return render_template(f'/quest/{ type }.html')

