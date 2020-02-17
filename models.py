## modules
from peewee import *





#### .gitignore DB connection during deployment, transfer to psql
# portable data for development: value = DB connection string
DATABASE = SqliteDatabase('searches.sqlite')



## class models

	# insert class models here

## class models


# method to set-up DB's connection
def initialize():
	DATABASE.connect()


# creates tables for classes above
# DATABASE.create_tables([ ], safe=True)
print('Connected to DB, created tables if non-existed')

# close DB connection, free space in connection pool
DATABASE.close()
