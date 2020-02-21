# flask-estate-api
Flask Real-Estate API to store user credentials/ search parameters to be utilized with React.js front-end and 3rd party API. 
For an example of a front end utilizing these routes, check out react-estate repo at https://github.com/OAmara/react-estate.

	— USER Routes —
GET         /api/v1.0/users       -> Index — show all
POST       /api/v1.0/users        -> Create — create a new User
GET          (show user route)    -> Not a route, show User by saving response from login into variable 
PUT      /api/v1.0/users/(id)     -> Update — edit/change/update User. (Not yet a route)
DESTROY /api/v1.0/users/(id)      -> DESTROY User relatables and then DELETE User(not yet a route)

	— SEARCH Routes — 
GET         /api/v1.0/searches        -> Index — show all
POST       /api/v1.0/searches/        -> Create — create a new Search
GET       /api/v1.0/searches/(id)     -> Show specific/one Search
PUT      /api/v1.0/searches/(id)      -> Update — edit/change/update Search
DESTROY /api/v1.0/searches/(id)       -> DELETE Search


Set-up/ Install: (assuming you already have python3 installed)

	step 1:
			Run in CLI: 'virtualenv .env -p python3'

	step 2:
			Run in CLI: 'source .env/bin/activate'
			This will 
			**(see notes below: need to 'deactivate' environment when done)

	step 3:
			Install listed modules in requirements.txt file by Running CLI:	'pip3 install -r requirements.txt'

	step 4:
			Run in CLI: 'pip3 install flask'

	step 5:
			run: 'pip3 freeze > requirements.txt'

	step 6:
		Run command in CLI UI: 'python3 app.py' 
		(python_runtime_environment & python_file_name)
		This will start the server. If successful, you should see something similar to this:

			 * Serving Flask app "app" (lazy loading)
	 		 * Environment: production
			   WARNING: This is a development server. Do not use it in a production deployment.
			   Use a production WSGI server instead.
			 * Debug mode: on
			 * Running on http://....(irrelevant number):8000/ (Press CTRL+C to quit)
			 * Restarting with stat
			 * Debugger is active!
			 * Debugger PIN