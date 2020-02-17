from models import User

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash

## import flask login_user

from playhouse.shortcuts import model_to_dict


users = Blueprint('users', 'users')


## User routes

# user register route
@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()

	# make emails/ username case insensitive
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	print(payload)

	try:
		# check DB if user exists
		User.get(User.email == payload['email'] or User.username == payload['username'])

		return jsonify(
			data={},
			description=f"Account with Email {payload['email']} already exists",
			status=401
		), 401
	#exinate models. , just DoesNotExist
	except models.DoesNotExist:

		created_user = User.create(
			email=payload['email'],
			username=payload['username'],
			firstname=payload['firstname'],
			lastname=payload['lastname'],
			hometown=payload['hometown'],
			secretquestion=payload['secretquestion'],
			secretanswer=payload['secretanswer'],
			password=generate_password_hash(payload['password'])
		)

		# created user
		user_dict = model_to_dict(created_user)
		print(user_dict)

		### remove user password from response

		return jsonfiy(
			data=user_dict,
			message=f"Successfully registered {user_dict['email']}",
			status=201,
		), 201








