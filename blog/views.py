from flask import Blueprint, render_template, request, redirect, url_for
from ..blog.models.Blog import BlogController

blog = Blueprint('blog', __name__)

@blog.route('/view')
def view_blog():
	id = request.args.get('id', None)

	if id is None:
		return redirect(url_for('homepage.index'))

	blog = BlogController.get_blog_by_id(id)
	return render_template('blog.html', blog=blog)


