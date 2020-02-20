import datetime

from models import Search, DoesNotExist

from flask import Blueprint, request, jsonify

# current_user = user logged in, login_required requires to be logged in to access route.
from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict


# searches Blueprint/ 'controller'
searches = Blueprint('searches', 'searches')


# search index route
@searches.route('/', methods=['GET'])
@login_required
def searches_index():
	current_user_searches = [model_to_dict(search) for search in current_user.searches]

	for dictionary in current_user_searches:
		dictionary['client'].pop('password')
		dictionary['client'].pop('secretanswer')
		dictionary['client'].pop('secretquestion')

	return jsonify(
		data=current_user_searches,
		message=f'Successfully retrieved {len(current_user_searches)} Searches for {current_user.firstname}',
		status=200
	), 200



############# CREATE AN INDEX ROUTE !login_required for unregistered users.... See todo.md for details.
# All Users: all searches index route



# search show route
@searches.route('/<id>', methods=['GET'])
def one_search(id):
	search = Search.get_by_id(id)

	# User is not logged in
	if not current_user.is_authenticated:
		jsonify(
			data={
				##### insert specific data that is public to all users
			},
			message='Register to have access to additional information and other user benefits.',
			status=200
		), 200
	# logged in/ registered user, can access additional info
	else:
		search_dict = model_to_dict(search)
		search_dict['client'].pop('password')
		search_dict['client'].pop('secretanswer')
		search_dict['client'].pop('secretquestion')

		if search.client_id != current_user.id:
			search_dict['client'].pop('hometown')
			search_dict['client'].pop('email')
			search_dict['client'].pop('created_on')
			search_dict['client']['lastname'] = 'hidden'
			search_dict['client']['username'] = 'hidden'

		return jsonify(
			data=search_dict,
			message=f"Found and displaying Search with id of {search.id}",
			status=200
		), 200


# search create route
@searches.route('/', methods=['POST'])
@login_required
def create_search():
	payload = request.get_json()

	### would this be more concise for users if search info is placed in a list or dict called search?
	### Just so that there is no confusion between client result and all others?
	search = Search.create(
		name=payload['name'],
		zipcode=payload['zipcode'],
		sqrft=payload['sqrft'],
		upperprice=payload['upperprice'],
		lowerprice=payload['lowerprice'],
		# last_modified=datetime.datetime.now,
		client=current_user.id
	)

	search_dict = model_to_dict(search)

	search_dict['client'].pop('password')
	search_dict['client'].pop('secretanswer')
	search_dict['client'].pop('secretquestion')

	return jsonify(
		data=search_dict,
		message='Successfully created Search!',
		status=201
	), 201


# search delete route
@searches.route('/<id>', methods=['Delete'])
@login_required
def delete_search(id):
	# find user's search
	search_to_delete = Search.get_by_id(id)

	if current_user.id == search_to_delete.client.id:
		search_to_delete.delete_instance()

		return jsonify(
			data={},
			message=f"Successfully deleted Search with id {id}",
			status=200
		), 200

	else:
		return jsonify(
			data={
				'error': 'FORBIDDEN'
			},
			message="Search client_id does not match logged in user_id. User can only delete their own stored searches",
			status=403
		), 403


# search update/edit route
@searches.route('/<id>', methods=['PUT'])
@login_required
def update_search(id):
	payload = request.get_json()

	# find search by id for verification in if statement below
	search = Search.get_by_id(id)

	# update search if search.client id matches logged in user id
	if search.client.id == current_user.id:

		### somehow utilize query already used to check if conditional.
		update_query = Search.update(**payload).where(Search.id == id)

		update_query.execute()

		# search.name = payload['name'] if 'name' in payload else None
		# search.zipcode = payload['zipcode'] if 'zipcode' in payload else None
		# search.sqrft = payload['sqrft'] if 'sqrft' in payload else None
		# search.upperprice = payload['upperprice'] if 'upperprice' in payload else None
		# search.lowerprice = payload['lowerprice'] if 'lowerprice' in payload else None
		# search.last_modified = datetime.datetime.now

		# update_search.save()
		# search_dict = model_to_dict(search)
		updated_search = Search.get_by_id(id)
		updated_search_dict = model_to_dict(updated_search)

		return jsonify(
			data=updated_search_dict,
			message=f"Successfully updated User's Search with id {id}",
			status=200
		), 200

	# account does not belong to user
	else:
		return jsonify(
			data={
				'error': 'FORBIDDEN'
			},
			message=f"Search's client_id of ({search.client.id}) does not match logged in user's id of ({current_user.id}). Can only update logged in user's Search.",
			status=403
		), 403







