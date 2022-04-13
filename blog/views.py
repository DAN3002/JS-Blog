from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from ..blog.models.Blog import BlogController
import uuid
import os

blog = Blueprint('blog', __name__)

import json

@blog.route('/view')
def view_blog():
	id = request.args.get('id', None)

	if id is None:
		return redirect(url_for('homepage.index'))

	blog = BlogController.get_blog_by_id(id)
	return render_template('blog.html', blog=blog)

@blog.route('/upload')
def upload_blog():
	# Check status from session if unlock
	if session.get('unlock_blog', False) == False:
		return redirect(url_for('homepage.index'))

	return render_template('upload.html')

@blog.route('/upload', methods=['POST'])
def upload_blog_post():
	from ..app import app

	# Upload file
	f = request.files['image']

	filename = uuid.uuid1().hex + secure_filename(f.filename)
	path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

	print(path)

	f.save(path)

	# Get data from request body
	# request_data = request.data
	# request_data = json.loads(request_data)

	# name = request_data['name']
	# role = request_data['role']
	# subtitle = request_data['subtitle']
	# fullContent = request_data['fullContent']


	# Add new blog
	# BlogController.add_new_blog(title, content)

	return jsonify({
		'status': 'success'
	})
