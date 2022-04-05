from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
	# Create the Flask application object
	app = Flask(__name__, static_url_path='/static', static_folder='static')
	app.config['SECRET_KEY'] = 'js-blog-secret-key'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///js-blog-db.sqlite'

	db.init_app(app)

	# Config Login
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	# Import the views module
	from .homepage.views import homepage
	from .auth.views import auth
	from .quest.views import quest
	
	# Register the blueprint with the application
	app.register_blueprint(homepage)
	app.register_blueprint(auth, url_prefix="/auth")
	app.register_blueprint(quest, url_prefix="/quest")
	
	from .auth.models.User import User
	from .quest.models.UserSubmit import UserSubmit

	db.create_all(app=app)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	# Return the application object
	return app
