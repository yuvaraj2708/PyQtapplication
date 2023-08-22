# import sqlite3

# # Connect to or create the database
# connection = sqlite3.connect("user_database.db")
# cursor = connection.cursor()

# # Create the users table if it doesn't exist
# create_table_query = '''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     );
# '''

# cursor.execute(create_table_query)
# connection.commit()

# # Insert admin user
# admin_username = "admin"
# admin_password = "admin"
# insert_admin_query = '''
#     INSERT INTO users (username, password) VALUES (?, ?);
# '''
# cursor.execute(insert_admin_query, (admin_username, admin_password))
# connection.commit()

# # Close the connection
# connection.close()

# print("Database tables created and admin user added successfully.")


# #patient registration
import sqlite3

# Connect to or create the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the patients table if it doesn't exist
create_patients_table_query = '''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uhid TEXT NOT NULL UNIQUE,
        title TEXT NOT NULL,
        patientname TEXT NOT NULL,
        dob DATE NOT NULL,
        age TEXT NOT NULL,
        gender TEXT NOT NULL,
        mobile TEXT NOT NULL,
        email TEXT NOT NULL
    );
'''

cursor.execute(create_patients_table_query)
connection.commit()

# Close the connection
connection.close()

print("Patients table created successfully.")


import sqlite3

# Connect to or create the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the patients table if it doesn't exist
create_tests_table_query = '''
    CREATE TABLE IF NOT EXISTS tests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Testcode TEXT NOT NULL UNIQUE,
        TestName TEXT NOT NULL,
        specimentype TEXT NOT NULL,
        reportingrate TEXT NOT NULL,
        department DATE NOT NULL,
        reportformat TEXT NOT NULL
        
        
        
        
    );
'''

cursor.execute(create_tests_table_query)
connection.commit()

# Close the connection
connection.close()

print("tests table created successfully.")

import sqlite3

# Connect to or create the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the patients table if it doesn't exist
create_refdr_table_query = '''
    CREATE TABLE IF NOT EXISTS refdr (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        DoctorCode TEXT NOT NULL UNIQUE,
        DoctorName TEXT NOT NULL,
        Qualification TEXT NOT NULL,
        Specialisation TEXT NOT NULL,
        Address DATE NOT NULL,
        PINCode TEXT NOT NULL,
        Mobile  TEXT NOT NULL,
        Emailid TEXT NOT NULL
        
        
    );
'''

cursor.execute(create_refdr_table_query)
connection.commit()

# Close the connection
connection.close()

print("refdr table created successfully.")

import sqlite3

conn = sqlite3.connect('patient_data.db')
cursor = conn.cursor()

# Create the Visit table with the foreign key constraint
create_visit_table_query = '''
    CREATE TABLE IF NOT EXISTS visit (
        id INTEGER PRIMARY KEY,
        patient_id TEXT,
        patient_category TEXT,
        ref_dr TEXT,
        selected_test TEXT,
        visitid TEXT,
        date DATE,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    );
'''

cursor.execute(create_visit_table_query)
conn.commit()

# Close the connection
conn.close()

print("Database schema and tables created successfully.")


import sqlite3

conn = sqlite3.connect('patient_data.db')
cursor = conn.cursor()

# Create the Visit table with the foreign key constraint
cursor.execute('''
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY,
        categoryvalue TEXT
        
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("patientcategory table created successfully.")
