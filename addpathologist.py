

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog


class Ui_pathologisterForm(object):
    def setupUi(self, Form):
        self.f=Form
        self.conn = sqlite3.connect("patient_data.db")
        Form.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        self.cursor = self.conn.cursor()       
        Form.setObjectName("Form")
        Form.resize(1157, 642)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(-10, 140, 1161, 341))
        self.textEdit.setObjectName("textEdit")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(-10, 140, 1181, 341))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(760, 70, 231, 31))#specilisation
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
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(480, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: #5E6278;")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(70, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: #5E6278;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(210, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: #5E6278;")
        self.label_23.setObjectName("label_23")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(760, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: #5E6278;")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(100, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: #5E6278;")
        self.label_25.setObjectName("label_25")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_28.setGeometry(QtCore.QRect(70, 70, 121, 31))#code
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
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(330, 130, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: #5E6278;")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(590, 130, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: #5E6278;")
        self.label_27.setObjectName("label_27")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(480, 70, 231, 31))#qualification
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
        self.lineEdit_11.setGeometry(QtCore.QRect(210, 70, 231, 31))#name
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
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_29.setGeometry(QtCore.QRect(330, 150, 231, 31))#mobile
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
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_30.setGeometry(QtCore.QRect(590, 150, 231, 31))#signature
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
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_32.setGeometry(QtCore.QRect(70, 150, 231, 31))#address
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(60, 80, 211, 35))
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
        self.lineEdit_28.setText(next_test_number)  # Set the generated test code
        
        self.selectImageBtn = QtWidgets.QToolButton(self.groupBox)
        self.selectImageBtn.setGeometry(QtCore.QRect(830, 150, 100, 19))  # Position the "Select Image" button near the QLineEdit
        self.selectImageBtn.setText("Add Signature")
        self.selectImageBtn.clicked.connect(self.selectImage)
        
    def selectImage(self):
       options = QFileDialog.Options()
       options |= QFileDialog.ReadOnly
       options |= QFileDialog.HideNameFilterDetails
       options |= QFileDialog.DontUseNativeDialog

       file_path, _ = QFileDialog.getOpenFileName(self.f, "Select Image File", "", "Image Files (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options)

       if file_path:
           # Set the selected image file path in the QLineEdit
           self.lineEdit_30.setText(file_path)
        
    def fetch_latest_refdr_number(self):
        try:
            self.cursor.execute("SELECT MAX(DoctorCode) FROM pathologist")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest test number:", str(e))
            return None

    def generate_next_refdr_number(self, latest_refdr_number):
     if latest_refdr_number is None:
         return "D00001"

     try:
         # Attempt to convert the numeric part to an integer
         numeric_part = int(latest_refdr_number[1:])
     except ValueError:
         # Handle the case where the conversion fails (e.g., if latest_refdr_number is not a valid integer string)
         # You can set a default numeric_part or raise an error as needed.
         numeric_part = 1  # Set a default value, or choose an appropriate fallback.

     prefix = "D"
     next_numeric_part = numeric_part + 1
     next_refdr_number = f"{prefix}{next_numeric_part:05}"  # Format as "D00001"
     return next_refdr_number



            
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.pushButton_7.setText(_translate("Form", "Save"))
        self.label_21.setText(_translate("Form", "Qualification "))
        self.label_22.setText(_translate("Form", "Doctor Code"))
        self.label_23.setText(_translate("Form", "Doctor Name "))
        self.pushButton_8.setText(_translate("Form", "Close"))
        self.label_24.setText(_translate("Form", "Specialisation "))
        self.label_25.setText(_translate("Form", "Address"))
        self.label_26.setText(_translate("Form", "Mobile "))
        self.label_27.setText(_translate("Form", "Signature"))
        self.label.setText(_translate("Form", "Add Pathologist"))
        self.pushButton_7.clicked.connect(self.save_refdr_data)
        self.pushButton_8.clicked.connect(Form.close)
        
    def clear_input_fields(self):
        self.lineEdit_9.clear()
        self.lineEdit_28.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_29.clear()
        self.lineEdit_30.clear()
        self.lineEdit_32.clear()
        
     
    def save_refdr_data(self):
        DoctorCode = self.lineEdit_28.text()
        DoctorName = self.lineEdit_11.text()
        Qualification = self.lineEdit_10.text()
        Specialisation = self.lineEdit_9.text()
        Address = self.lineEdit_32.text()
        signature = self.lineEdit_30.text()
        Mobile = self.lineEdit_29.text()
        
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%d%m%Y")

        # Insert patient data into the database
        self.cursor.execute("INSERT INTO pathologist (DoctorCode, DoctorName, Qualification, Specialisation, Address, Mobile,signature,date) VALUES (?, ?, ?, ?, ?, ?, ?,?)",
                            (DoctorCode, DoctorName, Qualification, Specialisation, Address,Mobile,signature,current_date))
        self.conn.commit()

        # Clear the input fields after saving
        self.clear_input_fields()
        self.f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_pathologisterForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
