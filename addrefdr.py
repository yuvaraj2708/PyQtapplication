

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_refdrForm(object):
    def setupUi(self, Form):
        self.conn = sqlite3.connect("patient_data.db")
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
        self.groupBox.setGeometry(QtCore.QRect(0, 50, 961, 301))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
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
        self.pushButton.setGeometry(QtCore.QRect(290, 210, 91, 31))
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
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 91, 16))
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
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(230, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 210, 91, 31))
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
        self.label_5.setGeometry(QtCore.QRect(570, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 81, 16))
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
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_14.setGeometry(QtCore.QRect(370, 140, 191, 31))
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
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(370, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #5E6278;")
        self.label_14.setObjectName("label_14")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_21.setGeometry(QtCore.QRect(570, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_21.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_21.setFrame(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(570, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: #5E6278;")
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.fetch_latest_refdr_number()
        latest_test_number = self.fetch_latest_refdr_number()
        next_test_number = self.generate_next_refdr_number(latest_test_number)
        self.lineEdit_16.setText(next_test_number)  # Set the generated test code
        
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
            return "D00001"

        prefix = "D"
        numeric_part = int(latest_refdr_number[1:])  # Convert the numeric part to integer
        next_numeric_part = numeric_part + 1
        next_refdr_number = f"{prefix}{next_numeric_part:05}"  # Format as "T00001"
        return next_refdr_number


            
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pathalogist Master"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label_4.setText(_translate("Form", "Qualification "))
        self.label_2.setText(_translate("Form", "Doctor Code"))
        self.label_3.setText(_translate("Form", "Doctor Name "))
        self.label_8.setText(_translate("Form", "PIN Code"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.label_5.setText(_translate("Form", "Specialisation "))
        self.label_6.setText(_translate("Form", "Address"))
        self.label_14.setText(_translate("Form", "Mobile "))
        self.label_15.setText(_translate("Form", "Email ID"))
        self.pushButton.clicked.connect(self.save_refdr_data)
    
    def clear_input_fields(self):
        self.lineEdit_16.clear()
        self.lineEdit_15.clear()
        self.lineEdit_18.clear()
        self.lineEdit_6.clear()
        self.lineEdit_12.clear()
        self.lineEdit_10.clear()
        self.lineEdit_14.clear()
        self.lineEdit_21.clear()
     
    def save_refdr_data(self):
        DoctorCode = self.lineEdit_16.text()
        DoctorName = self.lineEdit_15.text()
        Qualification = self.lineEdit_18.text()
        Specialisation = self.lineEdit_6.text()
        Address = self.lineEdit_12.text()
        PINCode = self.lineEdit_10.text()
        Mobile = self.lineEdit_14.text()
        Emailid = self.lineEdit_21.text()

        # Insert patient data into the database
        self.cursor.execute("INSERT INTO refdr (DoctorCode, DoctorName, Qualification, Specialisation, Address, PINCode, Mobile,Emailid) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (DoctorCode, DoctorName, Qualification, Specialisation, Address, PINCode, Mobile,Emailid))
        self.conn.commit()

        # Clear the input fields after saving
        self.clear_input_fields()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_refdrForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
