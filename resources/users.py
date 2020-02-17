from models import User, DoesNotExist

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash

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
		User.get(User.email == payload['email'])

		### Find way to retrieve username with same query like below:
		# User.get(User.email == payload['email'], User.username == payload['username'])

		# if User.email == payload['email'] and User.username == payload['username']:
		# 	description = f"Account with Email {payload['email']} and Username {payload['username']} already exists",
		# elif User.username == payload['username']:
		# 	description = f"Account with Username {payload['username']} already exists",
		# else:
		# 	desctiption = f"Account with Email {payload['email']} already exists",

		return jsonify(
			data={},
			# description=description,
			description= f"Account with Email {payload['email']} already exists",
			status=401
		), 401
	#exinate models. , just DoesNotExist
	except DoesNotExist:

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

		user_dict.pop('password')
		user_dict.pop('secretanswer')
		user_dict.pop('secretanswer')

		return jsonify(
			data=user_dict,
			message=f"Successfully registered {user_dict['email']}",
			status=201,
		), 201


# user login route
@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	# payload['username'] = payload['username'].lower()
	try:
		# find by email
		user = User.get(User.email == payload['email'].lower())

		# if found, compare to password
		user_dict = model_to_dict(user)
		compare_password = check_password_hash(user_dict['password'], payload['password'])

		# if there is a match
		if compare_password:

			user_dict.pop('password')
			user_dict.pop('secretanswer')
			user_dict.pop('secretanswer')
			return jsonify(
				data=user_dict,
				message=f"Successfully logged in: {user_dict}",
				status=200
			), 200

		else:
			print('Password does not match user')

			return jsonify(
				data={},
				message='Email or Password is incorrect',
				status=401
			), 401

	# user not found
	except DoesNotExist:
		print('Username/ Email does not match')
		return jsonify(
			data={},
			message='Email or Password is incorrect',
			status=401
		), 401






