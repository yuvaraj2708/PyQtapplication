

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import re
from PyQt5.QtWidgets import QMessageBox

class Ui_refdrForm(object):
    def setupUi(self, Form):
        self.f=Form
        Form.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        self.conn = sqlite3.connect("patient_data.db")
        self.cursor = self.conn.cursor()       
        Form.setObjectName("Form")
        Form.resize(1157, 889)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(-240, -10, 1941, 701))
        self.textEdit.setMinimumSize(QtCore.QSize(1500, 0))
        self.textEdit.setObjectName("textEdit")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 130, 1161, 301))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(750, 70, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_8.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_8.setFrame(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(480, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(60, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(210, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #5E6278;")
        self.label_9.setObjectName("label_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(750, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #5E6278;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(60, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #5E6278;")
        self.label_11.setObjectName("label_11")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_22.setGeometry(QtCore.QRect(60, 70, 121, 31))#code
        self.lineEdit_22.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_22.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_22.setFrame(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox)
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("\\d{10}"), self.lineEdit_26)
        self.lineEdit_26.setValidator(validator)
        self.lineEdit_26.setGeometry(QtCore.QRect(320, 150, 191, 31))#mobile
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
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(320, 130, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: #5E6278;")
        self.label_19.setObjectName("label_19")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(210, 70, 241, 31))#name
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_9.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_9.setFrame(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(480, 70, 241, 31))#qualification
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
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(60, 150, 241, 31))#address
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_11.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_11.setFrame(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(60, 90, 211, 35))
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
        
        self.fetch_latest_refdr_number()
        latest_test_number = self.fetch_latest_refdr_number()
        next_test_number = self.generate_next_refdr_number(latest_test_number)
        self.lineEdit_22.setText(next_test_number)  # Set the generated test code
        
    def fetch_latest_refdr_number(self):
        try:
            self.cursor.execute("SELECT MAX(DoctorCode) FROM refdr")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest test number:", str(e))
            return None

    def generate_next_refdr_number(self, latest_refdr_number):
        if latest_refdr_number is None:
            return "R00001"

        prefix = "R"
        numeric_part = int(latest_refdr_number[1:])  # Convert the numeric part to integer
        next_numeric_part = numeric_part + 1
        next_refdr_number = f"{prefix}{next_numeric_part:05}"  # Format as "T00001"
        return next_refdr_number


            
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.pushButton_5.setText(_translate("Form", "Save"))
        self.label_7.setText(_translate("Form", "Qualification "))
        self.label_8.setText(_translate("Form", "Doctor Code"))
        self.label_9.setText(_translate("Form", "Doctor Name "))
        self.pushButton_6.setText(_translate("Form", "Close"))
        self.label_10.setText(_translate("Form", "Specialisation "))
        self.label_11.setText(_translate("Form", "Address"))
        self.label_19.setText(_translate("Form", "Mobile "))
        self.label.setText(_translate("Form", "RefDr Master"))
        self.pushButton_5.clicked.connect(self.save_refdr_data)
        self.pushButton_6.clicked.connect(Form.close)

    def validate(self,DoctorName,Qualification,Specialisation,Address,Mobile):
            name_pattern=r'^[a-zA-z]+$'
            mobile_pattern=r'[0-9]{10}'

            i=0
            if re.match(name_pattern,DoctorName):
                i=i+1
            else:
                QMessageBox.information(self.f,'Information','Please enter the correct name')
                self.lineEdit_9.clear()
            if re.match(name_pattern,Qualification):
                i=i+1
            else:
                QMessageBox.information(self.f,'Information','Please enter the correct Qualification')
                self.lineEdit_10.clear()
            if re.match(name_pattern,Specialisation):
                i=i+1
            else:
                QMessageBox.information(self.f,'Information','Please enter the correct Specialisation')
                self.lineEdit_8.clear()
            if Address=='':
                QMessageBox.information(self.f,'Information','Please enter the correct Address')
            else:
                i=i+1
            if re.match(mobile_pattern,Mobile):
                i=i+1
            else:
                QMessageBox.information(self.f,'Information','Please enter the correct Mobile')
                self.lineEdit_26.clear()

            if i==5:
                return 1
            else:
                return 0
        
    def clear_input_fields(self):
        self.lineEdit_8.clear()
        self.lineEdit_22.clear()
        self.lineEdit_26.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        
     
    def save_refdr_data(self):
        DoctorCode = self.lineEdit_22.text()
        DoctorName = self.lineEdit_9.text()
        Qualification = self.lineEdit_10.text()
        Specialisation = self.lineEdit_8.text()
        Address = self.lineEdit_11.text()
        Mobile = self.lineEdit_26.text()
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%d%m%Y")

        value=self.validate(DoctorName,Qualification,Specialisation,Address,Mobile)
        if value!=1:
                DoctorCode = self.lineEdit_22.text()
                DoctorName = self.lineEdit_9.text()
                Qualification = self.lineEdit_10.text()
                Specialisation = self.lineEdit_8.text()
                Address = self.lineEdit_11.text()
                Mobile = self.lineEdit_26.text()
                current_datetime = datetime.datetime.now()
                current_date = current_datetime.strftime("%d%m%Y")

        if DoctorName and Qualification and Specialisation and Address and Mobile:
        # Insert patient data into the database
                self.cursor.execute("INSERT INTO refdr (DoctorCode, DoctorName, Qualification, Specialisation, Address,  Mobile,date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (DoctorCode, DoctorName, Qualification, Specialisation, Address, Mobile,current_date))
                self.conn.commit()

                # Clear the input fields after saving
                self.clear_input_fields()
                self.f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_refdrForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
