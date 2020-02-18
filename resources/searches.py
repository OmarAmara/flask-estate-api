from models import Search, DoesNotExist

from flask import Blueprint, request, jsonify

# current_user = user logged in, login_required requires to be logged in to access route.
from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict

searches = Blueprint('searches', 'searches')



#### create routes, utilize login_required