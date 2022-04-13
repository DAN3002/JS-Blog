from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_session import Session

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
	# Create the Flask application object
	app = Flask(__name__, static_url_path='/static', static_folder='static')
	app.config['SECRET_KEY'] = 'js-blog-secret-key'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///js-blog-db.sqlite'

	app.config["SESSION_PERMANENT"] = False
	app.config["SESSION_TYPE"] = "filesystem"

	app.config['UPLOAD_FOLDER'] = 'static/img/user_upload'
	app.config['MAX_CONTENT_PATH'] = 50000000

	Session(app)

	db.init_app(app)
	migrate = Migrate(app, db)

	# Config Login
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	# Import the views module
	from .homepage.views import homepage
	from .auth.views import auth
	from .quest.views import quest
	from .blog.views import blog
	
	# Register the blueprint with the application
	app.register_blueprint(homepage)
	app.register_blueprint(auth, url_prefix="/auth")
	app.register_blueprint(quest, url_prefix="/quest")
	app.register_blueprint(blog, url_prefix="/blog")
	
	from .auth.models.User import User
	from .quest.models.UserSubmit import UserSubmit
	from .blog.models.Blog import Blog

	db.create_all(app=app)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	# Return the application object
	return app
