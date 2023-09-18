from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from PyQt5.QtWidgets import QComboBox

class Ui_editpatientForm(object):
    def setupUi(self, Form,patient_uhid):
        self.conn = sqlite3.connect("patient_data.db")
        self.cursor = self.conn.cursor()
        self.conn = sqlite3.connect("patient_data.db")
        Form.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        self.cursor = self.conn.cursor()
        Form.setObjectName("Form")
        Form.resize(900, 588)
        Form.setMaximumSize(QtCore.QSize(851, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: #ffffff;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 35))
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
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 961, 401))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(360, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(570, 70, 201, 31))
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
        self.pushButton.setGeometry(QtCore.QRect(300, 300, 111, 31))
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
        self.label_4.setGeometry(QtCore.QRect(360, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(230, 140, 121, 31))
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
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(570, 120, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #5E6278;")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(230, 120, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 250, 111, 31))
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
        self.label_5.setGeometry(QtCore.QRect(570, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(570, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16.setGeometry(QtCore.QRect(20, 70, 121, 31))
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
        self.lineEdit_18.setGeometry(QtCore.QRect(360, 70, 201, 31))
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
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 70, 201, 31))
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
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_14.setGeometry(QtCore.QRect(570, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_14.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_14.setFrame(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_13.setGeometry(QtCore.QRect(360, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_13.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_13.setFrame(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setGeometry(QtCore.QRect(20, 140, 201, 31))
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
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #5E6278;")
        self.label_11.setObjectName("label_11")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_25.setGeometry(QtCore.QRect(20, 220, 201, 31))
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
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(460, 190, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #5E6278;")
        self.label_12.setObjectName("label_12")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_26.setGeometry(QtCore.QRect(460, 210, 201, 31))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.fetch_latest_patient_number()
        latest_patient_number = self.fetch_latest_patient_number()
        next_patient_number = self.generate_next_patient_number(latest_patient_number)
        self.lineEdit_16.setText(next_patient_number)  # Set the generated test code
        
        self.fetch_latest_accession_number()
        latest_accession_number = self.fetch_latest_accession_number()
        next_accession_number = self.generate_next_accession_number(latest_accession_number)
        self.comboBox_25 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_25.setGeometry(QtCore.QRect(20, 220, 201, 31))
        
        # Populate comboBox_25 with data from the database
        refdr_data = self.fetch_refdr_from_database()
        self.comboBox_25.addItems(refdr_data)

        # Create comboBox_26
        self.comboBox_26 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_26.setGeometry(QtCore.QRect(460, 210, 201, 31))

        # Populate comboBox_26 with data from the database
        selecttest_data = self.fetch_selecttest_from_database()
        self.comboBox_26.addItems(selecttest_data)
        
        self.listWidgetTestSelected = QtWidgets.QListWidget(self.groupBox)
        self.listWidgetTestSelected.setGeometry(QtCore.QRect(460, 250, 201, 111))
        self.listWidgetTestSelected.setObjectName("listWidgetTestSelected") 
        
        
        self.pushButtonAddTest = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddTest.setGeometry(QtCore.QRect(680, 210, 51, 31))
        self.pushButtonAddTest.setText("Add")
        self.pushButtonAddTest.clicked.connect(self.add_selected_test_to_list)
        
        refdr_data = self.fetch_refdr_from_database()
        self.populate_refdrdropdown(self.comboBox_25, refdr_data)  # Use your populate function
        
        # Populate comboBox_26 with data from the database
        selecttest_data = self.fetch_selecttest_from_database()
        self.populate_testdropdown(self.comboBox_26, selecttest_data)
        self.patient_uhid = patient_uhid  # Store the patient ID
        self.populate_patient_data() 
        
    def populate_patient_data(self):
        if self.patient_uhid:
            # Fetch patient data for the specified patient_id
            patient_data = self.fetch_patient_data_by_id(self.patient_uhid)
            if patient_data:
                # Populate the form fields with the patient data
                self.lineEdit_16.setText(str(patient_data[0]))
                self.lineEdit_15.setText(patient_data[2])  # Assuming the second item is the title
                self.lineEdit_18.setText(patient_data[3])  # Assuming the third item is the patient name
                self.lineEdit_6.setText(patient_data[4])
                self.lineEdit_12.setText(patient_data[5])
                self.lineEdit_10.setText(patient_data[6])
                self.lineEdit_14.setText(patient_data[7])
                self.lineEdit_13.setText(patient_data[8])
                # self.comboBox_25.currentText(patient_data[9])
                # self.comboBox_26.currentText(patient_data[10])
    
    def fetch_patient_data_by_id(self, patient_uhid):
        self.cursor.execute("SELECT * FROM patients WHERE uhid=?", (patient_uhid,))
        patient_data = self.cursor.fetchone()
        return patient_data    
        
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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Add Patient"))
        self.label_7.setText(_translate("Form", "Email ID"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.pushButton_2.setText(_translate("Form", "Close"))
        self.pushButton_2.clicked.connect(Form.close)
        self.label_4.setText(_translate("Form", "Patient Name"))
        self.label_2.setText(_translate("Form", "UHID"))
        self.label_3.setText(_translate("Form", "Title"))
        self.label_9.setText(_translate("Form", "Mobile"))
        self.label_8.setText(_translate("Form", "Age"))
        self.label_5.setText(_translate("Form", "Gender"))
        self.label_6.setText(_translate("Form", "DOB"))
        self.label_11.setText(_translate("Form", "Ref Dr"))
        self.label_12.setText(_translate("Form", "Select Test"))
        self.pushButton.clicked.connect(self.save_patient_data)
        
    def clear_input_fields(self):
        self.lineEdit_16.clear()
        self.lineEdit_15.clear()
        self.lineEdit_18.clear()
        self.lineEdit_6.clear()
        self.lineEdit_12.clear()
        self.lineEdit_10.clear()
        self.lineEdit_14.clear()
        self.lineEdit_13.clear()
        self.comboBox_25.clear()
        self.comboBox_26.clear()
        
    def save_patient_data(self):
     try:
        uhid = self.lineEdit_16.text()
        title = self.lineEdit_15.text()
        patientname = self.lineEdit_18.text()
        dob = self.lineEdit_6.text()
        age = self.lineEdit_12.text()
        gender = self.lineEdit_10.text()
        mobile = self.lineEdit_14.text()
        email = self.lineEdit_13.text()
        refdr = self.comboBox_25.currentText()
        selected_test = self.comboBox_26.currentText()
        
        # Uncomment the code to fetch the latest accession number
        latest_accession_number = self.fetch_latest_accession_number()
        accession = self.generate_next_accession_number(latest_accession_number)

        # Insert patient data into the database
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%d%m%Y")

        self.cursor.execute("UPDATE patients SET title=?, patientname=?, dob=?, age=?, gender=?, mobile=?, email=?, date=?, refdr=?, selected_test=?, accession=? WHERE uhid=?",
                            (title, patientname, dob, age, gender, mobile, email, current_date, refdr, selected_test,accession,uhid))
        self.conn.commit()
        # self.f.close()

        # Clear the input fields after saving
        self.clear_input_fields()
        
     except sqlite3.Error as e:
        print("Error:", str(e))
      
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_editpatientForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
