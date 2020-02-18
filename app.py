## imported modules

# g(global variable)
from flask import Flask, g, jsonify

### Install and import CORS here ###

from flask_login import LoginManager

# try destructuring here or importing specific variables
from resources.users import users
from resources.searches import searches

from models import DATABASE, User, DoesNotExist, initialize


DEBUG = True
PORT = 8000 # hidr in production into .env
"""For Development Only"""


app = Flask(__name__)


##### secret key: Store as environment variable, .gitignore when deploying
app.secret_key = 'Super secret, nobody will ever guess it!'

# instantiate
login_manager = LoginManager()
# connect app
login_manager.init_app(app)

# cookie created with login_user as can be seen in register/ login users routes
@login_manager.user_loader
def load_user(userid):
	try:
		return User.get(User.id == userid)
	except DoesNotExist:
		return None


# change default html unauthorized response to custom json
@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data={
			'unauthorized': 'User must login to account'
		},
		message='You must be logged in to access resource',
		status=401
	), 401
	

### CORS will be inserted here to enable access to API ### Will also need to be installed.


# blueprint to set 'controllers' to handle model routes
app.register_blueprint(users, url_prefix='/api/v1.0/users')
app.register_blueprint(searches, url_prefix='/api/v1.0/searches')

# decrease SQL connection pool, open/close (before/ after) DB on every request
@app.before_request
def before_request():
	g.db = DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response




### Listener
if __name__ == '__main__':
	# requiring DB before listener below. Sets-up tables in models.py
	initialize()
	app.run(debug=DEBUG, port=PORT)