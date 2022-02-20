import sqlite3
import os

class create_database:
    def __init__(self):
        pass

    def dbcreate(self):
        filepath = os.getcwd()
        filepath += "/contact_book"
        if not os.path.exists(filepath):
            connect = sqlite3.connect('contact_book')
            cursor = connect.cursor()

            cursor.execute(""" CREATE TABLE contacts (
                id_num integer primary key,
                first_name text,
                last_name text,
                "contact_num" text,
                email_id text)
            """)

            connect.commit()
            connect.close()
