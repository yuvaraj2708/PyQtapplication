from PyQt5 import QtCore, QtGui, QtWidgets
from patientregister import Ui_addpatientForm
from patientdetails import Ui_patientForm 
from refdrmaster import Ui_refdrmasterForm 
from testmaster import Ui_testForm
from registrationsummary import Ui_visitsummaryForm
from reportformat import Ui_reportForm
from scansummary import Ui_scansummaryForm



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
        if self.ui.usernameLineEdit.text() == "username" and self.ui.passwordLineEdit.text() == "password":
            self.main_window = MainWindow()
            self.close()
            self.main_window.show()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")




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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionPatientregister = QtWidgets.QAction(MainWindow)
        self.actionPatientregister.setObjectName("actionPatientregister")
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
        self.menuPatientRegister.addAction(self.actionPatientregister)
        self.menuPatientRegister.addAction(self.actionAdd_Patient)
        self.menuMaster.addAction(self.actionRefDr_Master)
        self.menuMaster.addAction(self.actionTest_Master)
        self.menuMaster.addAction(self.actionReport_Format)
        self.menuVisit_Summary.addAction(self.actionregistrationsummary)
        self.menuscan_Summary.addAction(self.actionscansummary)
        self.menubar.addAction(self.menusdsa.menuAction())
        self.menubar.addAction(self.menuPatientRegister.menuAction())
        self.menubar.addAction(self.menuVisit_Summary.menuAction())
        self.menubar.addAction(self.menuscan_Summary.menuAction())
        self.menubar.addAction(self.menuMaster.menuAction())
        self.menubar.addAction(self.menuLogout.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.menusdsa.setTitle(_translate("MainWindow", "Dasboard"))
        self.menuPatientRegister.setTitle(_translate("MainWindow", "Front Desk"))
        self.menuVisit_Summary.setTitle(_translate("MainWindow", "Visit"))
        self.actionregistrationsummary.setText(_translate("MainWindow", "Registration Summary"))
        self.menuscan_Summary.setTitle(_translate("MainWindow", "Scan"))
        self.actionscansummary.setText(_translate("MainWindow", "Scan Summary"))
        self.menuMaster.setTitle(_translate("MainWindow", "Master"))
        self.menuLogout.setTitle(_translate("MainWindow", "Settings"))
        self.menuSettings.setTitle(_translate("MainWindow", "Logout"))
        self.actionPatientregister.setText(_translate("MainWindow", "Add Patient"))
        self.actionAdd_Patient.setText(_translate("MainWindow", "Patient Master"))
        self.actionRefDr_Master.setText(_translate("MainWindow", "RefDr Master"))
        self.actionTest_Master.setText(_translate("MainWindow", "Test Master"))
        self.actionReport_Format.setText(_translate("MainWindow", "Report Format"))
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        
        
        self.ui.actionPatientregister.triggered.connect(self.show_patient_register_frame)
        self.ui.actionAdd_Patient.triggered.connect(self.show_patient_master_frame)
        self.ui.actionRefDr_Master.triggered.connect(self.show_refdr_frame)
        self.ui.actionTest_Master.triggered.connect(self.show_testmaster_frame) 
        self.ui.menuVisit_Summary.triggered.connect(self.show_visitsummary_frame)
        self.ui.menuscan_Summary.triggered.connect(self.show_scansummary_frame)
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
    
    def refresh_main_window(self):
       # Update the content of the main window here
       # For example, you can reset the stacked widget to the central widget
       self.stacked_widget.clear()  # Remove all existing widgets from the stacked widget
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
    
    