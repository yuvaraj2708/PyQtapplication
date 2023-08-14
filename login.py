import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFormLayout, QComboBox, QDateEdit, QMessageBox, QMenuBar, QAction

class RegistrationPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Registration")
        self.setGeometry(100, 100, 500, 400)  # Set window position and size

        # Apply styles
        self.setStyleSheet("background-color: #f2f2f2;")  # Set background color

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
        self.register_button.setStyleSheet("background-color: #4CAF50; color: white;")  # Style the button

        self.setup_ui()

    def setup_ui(self):
        # Create layout for the first row (UHID, Title, Gender)
        first_row_layout = QHBoxLayout()
        first_row_layout.addWidget(self.uhid_label)
        first_row_layout.addWidget(self.uhid_input)
        first_row_layout.addWidget(self.title_label)
        first_row_layout.addWidget(self.title_combobox)
        first_row_layout.addWidget(self.gender_label)
        first_row_layout.addWidget(self.gender_combobox)

        # Create layout for the second row (Patient Name, DOB, Age)
        second_row_layout = QHBoxLayout()
        second_row_layout.addWidget(self.name_label)
        second_row_layout.addWidget(self.name_input)
        second_row_layout.addWidget(self.dob_label)
        second_row_layout.addWidget(self.dob_input)
        second_row_layout.addWidget(self.age_label)
        second_row_layout.addWidget(self.age_input)

        # Create layout for the subsequent rows
        third_rows_layout = QFormLayout()
        third_rows_layout.addWidget(self.name_label)
        third_rows_layout.addWidget(self.email_input)
        third_rows_layout.addWidget(self.mobile_label)
        third_rows_layout.addWidget(self.mobile_input)

        # Combine layouts into the main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(first_row_layout)
        main_layout.addLayout(second_row_layout)
        main_layout.addLayout(third_rows_layout)
        main_layout.addWidget(self.register_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_menu(self):
        self.menu_bar = QMenuBar(self)

        file_menu = self.menu_bar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

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
