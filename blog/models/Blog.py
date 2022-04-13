from datetime import datetime
from email.mime import image
from ... import db

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String)
	owner = db.Column(db.String)
	subtitle = db.Column(db.String)
	role = db.Column(db.String)
	date = db.Column(db.DateTime)
	image = db.Column(db.String)

class BlogController():
	@staticmethod
	def get_all_blogs():
		return Blog.query.all()

	@staticmethod
	def get_blog_by_id(id):
		return Blog.query.filter_by(id=id).first()

	@staticmethod
	def get_blog_by_owner(owner):
		return Blog.query.filter_by(owner=owner).all()

	@staticmethod
	def get_blog_by_role(role):
		return Blog.query.filter_by(role=role).all()

	@staticmethod
	def get_blog_by_date(date):
		return Blog.query.filter_by(date=date).all()

	@staticmethod
	def create_blog(content, owner, subtitle, role, image):
		new_blog = Blog(content=content, owner=owner, subtitle=subtitle, role=role, date=datetime.now(), image=image)
		db.session.add(new_blog)
		db.session.commit()
