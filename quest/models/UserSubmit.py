from datetime import datetime
from ... import db

class UserSubmit(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	level = db.Column(db.Integer)
	date = db.Column(db.DateTime)

class UserSubmitController():
	@staticmethod
	def get_latest_submit(user_id):
		return UserSubmit.query \
			.filter_by(user_id=user_id) \
			.order_by(UserSubmit.level.desc()) \
			.first()

	@staticmethod
	def add_new_submit(user_id, level):
		new_submit = UserSubmit(user_id=user_id, level=level, date=datetime.now())
		db.session.add(new_submit)
		db.session.commit()
