# import sqlite3

# def create_category_table():
#     conn = sqlite3.connect('patient_data.db')
#     cursor = conn.cursor()
    
#     # Create the category table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS category (
#             categoryvalue TEXT
#         )
#     ''')
    
#     # Commit changes and close the connection
#     conn.commit()
#     conn.close()

# def register_category(category_value):
#     conn = sqlite3.connect('patient_data.db')
#     cursor = conn.cursor()
    
#     # Insert category value into the category table
#     cursor.execute('''
#         INSERT INTO category (categoryvalue) VALUES (?)
#     ''', (category_value,))
    
#     # Commit changes and close the connection
#     conn.commit()
#     conn.close()

# # Create the category table if it doesn't exist
# create_category_table()

# # Register a new category
# category_value = input("Enter the category value: ")
# register_category(category_value)

# print("Category registered successfully.")

# from cx_Freeze import setup, Executable

# base = None

# executables = [Executable("menu.py", base=base, targetName="MenuApp.exe", icon="path/to/your/icon.ico")]

# # Additional files and packages required by your application
# additional_files = ["images/rdpl.png"]  # Add any additional files here
# additional_files = ["images/addvisit.png"]
# additional_files = ["images/aligncneter.png"]
# additional_files = ["images/alignleft.png"]
# additional_files = ["images/alignright.png"]
# additional_files = ["images/bold.png"]
# additional_files = ["images/bullet.png"]
# additional_files = ["images/cam.png"]
# additional_files = ["images/delete.png"]
# additional_files = ["images/edit.png"]
# additional_files = ["images/fontsize.png"]
# additional_files = ["images/image.png"]
# additional_files = ["images/italic.png"]
# additional_files = ["images/number.png"]
# additional_files = ["images/qr.png"]
# additional_files = ["images/redo.png"]
# additional_files = ["images/table.png"]
# additional_files = ["images/undo.png"]



# additional_modules = []  # Add any additional modules here

# setup(
#     name="MenuApp",
#     version="1.0",
#     description="My Menu Application",
#     options={
#         "build_exe": {
#             "include_files": additional_files,
#             "packages": additional_modules,
#         }
#     },
#     executables=executables
# )

import sys
from cx_Freeze import setup, Executable
from PyQt5.Qt import QApplication, QMainWindow, QPushButton

# Include any additional PyQt5 modules your app uses
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets



# Your PyQt application script
script = 'menu.py'

# List of PNG files to include
png_files = [
    'images/addvisit.png',
    'images/aligncenter.png',
    'images/alignleft.png',
    'images/alignright.png',
    'images/barcode.png',
    'images/bold.png',
    'images/bullet.png',
    'images/cam.png',
    'images/dcm.png',
    'images/delete.png',
    'images/edit.png',
    'images/edit.png',
    'images/image.png',
    'images/italic.png',
    'images/number.png',
    'images/print.png',
    'images/qr.png',
    'images/rdpl.png',
    'images/redo.png',
    'images/report.png',
    'images/table.png',
    'images/undo.png',
    'images/view.png',
    
    
    # Add more PNG files as needed
]

# Create the executable
executables = [Executable(script)]

# Additional options and include files if needed
options = {
    'build_exe': {
        'include_files': png_files,  # Include all PNG files
        'packages': ['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets'],
        'include_msvcr': True,
        'excludes': ['tkinter'],
        'optimize': 2,  # Use optimization level 2
    }
}

# Create the setup
setup(
    name='Ekon',
    version='1.0',
    description='Developed by Raddream',
    executables=executables,
    options=options
)
