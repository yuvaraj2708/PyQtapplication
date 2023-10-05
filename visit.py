from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from PyQt5.QtWidgets import QComboBox


class Ui_visitpatientForm(object):
    def setupUi(self, Form,patient_uhid):
        self.f=Form
        self.conn = sqlite3.connect("patient_data.db")
        self.cursor = self.conn.cursor()
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
        self.lineEdit_20.setReadOnly(True)
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
        self.comboBox_gender.setEnabled(False)
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
        self.lineEdit_24.setReadOnly(True)
        font = QtGui.QFont()
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
        self.lineEdit_27.setReadOnly(True)
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
        self.lineEdit_28.setReadOnly(True)
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
        self.lineEdit_30.setReadOnly(True)
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
       
        self.lineEdit_25 = QtWidgets.QLineEdit(Form)
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setGeometry(QtCore.QRect(40, 190, 211, 31))#UHID
        
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_title = QComboBox(Form)
        self.comboBox_title.setGeometry(QtCore.QRect(270, 190, 211, 31))
        self.comboBox_title.setEnabled(False)
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
        
        self.lineEdit_31 = QtWidgets.QLineEdit(Form)
        self.lineEdit_31.setGeometry(QtCore.QRect(40, 330, 211, 31))#DOB
        self.lineEdit_31.setReadOnly(True)
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
      

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        latest_visit_number = self.fetch_latest_visit_number()
        next_visit_number = self.generate_next_visit_number(latest_visit_number)
        self.lineEdit_25.setText(next_visit_number)  # Set the generated test code
          
        self.patient_uhid = patient_uhid  # Store the patient ID
        self.populate_patient_data() 
        
    def populate_patient_data(self):
        if self.patient_uhid:
            # Fetch patient data for the specified patient_id
            patient_data = self.fetch_patient_data_by_id(self.patient_uhid)
            if patient_data:
                # Populate the form fields with the patient data
                self.lineEdit_29.setText(patient_data[2])  # Assuming the second item is the title
                self.lineEdit_27.setText(patient_data[3])  # Assuming the third item is the patient name
                self.lineEdit_31.setText(str(patient_data[4]))
                self.lineEdit_30.setText(patient_data[5])
                self.lineEdit_20.setText(patient_data[6])
                self.lineEdit_24.setText(patient_data[7])
                self.lineEdit_28.setText(patient_data[8])
                # self.comboBox_25.currentText(patient_data[9])
                # self.comboBox_26.currentText(patient_data[10])
    
    def fetch_patient_data_by_id(self, patient_uhid):
        self.cursor.execute("SELECT * FROM patients WHERE uhid=?", (patient_uhid,))
        patient_data = self.cursor.fetchone()
        return patient_data    
        
   
        
    def fetch_latest_visit_number(self):
        try:
            self.cursor.execute("SELECT MAX(visitid) FROM visit")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest patient number:", str(e))
            return None

    def generate_next_visit_number(self, latest_patient_number):
        if latest_patient_number is None:
            return "V00001"

        prefix = "V"
        numeric_part = int(latest_patient_number[1:])  # Convert the numeric part to integer
        next_numeric_part = numeric_part + 1
        next_patient_number = f"{prefix}{next_numeric_part:05}"  # Format as "T00001"
        return next_patient_number
    

    
    def save_patient_data(self):
        try:
            DoctorCode = self.generate_next_patient_number()
            # ... rest of your save_test_data function ...

        except Exception as e:
            print("Error:", str(e))
    

    

            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.label.setText(_translate("Form", "Add Patient"))
        self.label_2.setText(_translate("Form", "visitID"))
        self.label_3.setText(_translate("Form", "Title"))
        self.label_4.setText(_translate("Form", "Patient Name"))
        self.label_5.setText(_translate("Form", "Gender"))
        self.label_6.setText(_translate("Form", "DOB"))
        self.label_7.setText(_translate("Form", "Age"))
        self.label_8.setText(_translate("Form", "Email ID"))
        self.label_9.setText(_translate("Form", "Mobile"))
        #self.label_10.setText(_translate("Form", "Ref Dr"))
       #self.label_11.setText(_translate("Form", "Select Test"))
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

        
    def save_patient_data(self):
     try:
        visitid = self.lineEdit_25.text()
        title = self.comboBox_title.currentText()
        patientname = self.lineEdit_27.text()
        dob = self.lineEdit_31.text()
        age = self.lineEdit_30.text()
        gender = self.comboBox_gender.currentText()
        mobile = self.lineEdit_24.text()
        email = self.lineEdit_28.text()
   

        # Insert patient data into the database
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%d%m%Y")

        self.cursor.execute("INSERT INTO VISIT (uhid,date,title,patientname,dob,age,gender,mobile,email,visitid) VALUES (?,?,?,?,?,?,?,?,?,?)",
                            (self.patient_uhid,current_date,title,patientname,dob,age,gender,mobile,email,visitid))
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
    ui = Ui_visitpatientForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
