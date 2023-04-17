from peewee import *

# Connection
db = PostgresqlDatabase(
    'contacts',
    user='',
    password='',
    host='localhost',
    port=5432)

db.connect()

# Model
class BaseModel(Model):
    class Meta:
        database = db


class ContactBook(BaseModel):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    phone = IntegerField()


# Remove table if they exist then Create table from scratch
db.drop_tables([ContactBook])
db.create_tables([ContactBook])

#Create a new contact
def create_contact():
    first_name = input('What is the First Name? ')
    last_name = input('What is the Last Name? ')
    email = input('Enter an email address: ')
    phone = int(input('Enter a phone number: '))
    new_contact = ContactBook(first_name=first_name, last_name=last_name, email=email, phone=phone)
    new_contact.save()
