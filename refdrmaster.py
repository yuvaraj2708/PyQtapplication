# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refdrmaster.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from addrefdr import Ui_refdrForm
import sqlite3

class Ui_refdrmasterForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        Form.setMaximumSize(QtCore.QSize(811, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: #ffffff;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 35))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(740, 260, 41, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 190, 91, 31))
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
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 260, 70, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(120, 260, 74, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(200, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_19.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_19.setFrame(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(220, 260, 70, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(520, 260, 48, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(430, 260, 46, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(320, 260, 78, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(610, 260, 37, 16))
        self.label_18.setObjectName("label_18")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(560, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(380, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.lineEdit_23 = QtWidgets.QLineEdit(Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(20, 120, 161, 31))
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
        self.lineEdit_24 = QtWidgets.QLineEdit(Form)
        self.lineEdit_24.setGeometry(QtCore.QRect(560, 120, 161, 31))
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
        self.lineEdit_25 = QtWidgets.QLineEdit(Form)
        self.lineEdit_25.setGeometry(QtCore.QRect(380, 120, 161, 31))
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
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(20, 190, 161, 31))
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 190, 91, 31))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.setObjectName("pushButton_2")
      
 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(-27, 280, 921, 421))
        self.textEdit.setObjectName("textEdit")
        
        

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.fetch_and_display_redr_data()
        
        
        # self.lineEdit_16.textChanged.connect(self.fetch_and_display_test_data)
    
    
    
    def fetch_and_display_redr_data(self):
    # Connect to the database
     conn = sqlite3.connect('patient_data.db')
     cursor = conn.cursor()
 
     # Fetch reference data
     cursor.execute("SELECT * FROM refdr")
     refdr_data = cursor.fetchall()
 
     if refdr_data:
         # Clear previous data from textEdit
         self.textEdit.clear()
 
         # Create a new vertical layout to hold rows of data
         vertical_layout = QtWidgets.QVBoxLayout()
 
         # Loop through each row in the refdr_data
         for row in refdr_data:
             # Create a new horizontal layout for this row
             layout = QtWidgets.QHBoxLayout()
 
             # Loop through each column in the row
             for column in row:
                 label = QtWidgets.QLabel(str(column))
                 layout.addWidget(label)
 
             # Add the horizontal layout (row) to the vertical layout
             vertical_layout.addLayout(layout)
 
         # Add the vertical layout to the textEdit
         self.textEdit.setLayout(vertical_layout)
 
     # Close the database connection
     conn.close()
 
 



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.label.setText(_translate("Form", "Ref Dr Master"))
        self.label_2.setText(_translate("Form", "From Date"))
        self.label_3.setText(_translate("Form", "To Date"))
        self.label_13.setText(_translate("Form", "Actions"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_10.setText(_translate("Form", "Doctor Code"))
        self.label_11.setText(_translate("Form", "Doctor Name"))
        self.label_14.setText(_translate("Form", "Qualification"))
        self.label_15.setText(_translate("Form", "PINCode"))
        self.label_16.setText(_translate("Form", "Address"))
        self.label_17.setText(_translate("Form", "Specialisation"))
        self.label_18.setText(_translate("Form", "Mobile"))
        self.label_4.setText(_translate("Form", "Doctor Code"))
        self.label_5.setText(_translate("Form", "Doctor Name"))
        self.label_6.setText(_translate("Form", "Qualification"))
        self.pushButton_2.setText(_translate("Form", "Add RefDr"))
        self.pushButton_2.clicked.connect(self.open_addrefdr_form)

   
    def open_addrefdr_form(self):
        self.add_test_form = QtWidgets.QWidget()
        self.ui_add_test = Ui_refdrForm()
        self.ui_add_test.setupUi(self.add_test_form)
        self.add_test_form.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_refdrmasterForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
