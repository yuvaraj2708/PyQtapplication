import sqlite3

def create_category_table():
    conn = sqlite3.connect('patient_data.db')
    cursor = conn.cursor()
    
    # Create the category table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category (
            categoryvalue TEXT
        )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

def register_category(category_value):
    conn = sqlite3.connect('patient_data.db')
    cursor = conn.cursor()
    
    # Insert category value into the category table
    cursor.execute('''
        INSERT INTO category (categoryvalue) VALUES (?)
    ''', (category_value,))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Create the category table if it doesn't exist
create_category_table()

# Register a new category
category_value = input("Enter the category value: ")
register_category(category_value)

print("Category registered successfully.")
