from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flask import jsonify 
from .models.UserSubmit import UserSubmitController

import json

from .enum import get_quest_info, get_quest_by_number

quest = Blueprint('quest', __name__)

PASSWORD = 'Bình'

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

	# Check it is quest latest or not
	latest_submit = UserSubmitController.get_latest_submit(current_user.id)


	if latest_submit is not None and quest_info['quest_id'] > latest_submit.level + 1:
		latest_quest = get_quest_by_number(latest_submit.level + 1)
		print(latest_quest)

		return redirect(f'/quest?type={ latest_quest }')

	return render_template(f'/quest/{ type }.html')

@quest.route('/submit_quest', methods = ['POST'])
def submit_quest():
	# Get password, type from request body
	request_data = request.data
	request_data = json.loads(request_data)

	password = request_data['quest_password']
	type = request_data['type']
	user_id = request_data['user_id']

	# Get and check quest info
	quest_info = get_quest_info(type)

	# Check if password is correct
	if password != quest_info['password']:
		return jsonify({ 'status': 'not success' })

	# add new Submit
	UserSubmitController.add_new_submit(user_id, quest_info['quest_id'])
	next_quest = quest_info['next_quest']

	return jsonify({
		'status': 'success',
		'next_quest': next_quest
	})

@quest.route('/check_pass', methods = ['POST'])
def check_pass():
	# Get password, type from request body
	request_data = request.data
	request_data = json.loads(request_data)

	password = request_data['quest_password']
	
	# Check if password is correct
	if password != PASSWORD:
		return jsonify({ 'status': 'not success' })

	return jsonify({ 'status': 'success' })
