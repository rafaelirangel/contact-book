## About
This is a Contact Book CLI application. The application allows the user to create, read, update and delete contacts from a locally run PostgreSQL db.

### There are five actions users can perform 
- create_contact
- list_all_contacts
- list_one_contact
- update_contact
- delete_contact


## Set the database on postgres
```
    -> Open your terminal and run
        $ psql -d postgres

    -> Create a new database with name of 'contacts'
        # create database contacts;

    -> Connect to the database you created
        # \c contacts

    -> View database command
        -> Show all database
            # \l      

        -> Select a specif table
           # \d contactbook

        -> Select all records in the 'contactbook' table 
           # SELECT * FROM contactbook;
```


## Intallation 
1. **Clone the repo and change into the new directory.** 
```
    -> Git clone 
        $ git clone https://github.com/rafaelirangel/contact-book.git
        $ cd contact-book
```
2. **Install dependencies**
```
    $ pipenv install peewee psycopg2-binary autopep8  

    -> Start the shell
        $ pipenv shell

    -> Run the command bwlow to interact with the shell
        $ python3 main.py
```

## Technologies
![PYTHON badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![GIT badge](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![POSTGRESQL badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)  
- PeeWee