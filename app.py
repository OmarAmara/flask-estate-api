## imported modules

from flask import Flask

import models



DEBUG = True
PORT = 8000 # hidr in production into .env
"""For Development Only"""


app = Flask(__name__)









### Listener
if __name__ == '__main__':
	# requiring DB before listener below. Sets-up tables in models.py
	# models.initialize()
	app.run(debug=DEBUG, port=PORT)