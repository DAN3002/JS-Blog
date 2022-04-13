from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from ..blog.models.Blog import BlogController
import uuid
import os

blog = Blueprint('blog', __name__)

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

	f.save(path)

	# Get data from request body

	name = request.form['name']
	role = request.form['role']
	subtitle = request.form['subtitle']
	fullContent = request.form['fullContent']


	# Add new blog
	BlogController.create_blog(fullContent, name, subtitle, role, path)

	return jsonify({
		'status': 'success'
	})
