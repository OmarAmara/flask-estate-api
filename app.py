## imported modules
# for deployment
import os

# g(global variable)
from flask import Flask, g, jsonify

from flask_cors import CORS

### Install and import CORS here ###

from flask_login import LoginManager

# try destructuring here or importing specific variables
from resources.users import users
from resources.searches import searches

# from models import DATABASE, User, DoesNotExist, initialize
import models


DEBUG = True
PORT = 8000 # hidr in production into .env
"""For Development Only"""


app = Flask(__name__)
##### secret key: Store as environment variable when deploying
app.config.update(
	# TESTING=True,
	SECRET_KEY='Super secret, nobody will ever guess it! Not #ven _/'
)

# instantiate
login_manager = LoginManager()
# connect app
login_manager.init_app(app)

# cookie created with login_user as can be seen in register/ login users routes
@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
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


# development # change the origins that are accepted when deploying. supports_credentials(cookies)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(searches, origins=['http://localhost:3000'], supports_credentials=True)


# blueprint to set 'controllers' to handle model routes
app.register_blueprint(users, url_prefix='/api/v1.0/users')
app.register_blueprint(searches, url_prefix='/api/v1.0/searches')

# decrease SQL connection pool, open/close (before/ after) DB on every request
@app.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response

# in production, app is run with gunicorn, this initializes the tables in that case.
if 'ON_HEROKU' in os.environ:
	print('\non heroku!')
	models.initialize()

### Listener
if __name__ == '__main__':
	# requiring DB before listener below. Sets-up tables in models.py
	models.initialize()
	app.run(debug=DEBUG, port=PORT)