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
    id=AutoField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    phone = IntegerField()


# Remove table if they exist then Create table from scratch
# db.drop_tables([ContactBook])
db.create_tables([ContactBook])

#Create a new contact
def create_contact():
     
    create = True
    while create:
        first_name = input('What is the First Name? ')
        last_name = input('What is the Last Name? ')
        email = input('Enter an email address: ')
        phone = int(input('Enter a phone number: '))
        new_contact = ContactBook(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone=phone)
        new_contact.save()
        print('----------////----------')
        print('Would you like to add another contact?(yes / no) ')
        user_input = str(input())
        if user_input.lower() == 'yes':
            create = True
        else:
            create = False
            break


#List all contacts
def list_all_contacts():
    list_all = ContactBook.select()
    print('All contacts: ')
    for contacts in list_all:
        print('----------////----------')
        print(
            f'First Name: {contacts.first_name}\nLast Name: {contacts.last_name}\nEmail: {contacts.email}\nPhone: {contacts.phone}\n')


# List a contact by the First Name
def list_one_contact():
    search_contact = input('Enter the first name: ').lower()
    list_one = ContactBook.select().where(ContactBook.first_name == search_contact)
    if list_one:
        for contact in list_one:
            print('----------////----------')
            print(
                f'First Name: {contact.first_name}\nLast Name: {contact.last_name}\nEmail: {contact.email}\nPhone Number: {contact.phone}\n')
    else:
        print('No contact found with the given first name.')

#Update a contact by ID 
def update_contact():
    
    update = True
    while update:
        
        contact_id = input('Enter contact ID to uptade a contact: ')
        
        get_contact = ContactBook.select().where(ContactBook.id == contact_id) 
        for contact in get_contact:
            print('----------////----------')
            print(
                f'This is the contact you want to update:\nFirst Name: {contact.first_name}\nLast Name: {contact.last_name}\nEmail: {contact.email}\nPhone Number: {contact.phone}')
            print('----------////----------')
            print('What would you like to update? First Name(f), Last Name(l), Email(e), Phone(p), All(a), or Quit(q)...')
            user_input = str(input(' ==> '))
            
            update_contact = ContactBook.get(ContactBook.id == contact_id)
            
            if user_input.lower() == 'f':
                new_first_name = str(input('Enter the first name: '))
                update_contact.first_name = new_first_name
                update_contact.save()
            elif user_input.lower() == 'l':
                new_last_name = str(input('Enter the last name: '))
                update_contact.last_name = new_last_name
                update_contact.save()
            elif user_input.lower() == 'e':
                new_email = str(input('Enter the email address: '))
                update_contact.email = new_email
                update_contact.save()    
            elif user_input.lower() == 'p':
                new_phone_number = str(input('Enter the phone number: '))
                update_contact.phone = new_phone_number
                update_contact.save()
            elif user_input.lower() == 'a':
                new_first_name = str(input('Enter the first name: '))
                new_last_name = str(input('Enter the last name: '))
                new_email = str(input('Enter the email address: '))
                new_phone_number = str(input('Enter the phone number: '))
                update_contact.first_name = new_first_name
                update_contact.last_name = new_last_name
                update_contact.email = new_email
                update_contact.phone = new_phone_number
                update_contact.save()
            elif user_input.lower() == 'q':
                update = False
                break
            
            else:
                ('Not a valid choice!')
                update = True  
                
# Delete a contact by ID
def delete_contact():
    delete = True
    while delete:
        contact_id = input('Enter contact ID to delete a contact: ')
        get_contact = ContactBook.select().where(ContactBook.id == contact_id)
        
        for contact in get_contact:
            print('----------////----------')
            print('This is the contact you want to delete, are you sure about that? (yes/no)')
            print('----------////----------')
            print(f'First Name: {contact.first_name}\nLast Name: {contact.last_name}\nEmail: {contact.email}\nPhone Number: {contact.phone}\n')
            user_input = str(input('==> ')).lower()
            
            get_contact = ContactBook.get(ContactBook.id == contact_id)
            
            if user_input.lower() == 'yes':
                get_contact.delete_instance()
                print('Your contact was deleted! ')
                print('----------////----------')
                new_delete = str(input('Would you like to delete another contact? (yes/no) ')).lower()
                if new_delete == 'yes':
                    delete = True
                else:
                    delete = False
                    break           
            else:
                delete = False
                break            
        
    
        
#Main Function
def start_contacts_book():
    while True:
        print('''Chose one of the following options:
            1. Create a Contact
            2. List All Contacts
            3. List one specif Contact
            4. Update a contact
            5. Delete a contact
            6. Exit
            ''')
        choice = input('Enter your choice number: ')
        if choice == '1':
            create_contact()
        elif choice == '2':
            list_all_contacts()
        elif choice == '3':
            list_one_contact()     
        elif choice == '4':
            update_contact()   
        elif choice == '5':
            delete_contact()          
        elif choice == '6':
            print('Exiting ...')
            break
        else: 
            print('Not a valid choice, please try again!') 
            
start_contacts_book()