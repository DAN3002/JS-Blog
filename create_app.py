from flask import Flask

def create_app():
	# Create the Flask application object
	app = Flask(__name__)

	# Import the views module
	from homepage.views import homepage_blueprint
	
	# Register the blueprint with the application
	app.register_blueprint(homepage_blueprint)
	
	# Return the application object
	return app
