# flask-estate-api
Flask Real-Estate API to store user credentials/ search parameters to be utilized with React.js front-end and 3rd party API. 

step 0:
		create(for python): .gitignore --> .env & other relatables

step 1:
		run: 'virtualenv .env -p python3'

step 2:
		run: 'source .env/bin/activate'
		**(see notes below: need to 'deactivate' environment when done)

step?: (SKIP STEPS 3-4 WHEN CLONING ALREADY EXISTING FLASK APP FROM REPOSITORY, instead
		install listed modules in repo by running:	'pip3 install -r requirements.txt')

step 3:
		run: 'pip3 install flask'

step 4:
		run: 'pip3 freeze > requirements.txt'

step 5:
	Program server --> then run command in CLI UI: 'python3 app.py' (python_runtime_environment & python_file_name).

	note: should see something similar to --
		 * Serving Flask app "app" (lazy loading)
 		 * Environment: production
		   WARNING: This is a development server. Do not use it in a production deployment.
		   Use a production WSGI server instead.
		 * Debug mode: on
		 * Running on http://....(irrelevant number):8000/ (Press CTRL+C to quit)
		 * Restarting with stat
		 * Debugger is active!
		 * Debugger PIN