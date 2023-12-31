from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import re
from PyQt5.QtWidgets import QMessageBox

class Ui_addtestForm(object):
        

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
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 190, 131, 31))
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
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 190, 131, 31))
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
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(630, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_23.setGeometry(QtCore.QRect(370, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_23.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_23.setFrame(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(110, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(370, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #5E6278;")
        self.label_9.setObjectName("label_9")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_25.setGeometry(QtCore.QRect(630, 80, 251, 31))
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
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_26.setGeometry(QtCore.QRect(110, 80, 251, 31))
        self.lineEdit_26.setReadOnly(True)
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(110, 90, 211, 35))
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
        
        self.fetch_latest_test_number()
        latest_test_number = self.fetch_latest_test_number()
        next_test_number = self.generate_next_test_number(latest_test_number)
        self.lineEdit_26.setText(next_test_number)  # Set the generated test code
        
    def fetch_latest_test_number(self):
        try:
            self.cursor.execute("SELECT MAX(Testcode) FROM tests")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest test number:", str(e))
            return None

    def generate_next_test_number(self, latest_test_number):
        if latest_test_number is None:
            return "T00001"

        prefix = "T"
        numeric_part = int(latest_test_number[1:])  # Convert the numeric part to integer
        next_numeric_part = numeric_part + 1
        next_test_number = f"{prefix}{next_numeric_part:05}"  # Format as "T00001"
        return next_test_number


    
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.pushButton_5.setText(_translate("Form", "Save"))
        self.pushButton_6.setText(_translate("Form", "Close"))
        self.label_7.setText(_translate("Form", "specimen type"))
        self.label_8.setText(_translate("Form", "Test code"))
        self.label_9.setText(_translate("Form", "Test Name"))
        self.label.setText(_translate("Form", "Add Test"))
        self.pushButton_5.clicked.connect(self.save_test_data)
        self.pushButton_6.clicked.connect(Form.close)
        
    def clear_input_fields_test(self):
        self.lineEdit_23.clear()
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        
    def validate(self,testname,specimen):
        pattern=r'^[a-zA-Z]+$' 
        i=0
        if re.match(pattern,testname):
            i=i+1
        else:
            QMessageBox.information(self.f,'Information','Please enter the correct testname')
            self.lineEdit_23.clear()   
        if re.match(pattern,specimen):
            i=i+1
        else:
            QMessageBox.information(self.f,'Information','Please enter the correct specimen type')
            self.lineEdit_25.clear()

        if i==2:
            return 1
        else:
            return 0
    
    

    def save_test_data(self):
        try:
            Testcode = self.lineEdit_26.text()
            TestName = self.lineEdit_23.text()
            specimentype = self.lineEdit_25.text()
            
            value=self.validate(TestName,specimentype)
            if value==1:
            # Insert patient data into the database
                self.cursor.execute("INSERT INTO tests (Testcode, TestName, specimentype) VALUES (?, ?, ?)",
                                    (Testcode, TestName, specimentype))
                self.conn.commit()
        
                # Clear the input fields after saving
                self.clear_input_fields_test()
                self.f.close()

        except Exception as e:
            print("Error:", str(e))
        
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_addtestForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())