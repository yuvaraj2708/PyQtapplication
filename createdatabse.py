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


#patient registration
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

