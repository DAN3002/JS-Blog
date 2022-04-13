from flask import Blueprint, render_template, request, redirect, url_for, session
from ..blog.models.Blog import BlogController

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
