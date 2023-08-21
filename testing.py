# import sys
# import sqlite3
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QListWidget, QPushButton

# class DatabaseHandler:
#     def __init__(self, db_name):
#         self.db_name = db_name
#         self.conn = None
#         self.cursor = None
    
#     def connect(self):
#         self.conn = sqlite3.connect(self.db_name)
#         self.cursor = self.conn.cursor()
    
#     def disconnect(self):
#         if self.conn:
#             self.conn.close()
    
#     def fetch_all_patients(self):
#         self.connect()
#         query = "SELECT * FROM category"
#         self.cursor.execute(query)
#         all_patients = self.cursor.fetchall()
#         self.disconnect()
#         return all_patients

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("All Patients' Details")
#         self.setGeometry(100, 100, 600, 400)

#         self.db_handler = DatabaseHandler('patient_data.db')

#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)

#         self.layout = QVBoxLayout()
#         self.central_widget.setLayout(self.layout)

#         self.patient_list = QListWidget(self)
#         self.layout.addWidget(self.patient_list)

#         self.refresh_button = QPushButton("Refresh", self)
#         self.refresh_button.clicked.connect(self.show_patient_details)
#         self.layout.addWidget(self.refresh_button)

#         self.show_patient_details()

#     def show_patient_details(self):
#         self.patient_list.clear()
#         all_patients = self.db_handler.fetch_all_patients()
        
#         if all_patients:
#             for patient in all_patients:
#                 self.patient_list.addItem("Patient Data: " + str(patient))
#         else:
#             self.patient_list.addItem("No patients found.")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_win = MainWindow()
#     main_win.show()
#     sys.exit(app.exec_())


import sqlite3

def view_visit_table(database_file):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Execute a SELECT query to fetch all records from the "visit" table
    cursor.execute("SELECT * FROM visit")
    rows = cursor.fetchall()

    # Display the fetched data
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

# Replace 'your_database.db' with the actual name of your SQLite database file
database_file = 'patient_data.db'
view_visit_table(database_file)
