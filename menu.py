from PyQt5 import QtCore, QtGui, QtWidgets
from patientregister import Ui_addpatientForm
from patientdetails import Ui_patientForm 
from refdrmaster import Ui_refdrmasterForm 
from testmaster import Ui_testForm
from registrationsummary import Ui_visitsummaryForm
from reportformat import Ui_reportForm
from scansummary import Ui_scansummaryForm

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
    MainWindow = MainWindow()  # Create an instance of your MainWindow
    MainWindow.show()
    sys.exit(app.exec_())