# install all the dependencies
# run pipenv shell
# make connections 
# create models
# work on functionality

from peewee import *
import argparse 
# import IPython

# Create a database object
db = PostgresqlDatabase(
    'contactbook',  # name of the database
    user='rafa',  # name of the user
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

#Create a contact as an example
# rafaeli = Contact(first_name = 'Rafaeli', last_name ='Rangel', nickname = 'Rafa', phone_num = 123455673, email = 'rafaelirangel@test.com')
# rafaeli.save()

# Arguments (aka positional arguments) are required inputs to a command-line application
# Main function 
def contact_book():
    print('''Choose one of the following options to continue: 
          1 - See all your contacts
          2 - Seacrh for a specif contact by the first name
          3 - Add a new contact to your list
          4 - Update an existing contact
          5 - Delete a contact
          ''')
    
    user_input = int(input('Enter a num: '))
    if user_input == 1:
        all_contacts()
    elif user_input == 2:
        search_contact()
    elif user_input == 3:
        add_contact()
    elif user_input == 4:
        delete_contact()
    else: 
        print('Not a valid choice')
  
# Function to see all contacts
    def all_contacts():
        contacts = Contact.select()
        if contacts.count() > 0:
            print('All Contacts:')
            for contact in contacts:
                print(f'{contact.first_name} {contact.last_name} Nickname: {contact.nickname}, Phone: {contact.phone_num}, Email: {contact.email}')
        else:
            print("No contacts in the contact book.")

    # Function to search a contact by the first name
    def search_contact():
    
    # Function to add a new contact
    def add_contact():
    
    # Function to update an existing contact
    def update_contact():
    
    # Function to delete a contact
    def delete_contact():
    

contact_book()


# Define the command line arguments
parser = argparse.ArgumentParser(description="Contact Book")
subparsers = parser.add_subparsers(dest="command")

# Create sub-parser for 'all contacts' command
list_parser = subparsers.add_parser('list', help='List all contacts')
list_parser.set_defaults(func=all_contacts)

# Create sub-parser for 'search' command
find_parser = subparsers.add_parser('find', help='Find a contact by first name')
find_parser.add_argument('first_name', type=str, help='First name')
find_parser.set_defaults(func=search_contact)

# Create sub-parser for 'create' command
create_parser = subparsers.add_parser('create', help='Create a new contact')
create_parser.add_argument('first_name', type=str, help='First name')
create_parser.add_argument('last_name', type=str, help='Last name')
create_parser.add_argument('nickname', type=str, help='Nickname')
create_parser.add_argument('phone_num', type=int, help='Phone number')
create_parser.add_argument('email', type=str, help='Email')
create_parser.set_defaults(func=add_contact)

# Update sub-parser for 'update' command
update_parser = subparsers.add_parser('update', help='Update a contact')
update_parser.add_argument('first_name', type=str, help='First name of the contact to be updated')
update_parser.add_argument('last', type=str, help='Last name of the contact to be updated')
update_parser.add_argument('nickname', type=str, help='Nickname of the contact to be updated')
update_parser.add_argument('phone_num', type=int, help='Phone number of the contact to be updated')
update_parser.add_argument('email', type=str, help='Email of the contact to be updated')
update_parser.set_defaults(func=update_contact)


# Parse the command line arguments
args = parser.parse_args()

# Call the appropriate function based on the command
if args.command:
    args.func(args)
else:
    parser.print_help()
