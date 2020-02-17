## imported modules

# g(global variable)
from flask import Flask, g, jsonify

# try destructuring here or importing specific variables

from resources.users import users

from models import DATABASE, User


DEBUG = True
PORT = 8000 # hidr in production into .env
"""For Development Only"""


app = Flask(__name__)



# blueprint to set 'controllers' to handle model routes
app.register_blueprint(users, url_prefix='/api/v1.0/users')


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
	# models.initialize()
	app.run(debug=DEBUG, port=PORT)