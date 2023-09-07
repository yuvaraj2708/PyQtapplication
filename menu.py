from PyQt5 import QtCore, QtGui, QtWidgets
from patientregister import Ui_addpatientForm
from patientdetails import Ui_patientForm 
from refdrmaster import Ui_refdrmasterForm 
from testmaster import Ui_testForm
from registrationsummary import Ui_visitsummaryForm
from reportformat import Ui_reportForm
from scansummary import Ui_scansummaryForm
import sqlite3


class Ui_deviceForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(811, 588)
        Form.setMaximumSize(QtCore.QSize(811, 16777215))
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
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 80, 251, 31))
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
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(290, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
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
        self.label_4.setGeometry(QtCore.QRect(50, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(350, 230, 351, 31))
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
        self.label_8.setGeometry(QtCore.QRect(350, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 280, 91, 31))
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
        self.label_5.setGeometry(QtCore.QRect(450, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16.setGeometry(QtCore.QRect(50, 80, 121, 31))
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
        self.lineEdit_18.setGeometry(QtCore.QRect(50, 150, 651, 31))
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
        self.lineEdit_15.setGeometry(QtCore.QRect(190, 80, 231, 31))
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
        self.lineEdit_12.setGeometry(QtCore.QRect(50, 230, 231, 31))
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Register Device"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label_4.setText(_translate("Form", "Address"))
        self.label_2.setText(_translate("Form", "Device ID"))
        self.label_3.setText(_translate("Form", "Client Name"))
        self.label_8.setText(_translate("Form", "Email ID"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.label_5.setText(_translate("Form", "PIN Code"))
        self.label_6.setText(_translate("Form", "Mobile No"))

class DeviceRegistrationForm(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_deviceForm()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.register_device)

    def register_device(self):
       device_id = self.ui.lineEdit_16.text()
       client_name = self.ui.lineEdit_15.text()
       address = self.ui.lineEdit_18.text()
       pin_code = self.ui.lineEdit_6.text()
       mobile_no = self.ui.lineEdit_12.text()
       email_id = self.ui.lineEdit_10.text()

       # Verify if the Device ID is correct ('1003')
       if device_id != '1003':
           print("Invalid Device ID. Registration failed.")
           return  # Exit the method if Device ID is invalid

       # Connect to the database
       connection = sqlite3.connect("patient_data.db")
       cursor = connection.cursor()

       # Check if the device is already registered
       cursor.execute("SELECT DeviceID FROM device WHERE DeviceID = ?", (device_id,))
       existing_device = cursor.fetchone()

       if existing_device:
           # Device is already registered, redirect to the login page
           print("Device is already registered.")
       else:
           # Insert the device information into the database
           cursor.execute('''
               INSERT INTO device (DeviceID, ClientName, Address, PINCode, MobileNo, EmailID)
               VALUES (?, ?, ?, ?, ?, ?)
           ''', (device_id, client_name, address, pin_code, mobile_no, email_id))

           # Commit changes and close the connection
           connection.commit()
           connection.close()

           print("Device registered successfully.")

       # Close the current registration form
       self.close()

       # Show the login form
       self.login_form = LoginForm()
       self.login_form.show()






class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(811, 588)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(370, 90, 81, 35))
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
        
        self.centralwidget = QtWidgets.QWidget(LoginForm)
        self.centralwidget.setObjectName("centralwidget")
        LoginForm.setCentralWidget(self.centralwidget)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 81, 20))
        self.label.setObjectName("label")
        
        # self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.usernameLineEdit.setGeometry(QtCore.QRect(100, 80, 201, 31))
        # self.usernameLineEdit.setObjectName("usernameLineEdit")
        
        self.passwordLineEdit = QtWidgets.QLineEdit(LoginForm)
        self.passwordLineEdit.setGeometry(QtCore.QRect(310, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("QLineEdit\n"
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
        self.passwordLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.passwordLineEdit.setFrame(True)
        self.passwordLineEdit.setObjectName("lineEdit_6")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.usernameLineEdit = QtWidgets.QLineEdit(LoginForm)
        self.usernameLineEdit.setGeometry(QtCore.QRect(310, 230, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setStyleSheet("QLineEdit\n"
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
        self.usernameLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.usernameLineEdit.setFrame(True)
        self.usernameLineEdit.setObjectName("lineEdit_18")    
        
        
        self.loginButton = QtWidgets.QPushButton(LoginForm)
        self.loginButton.setGeometry(QtCore.QRect(350, 370, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton\n"
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
        self.loginButton.setObjectName("pushButton_2") 
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(370, 90, 81, 35))
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
       
       
        self.imageLabel = QtWidgets.QLabel(LoginForm)
        self.imageLabel.setGeometry(QtCore.QRect(250, 150, 300, 30))  # Adjust the geometry and size as needed
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        # Load the image and resize it before setting it to the QLabel
        image = QtGui.QPixmap('images/rdpl.png')  # Provide the correct path to your image
        image = image.scaled(self.imageLabel.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.imageLabel.setPixmap(image)
        
        
       
        
        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
    
    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        # self.label.setText(_translate("LoginForm", "Login"))
        self.loginButton.setText(_translate("LoginForm", "Login"))

class LoginForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        
        self.ui.loginButton.clicked.connect(self.check_login)
        
    def check_login(self):
        # Check username and password here
        # For this example, let's assume valid credentials are "username" and "password"
        if self.ui.usernameLineEdit.text() == "" and self.ui.passwordLineEdit.text() == "":
            self.main_window = MainWindow()
            self.close()
            self.main_window.show()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
        
        self.close() 



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 588)
        # self.showMaximized()
        MainWindow.setMaximumSize(QtCore.QSize(851, 17777415))
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

        # Connect the action to the logout method
        self.actionLogout.triggered.connect(MainWindow.logout)  # Connect to MainWindow's logout method

    # Define the actionLogout attribute
    
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        # self.actionPatientregister = QtWidgets.QAction(MainWindow)
        # self.actionPatientregister.setObjectName("actionPatientregister")
        self.actionAdd_Patient = QtWidgets.QAction(MainWindow)
        self.actionAdd_Patient.setObjectName("actionAdd_Patient")
        self.actionRefDr_Master = QtWidgets.QAction(MainWindow)
        self.actionRefDr_Master.setObjectName("actionRefDr_Master")
        self.actionTest_Master = QtWidgets.QAction(MainWindow)
        self.actionTest_Master.setObjectName("actionTest_Master")
        self.actionReport_Format = QtWidgets.QAction(MainWindow)
        self.actionReport_Format.setObjectName("actionReport_Format")
        self.actionregistrationsummary = QtWidgets.QAction(MainWindow)
        self.actionregistrationsummary.setObjectName("actionregistrationsummary")
        self.actionscansummary = QtWidgets.QAction(MainWindow)
        self.actionscansummary.setObjectName("actionscansummary")
        # self.menuPatientRegister.addAction(self.actionPatientregister)
        self.menuPatientRegister.addAction(self.actionAdd_Patient)
        self.menuPatientRegister.addAction(self.actionregistrationsummary)
        self.menuPatientRegister.addAction(self.actionscansummary)
        self.menuMaster.addAction(self.actionRefDr_Master)
        self.menuMaster.addAction(self.actionTest_Master)
        self.menuMaster.addAction(self.actionReport_Format)
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
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.menusdsa.setTitle(_translate("MainWindow", "Dasboard"))
        self.menuPatientRegister.setTitle(_translate("MainWindow", "Front Desk"))
        self.actionregistrationsummary.setText(_translate("MainWindow", "Registration Summary"))
        self.menuscan_Summary.setTitle(_translate("MainWindow", "Scan"))
        self.menuMaster.setTitle(_translate("MainWindow", "Master"))
        self.menuLogout.setTitle(_translate("MainWindow", "Settings"))
        self.menuSettings.setTitle(_translate("MainWindow", "Logout"))
        # self.actionPatientregister.setText(_translate("MainWindow", "Add Patient"))
        self.actionAdd_Patient.setText(_translate("MainWindow", "Patient Management"))
        self.actionscansummary.setText(_translate("MainWindow", "Scan Summary"))
        self.actionRefDr_Master.setText(_translate("MainWindow", "RefDr Master"))
        self.actionTest_Master.setText(_translate("MainWindow", "Test Master"))
        self.actionReport_Format.setText(_translate("MainWindow", "Report Format"))
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionLogout = QtWidgets.QAction(self)
        self.ui.actionLogout.setObjectName("actionLogout")
        self.ui.actionLogout.setText("Logout") 
        
        device_id_to_check = '1003'
        if self.is_device_registered(device_id_to_check):
            # The device is registered, show the login page
            self.show_login_page()
        else:
            # The device is not registered, show the device registration page
            self.show_device_registration_page()

    def logout(self):
        # Perform any necessary logout actions here
        # For example, you can close the current window and show the login form
        self.close()
        login_form = LoginForm()
        login_form.show()
        
        
    def is_device_registered(self, device_id):
    # Replace with your actual device ID check logic
       device_id = '1003'
       
       # Connect to the database
       connection = sqlite3.connect("patient_data.db")
       cursor = connection.cursor()
   
       # Check if the device is already registered
       cursor.execute("SELECT DeviceID FROM device WHERE DeviceID = ?", (device_id,))
       existing_device = cursor.fetchone()
   
       connection.close()
       
       return existing_device is not None

    def show_device_registration_page(self):
        # Pass self (the MainWindow instance) when creating DeviceRegistrationForm
        self.device_registration_form = DeviceRegistrationForm(self)
        self.device_registration_form.show()

    def show_login_page(self):
        self.login_form = LoginForm()
        # self.login_form.show()
        self.close()
        
        self.patient_register_frame = QtWidgets.QFrame()
        self.patient_register_ui = Ui_addpatientForm()#patient register
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
        
        self.add_visitsummary_frame = QtWidgets.QFrame()
        self.add_visitsummary_ui = Ui_visitsummaryForm()# Test master
        self.add_visitsummary_ui.setupUi(self.add_visitsummary_frame)
        
        self.add_scansummary_frame = QtWidgets.QFrame()
        self.add_scansummary_ui = Ui_scansummaryForm()# Test master
        self.add_scansummary_ui.setupUi(self.add_scansummary_frame)
        
        self.reportformat_frame = QtWidgets.QFrame()
        self.reportformat_ui = Ui_reportForm()# report format
        self.reportformat_ui.setupUi(self.reportformat_frame)
        
        
        # self.ui.actionPatientregister.triggered.connect(self.show_patient_register_frame)
        self.ui.actionAdd_Patient.triggered.connect(self.show_patient_master_frame)
        self.ui.actionRefDr_Master.triggered.connect(self.show_refdr_frame)
        self.ui.actionTest_Master.triggered.connect(self.show_testmaster_frame) 
        self.ui.actionregistrationsummary.triggered.connect(self.show_visitsummary_frame)
        self.ui.actionscansummary.triggered.connect(self.show_scansummary_frame)
        self.ui.actionReport_Format.triggered.connect(self.show_reportformat_frame)
        
        # Create a QStackedWidget to manage the frames
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        
        
        
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.stacked_widget.addWidget(self.ui.centralwidget)
        self.stacked_widget.addWidget(self.patient_register_frame)
        self.stacked_widget.addWidget(self.patient_master_frame)
        self.stacked_widget.addWidget(self.add_refdr_frame)
        self.stacked_widget.addWidget(self.add_testmaster_frame)
        self.stacked_widget.addWidget(self.add_visitsummary_frame)
        self.stacked_widget.addWidget(self.add_scansummary_frame)
        self.stacked_widget.addWidget(self.reportformat_frame)
        self.setCentralWidget(self.stacked_widget)
    
        self.show_patient_master_frame()
        self.patient_register_frame = QtWidgets.QFrame()
        self.patient_register_ui = Ui_addpatientForm()  # patient register
        self.patient_register_ui.setupUi(self.patient_register_frame)

 
    def refresh_main_window(self):
       # Update the content of the main window here
       # For example, you can reset the stacked widget to the central widget
    #    self.stacked_widget.clear()  # Remove all existing widgets from the stacked widget
       self.stacked_widget.addWidget(self.ui.centralwidget)
       self.stacked_widget.addWidget(self.patient_register_frame)
       self.stacked_widget.addWidget(self.patient_master_frame)
       self.stacked_widget.addWidget(self.add_refdr_frame)
       self.stacked_widget.addWidget(self.add_testmaster_frame)
       self.stacked_widget.addWidget(self.add_visitsummary_frame)
       self.stacked_widget.addWidget(self.add_scansummary_frame)
       self.stacked_widget.addWidget(self.reportformat_frame)
       self.setCentralWidget(self.stacked_widget)

       
    
    
    def show_patient_register_frame(self):
        self.stacked_widget.setCurrentWidget(self.patient_register_frame)

    def show_patient_master_frame(self):
        self.stacked_widget.setCurrentWidget(self.patient_master_frame)
        
    def show_refdr_frame(self):
        self.stacked_widget.setCurrentWidget(self.add_refdr_frame)    

    def show_testmaster_frame(self):
        self.stacked_widget.setCurrentWidget(self.add_testmaster_frame) 
    
    def show_visitsummary_frame(self):
        self.stacked_widget.setCurrentWidget(self.add_visitsummary_frame) 
    
    def show_scansummary_frame(self):
        self.stacked_widget.setCurrentWidget(self.add_scansummary_frame) 
    
    def show_reportformat_frame(self):
        self.stacked_widget.setCurrentWidget(self.reportformat_frame)     
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_form = LoginForm()  # Create an instance of the login form
    login_form.show()
    sys.exit(app.exec_())
    
    