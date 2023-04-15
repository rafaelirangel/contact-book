# install all the dependencies
# run pipenv shell
# make connections 
# create models
# work on functionality

from peewee import *
# import IPython

# Create a database object
db = PostgresqlDatabase(
    'contactbook',  # name of the database
    user='',  # name of the user
    password='',  # password
    host='localhost',  # name of the host
    port=5432  # port
)

# Connect to the database
db.connect()

#Create a model
class BaseModel(Model):
  class Meta:
    database = db
    
class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    nickname = CharField()
    phone_num = IntegerField()
    email = CharField()
    
# 2. Create the table
db.drop_tables([Contact])       # first, drop the tables (if they exist)
db.create_tables([Contact])     # then, create the tables from scratch

#Create a contact
rafaeli = Contact(first_name = 'Rafaeli', last_name ='Rangel', nickname = 'Rafa', phone_num = 123455673, email = 'rafaelirangel@test.com')
rafaeli.save()