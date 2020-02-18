## modules

import datetime

from peewee import *

# enable cookies/ login authentication
from flask_login import UserMixin


#### .gitignore DB connection during deployment, transfer to psql
# portable data for development: value = DB connection string
DATABASE = SqliteDatabase('searches.sqlite')


## class models
class User(UserMixin, Model):
	## Place Limits on characters allowed for certain fields
	email = CharField(unique=True)
	username = CharField()
	# Future: min length, requirements
	password = CharField()
	firstname = CharField()
	lastname = CharField()
	hometown = CharField()
	# Future: change to preset values for user to choose when creating account. --> more secure
	secretquestion = CharField()
	secretanswer = CharField()
	created_on = DateTimeField(default=datetime.datetime.now)

	# specifies how to connect to DB
	class Meta:
		database = DATABASE

class Search(Model):
		## Place Limits on characters allowed for certain fields
	name = CharField()
	# charfield, extended zipcode includes a dahs '-' between numbers
	zipcode = CharField()
	# square feet, number
	sqrft = IntegerField()
	# For pice range. May need to be altered.
	upperprice = IntegerField()
	lowerprice = IntegerField()
	client = ForeignKeyField(User, backref='searches')
	created_on = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE


# method to set-up DB's connection
def initialize():
	DATABASE.connect()


# creates tables for classes above
DATABASE.create_tables([User, Search], safe=True)
print('Connected to DB, created tables if non-existed')
#######print/insert date here!###########

# close DB connection, free space in connection pool
DATABASE.close()
