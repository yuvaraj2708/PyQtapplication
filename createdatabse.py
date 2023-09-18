import sqlite3

# Connect to or create the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the patients table if it doesn't exist
create_patients_table_query = '''
    CREATE TABLE IF NOT EXISTS patients (
        uhid TEXT NOT NULL UNIQUE,
        date DATE NOT NULL,
        title TEXT NOT NULL,
        patientname TEXT NOT NULL,
        dob DATE NOT NULL,
        age TEXT NOT NULL,
        gender TEXT NOT NULL,
        mobile TEXT NOT NULL,
        email TEXT NOT NULL,
        refdr TEXT NOT NULL,
        selected_test TEXT NOT NULL,
        accession TEXT NOT NULL
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
        DoctorCode TEXT NOT NULL UNIQUE,
        DoctorName TEXT NOT NULL,
        Qualification TEXT NOT NULL,
        Specialisation TEXT NOT NULL,
        Address DATE NOT NULL,
        PINCode TEXT NOT NULL,
        Mobile  TEXT NOT NULL,
        Emailid TEXT NOT NULL,
        date DATE NOT NULL
        
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
        patient_id INTEGER,  -- Change this to INTEGER as per the ForeignKey relation
        ref_dr TEXT,
        selected_test TEXT,
        visitid TEXT,
        date DATE,
        FOREIGN KEY (patient_id) REFERENCES patient(id)  -- Use the correct model name and field name
        FOREIGN KEY (selected_test) REFERENCES visit_tests(id)  -- Use the correct model name and field name
    );
'''

cursor.execute(create_visit_table_query)
conn.commit()

# Close the connection
conn.close()

print("Database schema and tables created successfully.")

# import sqlite3

# conn = sqlite3.connect('patient_data.db')
# cursor = conn.cursor()

# # Create the Visit table with the foreign key constraint
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS category (
#         categoryvalue TEXT
        
#     )
# ''')

# # Commit changes and close the connection
# conn.commit()
# conn.close()

# print("patientcategory table created successfully.")


import sqlite3

# Connect to the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the report_templates table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reporttemplates (
        code TEXT,
        name TEXT,
        template TEXT
    )
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print("report_templates table created successfully.")


import sqlite3

# Connect to the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the device table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS device (
        DeviceID TEXT NOT NULL,
        ClientID TEXT NOT NULL,
        ClientName TEXT NOT NULL,
        Address TEXT NOT NULL,
        MobileNo TEXT NOT NULL,
        EmailID TEXT NOT NULL,
        clientidstatus INTEGER DEFAULT 0,
        Deviceidstatus INTEGER DEFAULT 0,
        Createdon timestamp  NOT NULL
    )
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print("device table created successfully.")


import sqlite3

# Connect to the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the visit_tests table
cursor.execute('''
CREATE TABLE IF NOT EXISTS visit_tests (
    visit_id INTEGER,
    test_code TEXT,
    FOREIGN KEY (visit_id) REFERENCES visit(id)
   
);
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print("visit_tests table created successfully.")


import sqlite3

# Connect to the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the visit_tests table
cursor.execute('''
CREATE TABLE patient_reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    report_template TEXT NOT NULL,
    pathologist TEXT NOT NULL,
    report_content TEXT NOT NULL,
    report_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print("patient_reports table created successfully.")


import sqlite3

# Connect to or create the database
connection = sqlite3.connect("patient_data.db")
cursor = connection.cursor()

# Create the patients table if it doesn't exist
create_pathologist_table_query = '''
    CREATE TABLE IF NOT EXISTS pathologist (
        DoctorCode TEXT NOT NULL UNIQUE,
        DoctorName TEXT NOT NULL,
        Qualification TEXT NOT NULL,
        Specialisation TEXT NOT NULL,
        Address DATE NOT NULL,
        PINCode TEXT NOT NULL,
        Mobile TEXT NOT NULL,
        Emailid TEXT NOT NULL,
        date DATE NOT NULL,
        Signature BLOB  -- Add a BLOB (Binary Large Object) column for the signature image
    );
'''

cursor.execute(create_pathologist_table_query)
connection.commit()

# Close the connection
connection.close()

print("pathologist table created successfully.")
