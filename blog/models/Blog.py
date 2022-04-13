from datetime import datetime
from ... import db

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String)
	owner = db.Column(db.String)
	role = db.Column(db.String)
	date = db.Column(db.DateTime)


