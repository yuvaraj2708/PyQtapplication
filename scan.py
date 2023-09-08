from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scanForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 588)
        Form.setMaximumSize(QtCore.QSize(811, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: #ffffff;")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 79, 19))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(370, 90, 34, 19))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 310, 211, 81))
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
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(580, 90, 67, 19))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 310, 211, 81))
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
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(270, 90, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(510, 90, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.patient_details_label = QtWidgets.QLabel(Form)
        self.patient_details_label.setGeometry(QtCore.QRect(110, 120, 300, 19))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.patient_details_label.setFont(font)
        self.patient_details_label.setStyleSheet("color: #212529;")
        self.patient_details_label.setObjectName("patient_details_label")

        self.ref_by_label = QtWidgets.QLabel(Form)
        self.ref_by_label.setGeometry(QtCore.QRect(360, 120, 200, 19))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.ref_by_label.setFont(font)
        self.ref_by_label.setStyleSheet("color: #212529;")
        self.ref_by_label.setObjectName("ref_by_label")

        self.test_asked_label = QtWidgets.QLabel(Form)
        self.test_asked_label.setGeometry(QtCore.QRect(580, 120, 200, 19))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.test_asked_label.setFont(font)
        self.test_asked_label.setStyleSheet("color: #212529;")
        self.test_asked_label.setObjectName("test_asked_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def set_scan_data(self, visit_data):
        
       uhid, visit_id, selected_test, ref_dr, patient_category, patient_name, dob, age, gender, mobile, email = visit_data
   
       # Set the text of the labels with the scanned data
       self.patient_details_label.setText(f"Patient Name: {ref_dr}")#name
       self.ref_by_label.setText(f"Ref By: {visit_id}") #dr
       self.test_asked_label.setText(f"Test’s Asked: {email}") #test
    
    
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.label_2.setText(_translate("Form", "Patient Details"))
        # self.label_3.setText(_translate("Form", "Ref By"))
        self.pushButton.setText(_translate("Form", "Automatic Scan"))
        # self.label_4.setText(_translate("Form", "Test’s Asked"))
        self.pushButton_2.setText(_translate("Form", "Manual Scan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_scanForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
