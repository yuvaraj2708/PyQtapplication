import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout, QComboBox, QDateEdit, QMessageBox

class RegistrationPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Registration")

        # Create database connection
        self.connection = sqlite3.connect("user_database.db")
        self.cursor = self.connection.cursor()

        # Create UI elements
        self.uhid_label = QLabel("UHID:")
        self.uhid_input = QLineEdit()

        self.title_label = QLabel("Title:")
        self.title_combobox = QComboBox()
        self.title_combobox.addItems(["Mr.", "Mrs.", "Miss", "Dr."])

        self.gender_label = QLabel("Gender:")
        self.gender_combobox = QComboBox()
        self.gender_combobox.addItems(["Male", "Female", "Other"])

        self.name_label = QLabel("Patient Name:")
        self.name_input = QLineEdit()

        self.dob_label = QLabel("Date of Birth:")
        self.dob_input = QDateEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        self.email_label = QLabel("Email ID:")
        self.email_input = QLineEdit()

        self.mobile_label = QLabel("Mobile:")
        self.mobile_input = QLineEdit()

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register_patient)

        # Create layout and add widgets
        layout = QFormLayout()
        layout.addRow(self.uhid_label, self.uhid_input)
        layout.addRow(self.title_label, self.title_combobox)
        layout.addRow(self.gender_label, self.gender_combobox)
        layout.addRow(self.name_label, self.name_input)
        layout.addRow(self.dob_label, self.dob_input)
        layout.addRow(self.age_label, self.age_input)
        layout.addRow(self.email_label, self.email_input)
        layout.addRow(self.mobile_label, self.mobile_input)
        layout.addRow(self.register_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def register_patient(self):
        uhid = self.uhid_input.text()
        title = self.title_combobox.currentText()
        gender = self.gender_combobox.currentText()
        name = self.name_input.text()
        dob = self.dob_input.date().toString("yyyy-MM-dd")
        age = self.age_input.text()
        email = self.email_input.text()
        mobile = self.mobile_input.text()

        # Insert patient details into the database
        insert_patient_query = '''
            INSERT INTO patients (uhid, title, gender, name, dob, age, email, mobile)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        '''
        try:
            self.cursor.execute(insert_patient_query, (uhid, title, gender, name, dob, age, email, mobile))
            self.connection.commit()
            QMessageBox.information(self, "Success", "Patient registered successfully.")
            self.clear_fields()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Failed to register patient. Error: " + str(e))

    def clear_fields(self):
        self.uhid_input.clear()
        self.title_combobox.setCurrentIndex(0)
        self.gender_combobox.setCurrentIndex(0)
        self.name_input.clear()
        self.dob_input.setDate(QDateEdit.currentDate())
        self.age_input.clear()
        self.email_input.clear()
        self.mobile_input.clear()

    def closeEvent(self, event):
        self.connection.close()

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")

        # Create database connection
        self.connection = sqlite3.connect("user_database.db")
        self.cursor = self.connection.cursor()

        # Create UI elements
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Check credentials in the database
        query = "SELECT * FROM users WHERE username=? AND password=?"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()

        if user:
            self.welcome_page = RegistrationPage()
            self.welcome_page.show()
            self.hide()  # Hide the login page
        else:
            print("Login failed")

    def closeEvent(self, event):
        self.connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec_())
