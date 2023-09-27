from PyQt5 import QtCore, QtGui, QtWidgets
from patientregister import Ui_addpatientForm
from patientdetails import Ui_patientForm 
from refdrmaster import Ui_refdrmasterForm 
from testmaster import Ui_testForm
from reportformat import Ui_reportForm
import sqlite3
from resulttemplate import Ui_resulttemplateForm
from pathologistmaster import Ui_pathologistmasterForm
import requests
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

#device register
class Ui_deviceForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 889)
        # Form.setMaximumSize(QtCore.QSize(811, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: #ffffff;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 30, 211, 35))
        self.label.setMinimumSize(QtCore.QSize(5, 5))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setSizeIncrement(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: #181C32;")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 90, 971, 481))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(550, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(390, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton.setEnabled(False)  # Initialize the button as disabled
        self.pushButton.clicked.connect(self.save_button_clicked)  # Connect the button to a save function
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #0DBCC0;\n"
"    border: 0;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    border-radius: 4px;\n"
"color: #ffffff;\n"
"border: 0;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: #089598;\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(100, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(290, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setGeometry(QtCore.QRect(450, 230, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_10.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_10.setFrame(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(450, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #0DBCC0;\n"
"    border: 0;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    border-radius: 4px;\n"
"color: #ffffff;\n"
"border: 0;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: #089598;\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(550, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(100, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16.setGeometry(QtCore.QRect(100, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_16.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_16.setFrame(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setGeometry(QtCore.QRect(100, 150, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_18.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_18.setFrame(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_15.setGeometry(QtCore.QRect(290, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_15.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_15.setFrame(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setGeometry(QtCore.QRect(100, 230, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_12.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_12.setFrame(True)
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.lineEdit_16.textChanged.connect(self.validate_required_fields)
        self.lineEdit_15.textChanged.connect(self.validate_required_fields)
        self.lineEdit_12.textChanged.connect(self.validate_required_fields)
        self.lineEdit_18.textChanged.connect(self.validate_required_fields)
        self.lineEdit_10.textChanged.connect(self.validate_required_fields)
    
    def save_button_clicked(self):
        # Handle the save button click event here
        # This function will only be called when all required fields are filled in
        pass
        
    def validate_required_fields(self):
        # Check if all required fields are filled in
        device_id = self.lineEdit_16.text()
        client_id = self.lineEdit_15.text()
        address = self.lineEdit_12.text()
        client_name = self.lineEdit_18.text()
        mobile_no = self.lineEdit_10.text()

        if device_id and client_id and address and client_name and mobile_no:
            self.pushButton.setEnabled(True)  # Enable the "Save" button
        else:
            self.pushButton.setEnabled(False)  # Disable the "Save" button 
            
               
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Register Device"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label_4.setText(_translate("Form", "Address"))
        self.label_2.setText(_translate("Form", "Device ID"))
        self.label_3.setText(_translate("Form", "Client ID"))
        self.label_8.setText(_translate("Form", "Email ID"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.label_5.setText(_translate("Form", "Client Name"))
        self.label_6.setText(_translate("Form", "Mobile No"))

class DeviceRegistrationForm(QtWidgets.QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_deviceForm()
        self.ui.setupUi(self)

        # Connect the Tab key press event to the check_availability method
        self.ui.lineEdit_16.installEventFilter(self)
        self.ui.lineEdit_15.installEventFilter(self)

        # Connect the "Register" button click event to register_device method
        self.ui.pushButton.clicked.connect(self.register_device)

        # Check if the device is already registered
        if self.is_device_registered():
            # Device is already registered, show the login page directly
            self.show_login_page()
        else:
            # Device is not registered, show the device registration form
            self.show_device_registration_page()
            
    def is_device_registered(self):
        # Check if there's existing data in the device table
        connection = sqlite3.connect("patient_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM device")
        count = cursor.fetchone()[0]
        connection.close()
        return count > 0
    
    def check_existing_data(self, device_id, client_id):
       # Check if there's existing data for the given device_id and client_id
       connection = sqlite3.connect("patient_data.db")
       cursor = connection.cursor()
       cursor.execute("SELECT COUNT(*) FROM device WHERE DeviceID = ? AND ClientID = ?", (device_id, client_id))
       count = cursor.fetchone()[0]
       connection.close()
       return count > 0
       
            
    def eventFilter(self, obj, event):
      if event.type() == QtCore.QEvent.KeyPress and event.key() == Qt.Key_Tab:
          if obj == self.ui.lineEdit_16 or obj == self.ui.lineEdit_15:
              # Get the deviceid and clientid from the UI
              deviceid = self.ui.lineEdit_16.text()
              clientid = self.ui.lineEdit_15.text()
                         
              # Make an API call to check if the deviceid and clientid are available
              api_url = f'http://127.0.0.1:8000/register_client/?clientid={clientid}&deviceid={deviceid}'  # Replace with your API URL
              try:
                 response = requests.get(api_url)
                 if response.status_code == 200:
                     response_data = response.json()
                     if 'clientid' in response_data and 'deviceid' in response_data:
                         if response_data['clientid'] == clientid and response_data['deviceid'] == deviceid:
                            self.ui.lineEdit_6.setText(response_data['ClientName'])
                            self.ui.lineEdit_18.setText(response_data['Address'])
                            self.ui.lineEdit_12.setText(response_data['MobileNo'])
                            self.ui.lineEdit_10.setText(response_data['EmailID'])
        
                            # self.show_message("Availability", "Device found")
                                                                                                                    
                         else:
                             self.show_message("Availability", "Device not found")
                     else:
                         self.show_message("Error", "Response data does not contain 'clientid' and 'deviceid'.")
                 else:
                     self.show_message("API Request Failed", f"Status Code: {response.status_code}\n{response.text}")
 
              except requests.exceptions.RequestException as e:
                  self.show_message("Error", f'Error: {e}')
              
                  
              # Return True to indicate that the event was handled
              return True

      # If the event was not handled, return False
      return False

                
    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()
        
    def register_device(self):
      device_id = self.ui.lineEdit_16.text()
      client_id = self.ui.lineEdit_15.text()
      address = self.ui.lineEdit_18.text()
      client_name = self.ui.lineEdit_6.text()
      mobile_no = self.ui.lineEdit_12.text()
      email_id = self.ui.lineEdit_10.text()

      connection = sqlite3.connect("patient_data.db")
      cursor = connection.cursor()

      # Check if both device_id and client_id are already registered
      cursor.execute("SELECT DeviceID FROM device WHERE DeviceID = ? AND ClientID = ?", (device_id, client_id))
      existing_device = cursor.fetchone()

      if existing_device:
          # Both device_id and client_id are already registered, show a message and redirect to the login page
          print("Device and client are already registered.")
          connection.close()

          # Optionally, you can show a QMessageBox here to inform the user

          # Redirect to the login page
          self.show_login_page()

          return  # Return without further execution of the code

      # Insert the device information into the database
      cursor.execute('''
          INSERT INTO device (DeviceID, ClientName, ClientID, Address, MobileNo, EmailID, clientidstatus, Deviceidstatus, Createdon)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
      ''', (device_id, client_name, client_id, address, mobile_no, email_id, 1, 'status_value', 'timestamp_value'))

      # Commit changes and close the connection
      connection.commit()
      connection.close()

      print("Device registered successfully.")

      # Close the current registration form
      self.close()

      # Show the login form
      self.show_login_page()

    def show_login_page(self):
        # Create an instance of the LoginDialog class
        self.login_form = LoginDialog()
        self.login_form.show()

    def show_device_registration_page(self):
        # Show the device registration form
        self.show()


   

#loginpage

class Ui_loginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 889)
        Form.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)  # Add window flags
        # Form.setMaximumSize(QtCore.QSize(811, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: #ffffff;\n"
"border-color: rgb(52, 223, 203);")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(380, 230, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_18.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_18.setFrame(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 280, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 200, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 370, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #0DBCC0;\n"
"    border: 0;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    border-radius: 4px;\n"
"color: #ffffff;\n"
"border: 0;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: #089598;\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(450, 90, 81, 35))
        self.label.setMinimumSize(QtCore.QSize(5, 5))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setSizeIncrement(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: #181C32;")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "Username"))
        self.pushButton_2.setText(_translate("Form", "Login"))
        # self.label.setText(_translate("Form", "Login"))

class LoginDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginForm()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.login)
        
        # Set the echo mode for the password field to Password (dots)
        self.ui.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        
        # Hide the password visibility toggle button
        self.ui.lineEdit_6.setClearButtonEnabled(False)

    def login(self):
        username = self.ui.lineEdit_18.text()
        password = self.ui.lineEdit_6.text()

        # Add your login validation logic here
        if username == "admin" and password == "admin":
            QtWidgets.QMessageBox.information(self, "Login Successful", "Welcome!")
            self.accept()  # Close the dialog and return QDialog.Accepted
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 889)
        # self.showMaximized()
        # MainWindow.showFullScreen()
        # MainWindow.setMaximumSize(QtCore.QSize(851, 17777415))
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menusdsa = QtWidgets.QMenu(self.menubar)
        self.menusdsa.setObjectName("menusdsa")
        self.menuPatientRegister = QtWidgets.QMenu(self.menubar)
        self.menuPatientRegister.setObjectName("menuPatientRegister")
        self.menuVisit_Summary = QtWidgets.QMenu(self.menubar)
        self.menuVisit_Summary.setObjectName("menuscan_Summary")
        self.menuscan_Summary = QtWidgets.QMenu(self.menubar)
        self.menuscan_Summary.setObjectName("menuscan_Summary")
        self.menuMaster = QtWidgets.QMenu(self.menubar)
        self.menuMaster.setObjectName("menuMaster")
        self.menuLogout = QtWidgets.QMenu(self.menubar)
        self.menuLogout.setObjectName("menuLogout")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuSettings.addAction(self.actionLogout)  # Add the action to the Settings menu

    
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionAdd_Patient = QtWidgets.QAction(MainWindow)
        self.actionAdd_Patient.setObjectName("actionAdd_Patient")
        self.actionRefDr_Master = QtWidgets.QAction(MainWindow)
        self.actionRefDr_Master.setObjectName("actionRefDr_Master")
        self.actionTest_Master = QtWidgets.QAction(MainWindow)
        self.actionTest_Master.setObjectName("actionTest_Master")
        self.actionReport_Format = QtWidgets.QAction(MainWindow)
        self.actionReport_Format.setObjectName("actionReport_Format")
        self.actionpathologist_Master = QtWidgets.QAction(MainWindow)
        self.actionpathologist_Master.setObjectName("actionReport_Format")
        
       
        self.menuPatientRegister.addAction(self.actionAdd_Patient)
       
        self.menuMaster.addAction(self.actionRefDr_Master)
        self.menuMaster.addAction(self.actionTest_Master)
        self.menuMaster.addAction(self.actionReport_Format)
        self.menuMaster.addAction(self.actionpathologist_Master)
        self.menubar.addAction(self.menusdsa.menuAction())
        self.menubar.addAction(self.menuPatientRegister.menuAction())
        # self.menubar.addAction(self.menuVisit_Summary.menuAction())
        # self.menubar.addAction(self.menuscan_Summary.menuAction())
        self.menubar.addAction(self.menuMaster.menuAction())
        self.menubar.addAction(self.menuLogout.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    actionLogout = QtWidgets.QAction()
    actionLogout.setObjectName("actionLogout")
    actionLogout.setText("Logout")  # Set the text for the logout action
    actionLogout.triggered.connect(QtCore.QCoreApplication.quit)  
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ekon"))
        # self.menusdsa.setTitle(_translate("MainWindow", "Dasboard"))
        self.menuPatientRegister.setTitle(_translate("MainWindow", "Front Desk"))
        # self.actionregistrationsummary.setText(_translate("MainWindow", "Registration Summary"))
        self.menuscan_Summary.setTitle(_translate("MainWindow", "Scan"))
        self.menuMaster.setTitle(_translate("MainWindow", "Master"))
        self.menuLogout.setTitle(_translate("MainWindow", "Settings"))
        self.menuSettings.setTitle(_translate("MainWindow", "Logout"))
        # self.actionPatientregister.setText(_translate("MainWindow", "Add Patient"))
        self.actionAdd_Patient.setText(_translate("MainWindow", "Registration Summary"))
        # self.actionscansummary.setText(_translate("MainWindow", "Scan Summary"))
        self.actionRefDr_Master.setText(_translate("MainWindow", "RefDr Master"))
        self.actionTest_Master.setText(_translate("MainWindow", "Test Master"))
        self.actionReport_Format.setText(_translate("MainWindow", "Report Format"))
        self.actionpathologist_Master.setText(_translate("MainWindow", "Pathologist Master"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
   
        
        self.patient_register_frame = QtWidgets.QFrame()
        self.patient_register_ui = Ui_addpatientForm()
        self.patient_register_ui.setupUi(self.patient_register_frame)

        self.patient_master_frame = QtWidgets.QFrame()
        self.patient_master_ui = Ui_patientForm()# patient master
        self.patient_master_ui.setupUi(self.patient_master_frame)
    
        self.add_refdr_frame = QtWidgets.QFrame()
        self.add_refdr_ui = Ui_refdrmasterForm()# refdr master
        self.add_refdr_ui.setupUi(self.add_refdr_frame)
        
        self.add_testmaster_frame = QtWidgets.QFrame()
        self.add_testmaster_ui = Ui_testForm()# Test master
        self.add_testmaster_ui.setupUi(self.add_testmaster_frame)
        
        self.reportformat_frame = QtWidgets.QFrame()
        self.reportformat_ui = Ui_resulttemplateForm()# report format
        self.reportformat_ui.setupUi(self.reportformat_frame)
        
        self.pathologist_frame = QtWidgets.QFrame()
        self.pathologist_ui = Ui_pathologistmasterForm()# category
        self.pathologist_ui.setupUi(self.pathologist_frame)
        
        
        # self.ui.actionPatientregister.triggered.connect(self.show_patient_register_frame)
        self.ui.actionAdd_Patient.triggered.connect(self.show_patient_master_frame)
        self.ui.actionRefDr_Master.triggered.connect(self.show_refdr_frame)
        self.ui.actionTest_Master.triggered.connect(self.show_testmaster_frame) 
        self.ui.actionReport_Format.triggered.connect(self.show_reportformat_frame)
        self.ui.actionpathologist_Master.triggered.connect(self.show_pathologist_frame)
        
        # Create a QStackedWidget to manage the frames
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        
        
        
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.stacked_widget.addWidget(self.ui.centralwidget)
        self.stacked_widget.addWidget(self.patient_register_frame)
        self.stacked_widget.addWidget(self.patient_master_frame)
        self.stacked_widget.addWidget(self.add_refdr_frame)
        self.stacked_widget.addWidget(self.add_testmaster_frame)
        self.stacked_widget.addWidget(self.reportformat_frame)
        self.stacked_widget.addWidget(self.pathologist_frame)
        self.setCentralWidget(self.stacked_widget)
    
        self.show_patient_master_frame()
        self.patient_register_frame = QtWidgets.QFrame()
        self.patient_register_ui = Ui_addpatientForm()  # patient register
        self.patient_register_ui.setupUi(self.patient_register_frame)

 
    def refresh_main_window(self):
       self.stacked_widget.addWidget(self.ui.centralwidget)
       self.stacked_widget.addWidget(self.patient_register_frame)
       self.stacked_widget.addWidget(self.patient_master_frame)
       self.stacked_widget.addWidget(self.add_refdr_frame)
       self.stacked_widget.addWidget(self.add_testmaster_frame)
       self.stacked_widget.addWidget(self.reportformat_frame)
       self.stacked_widget.addWidget(self.category_frame)
       self.setCentralWidget(self.stacked_widget)

       
    
    
    def show_pathologist_frame(self):
        self.stacked_widget.setCurrentWidget(self.pathologist_frame)
    
    def show_patient_register_frame(self):
        self.stacked_widget.setCurrentWidget(self.patient_register_frame)

    def show_patient_master_frame(self):

        # self.patient_master_ui.timer.start()
        self.stacked_widget.setCurrentWidget(self.patient_master_frame)
        
    def show_refdr_frame(self):

        self.add_refdr_ui.lineEdit_25.setText('')

        self.add_refdr_ui.lineEdit_26.setText('')
        # self.add_refdr_ui.lineEdit_25.setText('')
        # self.add_refdr_ui.timer.start()
        self.stacked_widget.setCurrentWidget(self.add_refdr_frame)    

    def show_testmaster_frame(self):
        self.add_testmaster_ui.lineEdit_26.setText('')
        self.add_testmaster_ui.lineEdit_25.setText('')
        # self.add_testmaster_ui.timer.start()
        self.stacked_widget.setCurrentWidget(self.add_testmaster_frame) 
    
    # def show_visitsummary_frame(self):
    #     self.add_visitsummary_ui.lineEdit_25.setText('')

    
    def show_reportformat_frame(self):
         self.reportformat_ui.lineEdit_25.setText('')
         self.reportformat_ui.lineEdit_26.setText('')
        #  self.reportformat_ui.timer.start()
         self.stacked_widget.setCurrentWidget(self.reportformat_frame)     
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Check for existing data in the device table
    connection = sqlite3.connect("patient_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM device")
    count = cursor.fetchone()[0]
    connection.close()

    if count == 0:
        # No existing data, so show the device registration form
        device_registration_form = DeviceRegistrationForm()
        device_registration_form.show()
    else:
        # There is existing data, so show the login dialog
        login_dialog = LoginDialog()
        if login_dialog.exec_() == QtWidgets.QDialog.Accepted:
            # The login was successful, so create and show the main window
            main_window = MainWindow()
            main_window.show()

    sys.exit(app.exec_())