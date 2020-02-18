from models import Search, DoesNotExist

from flask import Blueprint, request, jsonify

# current_user = user logged in, login_required requires to be logged in to access route.
from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict

# searches Blueprint/ 'controller'
searches = Blueprint('searches', 'searches')


#### create routes, utilize login_required: index, delete, update

# search list index
# @searches.route('/', methods=['GET'])
# # route only available if logged in
# @login_required
# def searches_index():
	# INSERT QUERY AND RETURN LOGIC


# search create route
@searches.route('/', methods=['POST'])
@login_required
def create_search():
	payload = request.get_json()

	search = Search.create(
		name=payload['name'],
		zipcode=payload['zipcode'],
		sqrft=payload['sqrft'],
		upperprice=payload['upperprice'],
		lowerprice=payload['lowerprice'],
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

### route to delete





