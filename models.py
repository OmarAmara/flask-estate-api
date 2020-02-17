## modules

import datetime

from peewee import *





#### .gitignore DB connection during deployment, transfer to psql
# portable data for development: value = DB connection string
DATABASE = SqliteDatabase('searches.sqlite')



## class models
class User(Model):
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

# class Search(Model):
	# origin = ForeignKeyField(User, backref='searches')


# method to set-up DB's connection
def initialize():
	DATABASE.connect()


# creates tables for classes above
# DATABASE.create_tables([ ], safe=True)
print('Connected to DB, created tables if non-existed')
#######print/insert date here!###########

# close DB connection, free space in connection pool
DATABASE.close()
