from peewee import *

db = PostgresqlDatabase(
    'contactsbook',
    user='',
    password='',
    host='localhost',
    port=5432
)

db.connect()
