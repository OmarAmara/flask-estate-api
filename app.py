## imported modules

# g(global variable)
from flask import Flask, g

# try destructuring here or importing specific variables
from models import DATABASE



DEBUG = True
PORT = 8000 # hidr in production into .env
"""For Development Only"""


app = Flask(__name__)




# decrease SQL connection pool, open/close (before/ after) DB on every request
@app.before_request
def before_request():
	g.db = DATABASE
	g.db.connect()

@app.after_request
def after_request(respons):
	d.db.close()
	return response




### Listener
if __name__ == '__main__':
	# requiring DB before listener below. Sets-up tables in models.py
	# models.initialize()
	app.run(debug=DEBUG, port=PORT)