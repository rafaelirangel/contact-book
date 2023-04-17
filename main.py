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
     
    create = True
    while create:
        new_first_name = input('What is the First Name? ')
        new_last_name = input('What is the Last Name? ')
        new_email = input('Enter an email address: ')
        new_phone = int(input('Enter a phone number: '))
        new_contact = ContactBook(
            first_name=new_first_name, 
            last_name=new_last_name, 
            email=new_email, 
            phone=new_phone)
        new_contact.save()
        
        print('Would you like to add another contact?(yes / no) ')
        user_input = str(input())
        if user_input.lower == 'yes':
            create = True
        else:
            create = False
            break

#List all contacts
def list_all_contacts():
    list_all = ContactBook.select()
    print('All contacts: ')
    for contacts in list_all:
        print(f'First Name: {contacts.first_name}\nLast Name: {contacts.last_name}\nPhone: {contacts.phone_num}\n Email: {contacts.email}')


def start_contacts_book():
    while True:
        print('''Chose one of the following options:
            1. Create a Contact
            2. List All Contacts
            3. Exit
            ''')
        choice = input('Enter your choice --> ')
        if choice == '1':
            create_contact()
        elif choice == '2':
            list_all_contacts()
        elif choice == '3':
            print('Exiting ...')
            break
        else: 
            print('Not a valid choice, please try again!') 
            
start_contacts_book()