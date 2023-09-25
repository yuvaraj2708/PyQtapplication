# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addrefdr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime

class Ui_editrefdrForm(object):
    def setupUi(self, Form,DoctorCode):
        self.conn = sqlite3.connect("patient_data.db")
        Form.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
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

        self.DoctorCode = DoctorCode
        self.populate_refdr_data()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def populate_refdr_data(self):
        if self.DoctorCode:
            # Fetch refdr data for the specified DoctorCode
            refdr_data = self.fetch_refdr_data_by_id(self.DoctorCode)
            if refdr_data:
                # Populate the form fields with the refdr data
                self.lineEdit_22.setText(refdr_data[0])  # Assuming the first item is DoctorCode
                self.lineEdit_9.setText(refdr_data[1])   # Assuming the second item is DoctorName
                self.lineEdit_10.setText(refdr_data[2])  # Assuming the third item is Qualification
                self.lineEdit_8.setText(refdr_data[3])   # Assuming the fourth item is Specialisation
                self.lineEdit_11.setText(refdr_data[4])  # Assuming the fifth item is Address
                self.lineEdit_26.setText(refdr_data[5])  # Assuming the sixth item is Mobile
                
                
    def fetch_refdr_data_by_id(self, DoctorCode):
        self.cursor.execute("SELECT * FROM refdr WHERE DoctorCode=?", (DoctorCode,))
        refdr_data = self.cursor.fetchone()
        return refdr_data            
                       
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

        # Update refdr data in the database based on DoctorCode
        self.cursor.execute("UPDATE refdr SET DoctorName=?, Qualification=?, Specialisation=?, Address=?, Mobile=? WHERE DoctorCode=?",
                            (DoctorName, Qualification, Specialisation, Address, Mobile, DoctorCode))
        self.conn.commit()

        # Clear the input fields after saving
        self.clear_input_fields()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_editrefdrForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
