from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
import re

class Ui_addpatientForm(object):
    def setupUi(self, Form):
        self.f=Form
        self.conn = sqlite3.connect("patient_data.db")
        Form.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        self.cursor = self.conn.cursor()
        Form.setObjectName("Form")
        Form.resize(1157, 889)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(47, 44, 301, 71))
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
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(-330, 130, 1941, 601))
        self.textEdit.setMinimumSize(QtCore.QSize(1500, 0))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 170, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(500, 170, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(740, 190, 201, 31))#GENDER
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_20.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_20.setFrame(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.comboBox_gender = QComboBox(Form)
        self.comboBox_gender.setGeometry(QtCore.QRect(740, 190, 201, 31))
        self.comboBox_gender.setFont(font)
        self.comboBox_gender.setStyleSheet("QComboBox\n"
                                   "{\n"
                                   "font-size: 15px;\n"
                                   "font-weight: 400;\n"
                                   "color: #212529;\n"
                                   "background-color: #ffffff;\n"
                                   "background-clip: padding-box;\n"
                                   "border: 1px solid #ced4da;\n"
                                   "border-radius: 20px;\n"
                                   "padding: 0px 10px;\n"
                                   "}\n"
                                   "QComboBox:focus\n"
                                   "{\n"
                                   "border: 1px solid #3F4254;\n"
                                   "}\n")
        self.comboBox_gender.setObjectName("comboBox_gender")
        
        # Populate the gender dropdown with options
        self.comboBox_gender.addItem("Male")
        self.comboBox_gender.addItem("Female")
        self.comboBox_gender.addItem("Others")
        
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(740, 170, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 310, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 310, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(500, 310, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.lineEdit_24 = QtWidgets.QLineEdit(Form)
        self.lineEdit_24.setGeometry(QtCore.QRect(740, 330, 201, 31))#MOBILE
        font = QtGui.QFont()
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("\\d{10}"), self.lineEdit_24)
        self.lineEdit_24.setValidator(validator)

        
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_24.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_24.setFrame(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(740, 310, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #5E6278;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 460, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #5E6278;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(280, 460, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #5E6278;")
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 620, 161, 31))
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
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 620, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_27 = QtWidgets.QLineEdit(Form)
        self.lineEdit_27.setGeometry(QtCore.QRect(500, 190, 211, 31))#PATIENT NAME
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_27.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_27.setFrame(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(Form)
        self.lineEdit_28.setGeometry(QtCore.QRect(500, 330, 211, 31))#EMAILID
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_28.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_28.setFrame(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_28.textChanged.connect(self.validate_email)
        self.lineEdit_29 = QtWidgets.QLineEdit(Form)
        self.lineEdit_29.setGeometry(QtCore.QRect(270, 190, 211, 31))#TITLE
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_29.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_29.setFrame(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(Form)
        self.lineEdit_30.setGeometry(QtCore.QRect(270, 330, 211, 31))#AGE
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_30.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_30.setFrame(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        int_validator = QIntValidator()
        self.lineEdit_30.setValidator(int_validator)
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setGeometry(QtCore.QRect(270, 480, 211, 31))#TEST
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_26.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_26.setFrame(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_25 = QtWidgets.QLineEdit(Form)
        self.lineEdit_25.setGeometry(QtCore.QRect(40, 190, 211, 31))#UHID
        self.lineEdit_25.setReadOnly(True)
        self.comboBox_title = QtWidgets.QComboBox(Form)
        self.comboBox_title.setGeometry(QtCore.QRect(270, 190, 211, 31))
        self.comboBox_title.setFont(font)
        self.comboBox_title.setStyleSheet("QComboBox\n"
                                          "{\n"
                                          "font-size: 15px;\n"
                                          "font-weight: 400;\n"
                                          "color: #212529;\n"
                                          "background-color: #ffffff;\n"
                                          "background-clip: padding-box;\n"
                                          "border: 1px solid #ced4da;\n"
                                          "border-radius: 20px;\n"
                                          "padding: 0px 10px;\n"
                                          "}\n"
                                          "QComboBox:focus\n"
                                          "{\n"
                                          "border: 1px solid #3F4254;\n"
                                          "}\n")
        self.comboBox_title.setObjectName("comboBox_title")

        # Populate the title dropdown with options
        self.comboBox_title.addItem("Mr")
        self.comboBox_title.addItem("SMT")
        self.comboBox_title.addItem("Others")
        self.comboBox_title.addItem("Animal")
        self.comboBox_title.addItem("Baby")
        self.comboBox_title.addItem("MS")
        self.comboBox_title.addItem("MRS")
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_25.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_25.setFrame(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        
        
        self.lineEdit_31 = QtWidgets.QDateEdit(Form)
        self.lineEdit_31.dateChanged.connect(self.calculate_age)
        self.lineEdit_31.setGeometry(QtCore.QRect(40, 330, 211, 31))#DOB
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_31.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_31.setFrame(True)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_31.setMaximumDate(QDate.currentDate())
        self.lineEdit_31.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_31.setCalendarPopup(True) 
        self.lineEdit_31.setDate(QDate.currentDate())
        self.lineEdit_31.setDisplayFormat("dd-MMM-yyyy")
        self.lineEdit_31.setFrame(True)# to date
        self.lineEdit_32 = QtWidgets.QLineEdit(Form)
        self.lineEdit_32.setGeometry(QtCore.QRect(40, 480, 211, 31))#REFDR
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_32.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_32.setFrame(True)
        self.lineEdit_32.setObjectName("lineEdit_32")

        self.comboBox_title.currentTextChanged.connect(self.update_gender_options)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.fetch_latest_patient_number()
        latest_patient_number = self.fetch_latest_patient_number()
        next_patient_number = self.generate_next_patient_number(latest_patient_number)
        self.lineEdit_25.setText(next_patient_number)  # Set the generated test code
        
        self.fetch_latest_accession_number()
        latest_accession_number = self.fetch_latest_accession_number()
        next_accession_number = self.generate_next_accession_number(latest_accession_number)
        self.comboBox_25 = QtWidgets.QComboBox(Form)
        self.comboBox_25.setGeometry(QtCore.QRect(40, 480, 211, 31))
        
        # Populate comboBox_25 with data from the database
        refdr_data = self.fetch_refdr_from_database()
        self.comboBox_25.addItems(refdr_data)

        # Create comboBox_26
        self.comboBox_26 = QtWidgets.QComboBox(Form)
        self.comboBox_26.setGeometry(QtCore.QRect(270, 480, 211, 31))

        # Populate comboBox_26 with data from the database
        selecttest_data = self.fetch_selecttest_from_database()
        self.comboBox_26.addItems(selecttest_data)
        
        self.listWidgetTestSelected = QtWidgets.QListWidget(Form)
        self.listWidgetTestSelected.setGeometry(QtCore.QRect(270, 510, 211, 111))
        self.listWidgetTestSelected.setObjectName("listWidgetTestSelected") 
        
        
        self.pushButtonAddTest = QtWidgets.QPushButton(Form)
        self.pushButtonAddTest.setGeometry(QtCore.QRect(500, 480, 51, 31))
        self.pushButtonAddTest.setText("Add")
        self.pushButtonAddTest.clicked.connect(self.add_selected_test_to_list)
        
        refdr_data = self.fetch_refdr_from_database()
        self.populate_refdrdropdown(self.comboBox_25, refdr_data)  # Use your populate function
        
        # Populate comboBox_26 with data from the database
        selecttest_data = self.fetch_selecttest_from_database()
        self.populate_testdropdown(self.comboBox_26, selecttest_data)
    
    def validate_email(self):
        email = self.lineEdit_28.text()
        # Define a regular expression pattern for a simple email format
        pattern = r'^[\w\.-]+@[\w\.-]+(\.\w+)+$'
        
        # Use re.match to check if the email matches the pattern
        if re.match(pattern, email):
            # Valid email format, set the border color to a default color
            self.lineEdit_28.setStyleSheet("QLineEdit { border: 1px solid #ced4da; }")
        else:
            # Invalid email format, set the border color to red
            self.lineEdit_28.setStyleSheet("QLineEdit { border: 1px solid red; }")
    
    def update_gender_options(self):
        # Get the selected title from the Title ComboBox
        selected_title = self.comboBox_title.currentText()

        # Clear the Gender ComboBox
        self.comboBox_gender.clear()

        # Populate the Gender ComboBox based on the selected title
        if selected_title == "Mr":
            self.comboBox_gender.addItem("Male")
        elif selected_title in ["SMT", "MRS", "MS"]:
            self.comboBox_gender.addItem("Female")
        elif selected_title in ["Others","Animal","Baby"]:  
            self.comboBox_gender.addItem("Others")  
        else:
            self.comboBox_gender.addItem("Male")
            self.comboBox_gender.addItem("Female")
            self.comboBox_gender.addItem("Others")
    
    
    def calculate_age(self):
        # Calculate age based on Date of Birth and update Age field
        dob = self.lineEdit_31.date()
        current_date = QDate.currentDate()
        age = dob.daysTo(current_date) // 365  # Calculate age in years
        self.lineEdit_30.setText(str(age))
         
    def add_selected_test_to_list(self):
     selected_test = self.comboBox_26.currentText()
     if selected_test:
        self.listWidgetTestSelected.addItem(selected_test)
    
    
    
        
    def fetch_latest_patient_number(self):
        try:
            self.cursor.execute("SELECT MAX(uhid) FROM patients")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest patient number:", str(e))
            return None

    def generate_next_patient_number(self, latest_patient_number):
        if latest_patient_number is None:
            return "P00001"

        prefix = "P"
        numeric_part = int(latest_patient_number[1:])  # Convert the numeric part to integer
        next_numeric_part = numeric_part + 1
        next_patient_number = f"{prefix}{next_numeric_part:05}"  # Format as "T00001"
        return next_patient_number
    
    def fetch_latest_accession_number(self):
        try:
            self.cursor.execute("SELECT MAX(accession) FROM patients")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest patient number:", str(e))
            return None
    
    
    def generate_next_accession_number(self, latest_accession_number):
        if latest_accession_number is None:
            return "100001"
    
        numeric_part = int(latest_accession_number)
        next_numeric_part = numeric_part + 1
        next_accession_number = str(next_numeric_part).zfill(6)
        return next_accession_number
    
    def save_accession_data(self):
        try:
            DoctorCode = self.generate_next_accession_number()
            # ... rest of your save_test_data function ...

        except Exception as e:
            print("Error:", str(e))
    
    
    def save_patient_data(self):
        try:
            DoctorCode = self.generate_next_patient_number()
            # ... rest of your save_test_data function ...

        except Exception as e:
            print("Error:", str(e))
    
    
    
    def fetch_refdr_from_database(self):
    # Connect to your database
      connection = sqlite3.connect("patient_data.db")
      cursor = connection.cursor()
  
      # Fetch categories from the "category" table
      cursor.execute("SELECT * FROM refdr")
      refdr = cursor.fetchall()
     
      # Close the connection
      connection.close()
  
      return [refdrs[1] for refdrs in refdr]
    
      
    def fetch_selecttest_from_database(self):
       connection = sqlite3.connect("patient_data.db")
       cursor = connection.cursor()
  
       # Fetch data from the "tests" table
       cursor.execute("SELECT * FROM tests")
       tests = cursor.fetchall()

       # Print the fetched data for debugging
  
       connection.close()
  
       return [test[1] for test in tests]
    
    def populate_refdrdropdown(self, combo_box, data):
        combo_box.clear()
        combo_box.addItems(data)
    
    def populate_testdropdown(self, combo_box, data):
        combo_box.clear()
        combo_box.addItems(data)  
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.label.setText(_translate("Form", "Add Patient"))
        self.label_2.setText(_translate("Form", "UHID"))
        self.label_3.setText(_translate("Form", "Title"))
        self.label_4.setText(_translate("Form", "Patient Name"))
        self.label_5.setText(_translate("Form", "Gender"))
        self.label_6.setText(_translate("Form", "DOB"))
        self.label_7.setText(_translate("Form", "Age"))
        self.label_8.setText(_translate("Form", "Email ID"))
        self.label_9.setText(_translate("Form", "Mobile"))
        self.label_10.setText(_translate("Form", "Ref Dr"))
        self.label_11.setText(_translate("Form", "Select Test"))
        self.pushButton_2.setText(_translate("Form", "Close"))
        self.pushButton_3.setText(_translate("Form", "Save"))
        self.pushButton_3.clicked.connect(self.save_patient_data)
        self.pushButton_2.clicked.connect(Form.close)
  
    def clear_input_fields(self):
        self.lineEdit_25.clear()
        self.lineEdit_29.clear()
        self.lineEdit_27.clear()
        self.lineEdit_31.clear()
        self.lineEdit_30.clear()
        self.lineEdit_20.clear()
        self.lineEdit_24.clear()
        self.lineEdit_28.clear()
        self.comboBox_25.clear()
        self.comboBox_26.clear()
        
    def save_patient_data(self):
     try:
        uhid = self.lineEdit_25.text()
        title = self.comboBox_title.currentText()
        patientname = self.lineEdit_27.text()
        dob = self.lineEdit_31.text()
        age = self.lineEdit_30.text()
        gender = self.comboBox_gender.currentText()
        mobile = self.lineEdit_24.text()
        email = self.lineEdit_28.text()
        refdr = self.comboBox_25.currentText()
        selected_test = [self.listWidgetTestSelected.item(i).text() for i in range(self.listWidgetTestSelected.count())]
        
        # Uncomment the code to fetch the latest accession number
        latest_accession_number = self.fetch_latest_accession_number()
        accession = self.generate_next_accession_number(latest_accession_number)

        # Insert patient data into the database
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%d%m%Y")

        self.cursor.execute("INSERT INTO patients (uhid, title, patientname, dob, age, gender, mobile, email, date, refdr, selected_test, accession) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (uhid, title, patientname, dob, age, gender, mobile, email, current_date, refdr, ', '.join(selected_test),accession))
        self.conn.commit()
        self.f.close()
        # Clear the input fields after saving
        self.clear_input_fields()
        
     except sqlite3.Error as e:
        print("Error:", str(e))
      
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_addpatientForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
