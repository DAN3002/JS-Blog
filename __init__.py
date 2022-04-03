from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
	# Create the Flask application object
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'js-blog-secret-key'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///js-blog-db.sqlite'

	db.init_app(app)

	# Import the views module
	from .homepage.views import homepage
	from .auth.views import auth
	
	# Register the blueprint with the application
	app.register_blueprint(homepage)
	app.register_blueprint(auth, url_prefix="/auth")
	
	# Return the application object
	return app
