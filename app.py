from . import create_app

# Create app from create_app function
app = create_app()

if __name__ == '__main__':
	app.run(debug=True)
