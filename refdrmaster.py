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
import os
from editrefdr import Ui_editrefdrForm
from PyQt5.QtCore import QTime, QTimer

class Ui_refdrmasterForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1094, 889)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 340, 1941, 601))
        self.textEdit.setMinimumSize(QtCore.QSize(1500, 0))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 140, 111, 31))
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
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(830, 310, 41, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(30, 140, 201, 31))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(250, 140, 201, 31))#code
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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(470, 140, 111, 31))
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, 40, 211, 35))
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
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(1150, 310, 37, 16))
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(260, 310, 70, 16))
        self.label_16.setObjectName("label_16")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(140, 310, 74, 16))
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(510, 310, 46, 16))
        self.label_19.setObjectName("label_19")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(30, 310, 70, 16))
        self.label_13.setObjectName("label_13")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(380, 310, 78, 16))
        self.label_20.setObjectName("label_20")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_3.setObjectName("pushButton_3")
      
        
      
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 340, 1050, 600))  # Adjust the geometry as needed
        self.listWidget.setObjectName("listWidget")


        self.timer = QTimer(Form)
        # Set the interval to 1000 milliseconds (1 second)
        self.timer.setInterval(1000)
        # Connect the timeout signal to the function you want to call
        self.timer.timeout.connect(self.fetch_and_display_refdr_data)
        # Start the timer
        self.timer.start()
        self.fetch_and_display_refdr_data()

        
        
        # self.lineEdit_16.textChanged.connect(self.fetch_and_display_test_data)

    def filter_refdr_data(self):
       self.timer.stop()
       doccode = self.lineEdit_18.text()
       docname = self.lineEdit_19.text()
   
       conn = sqlite3.connect('patient_data.db')
       cursor = conn.cursor()
   
       # Fetch reference data
       query = "SELECT * FROM refdr WHERE "
   
       parameters = []
   
       if doccode:
           query += 'DoctorCode LIKE ?'
           parameters.append('%' + doccode + '%')
   
       if docname:
           if doccode:
               query += ' OR '
           query += 'DoctorName LIKE ?'
           parameters.append('%' + docname + '%')
   
       if not doccode and not docname:  # Both line edits are empty
           query = "SELECT * FROM refdr"  # Fetch all data
   
       cursor.execute(query, parameters)
   
       refdr_data = cursor.fetchall()
       self.listWidget.clear()
   
       if refdr_data:
           for row in refdr_data:
               item = QtWidgets.QListWidgetItem()
               self.listWidget.addItem(item)
   
               custom_widget = QtWidgets.QFrame()
               custom_widget.setFrameShape(QtWidgets.QFrame.Box)
               custom_layout = QtWidgets.QHBoxLayout(custom_widget)
               custom_layout.setAlignment(QtCore.Qt.AlignLeft)
   
               spacer = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
               custom_layout.addItem(spacer)
   
               i = 0
               for value in row:
                   if i == 8:
                       continue
   
                   if i == 0:
                       value = f'{value:>10}'
   
                   data_string = f'{value}'
   
                   label = QtWidgets.QLabel(data_string)
                   font = QtGui.QFont("Poppins", 8)
                   label.setFont(font)
   
                   if i == 0:
                       label.setFixedSize(60, 15)
                   elif i == 1:
                       label.setFixedSize(100, 15)
                   elif i == 2:
                       label.setFixedSize(40, 15)
                   elif i == 3:
                       label.setFixedSize(60, 15)
                   elif i == 4:
                       label.setFixedSize(130, 15)
                   elif i == 5:
                       label.setFixedSize(35, 15)
                   elif i == 6:
                       label.setFixedSize(70, 15)
                   elif i == 7:
                       label.setFixedSize(120, 15)
   
                   custom_layout.addWidget(label)
   
                   line_label = QtWidgets.QLabel()
                   line_label.setFrameShape(QtWidgets.QFrame.VLine)
                   line_label.setFrameShadow(QtWidgets.QFrame.Sunken)
                   custom_layout.addWidget(line_label)
   
                   i += 1
   
               button_layout = QtWidgets.QHBoxLayout()
   
               delete_button = QtWidgets.QPushButton()
               delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
               delete_button.setFixedSize(20, 20)
               delete_button.clicked.connect(lambda _, row=row: self.delete_refdr(row[0]))
               button_layout.addWidget(delete_button)
   
               edit_button = QtWidgets.QPushButton()
               edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))
               edit_button.setFixedSize(20, 20)
               edit_button.clicked.connect(lambda _, row=row: self.edit_refdr(row[0]))
               button_layout.addWidget(edit_button)
   
               button_layout.addSpacing(90)
   
               custom_layout.addLayout(button_layout)
               item.setSizeHint(custom_widget.sizeHint())
               self.listWidget.setItemWidget(item, custom_widget)
               item.refdr_data = row


       
       
    
    def fetch_and_display_refdr_data(self):
     
     conn = sqlite3.connect('patient_data.db')
     cursor = conn.cursor()
 
     # Fetch reference data
     cursor.execute("SELECT * FROM refdr")
     refdr_data = cursor.fetchall()
     self.listWidget.clear()
     if refdr_data:
         for row in refdr_data:
             item = QtWidgets.QListWidgetItem()
             self.listWidget.addItem(item)
     
             custom_widget = QtWidgets.QFrame()
             custom_widget.setFrameShape(QtWidgets.QFrame.Box) 
             custom_layout = QtWidgets.QHBoxLayout(custom_widget)
             custom_layout.setAlignment(QtCore.Qt.AlignLeft)

             # Add an empty spacer for spacing above the patient data
            
             spacer = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
             custom_layout.addItem(spacer)

      
            
             i=0
             for value in row:
                               # Create a vertical line (a QLabel with a border)
                    if i==8:
                         continue

                    if i==0:
                        value=f'{value:>10}'
                    
                   
                        # label = QtWidgets.QLabel(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[6]:<10} {row[7]:<10}  ")
                    data_string = f'{value}'

                    label = QtWidgets.QLabel(data_string)
                    font = QtGui.QFont("Poppins", 8)  # Replace "8" with the desired font size
                    label.setFont(font)

                    if i==0:
                            
                            label.setFixedSize(60, 15)
                    elif i==1:
                            
                            label.setFixedSize(100, 15)
                    elif i==2:
                            
                            label.setFixedSize(40, 15)
                    elif i==3:
                            
                            label.setFixedSize(60, 15)
                    elif i==4:
                            label.setFixedSize(130, 15)
                    elif i==5:
                            label.setFixedSize(35, 15)
                    elif i==6:
                            label.setFixedSize(70, 15)
                    elif i==7:
                            label.setFixedSize(120, 15)
                    
                    custom_layout.addWidget(label)

                    line_label = QtWidgets.QLabel()
                    line_label.setFrameShape(QtWidgets.QFrame.VLine)
                    line_label.setFrameShadow(QtWidgets.QFrame.Sunken)
                    custom_layout.addWidget(line_label)

                    i=i+1
             button_layout = QtWidgets.QHBoxLayout()  # Create a layout for the buttons 
             
             delete_button = QtWidgets.QPushButton()
             delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
             delete_button.setFixedSize(20, 20)
             delete_button.clicked.connect(lambda _, row=row: self.delete_refdr(row[0])) 
             button_layout.addWidget(delete_button)
             
             edit_button = QtWidgets.QPushButton()
             edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))  # Change to the correct icon
             edit_button.setFixedSize(20, 20)
             edit_button.clicked.connect(lambda _, row=row: self.edit_refdr(row[0]))
             button_layout.addWidget(edit_button)
             
             
             button_layout.addSpacing(90)
     
             custom_layout.addLayout(button_layout)  # Add the button layout to the custom layout
             item.setSizeHint(custom_widget.sizeHint())
             self.listWidget.setItemWidget(item, custom_widget)
             item.refdr_data = row
 
    def edit_refdr(self, DoctorCode):
        self.edit_refdr_form = QtWidgets.QWidget()
        self.ui_edit_refdr = Ui_editrefdrForm()  # Replace with the correct class name
        self.ui_edit_refdr.setupUi(self.edit_refdr_form, DoctorCode)  # Pass the DoctorCode argument
        self.edit_refdr_form.show()

        # Fetch refdr data for the specified DoctorCode
        refdr_data = self.fetch_refdr_data_by_id(DoctorCode)
        if refdr_data:
            self.edit_refdr_form.refdr_data = refdr_data  
        
        self.edit_refdr_form.show()

        self.listWidget.clear()
        
        self.ui_edit_refdr.pushButton_5.clicked.connect(self.fetch_and_display_refdr_data)

   
    def fetch_refdr_data_by_id(self, DoctorCode):
        # Connect to the database
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()

        # Fetch patient data by ID
        cursor.execute("SELECT * FROM refdr WHERE DoctorCode = ?", (DoctorCode,))
        refdr_data = cursor.fetchone()

        return refdr_data   
   
   
    def delete_refdr(self, DoctorCode):
       # Connect to the database
       conn = sqlite3.connect('patient_data.db')
       cursor = conn.cursor()

       # Delete patient data from the database
       cursor.execute("DELETE FROM refdr WHERE DoctorCode = ?", (DoctorCode,))
       conn.commit()

       # Refresh the displayed patient data immediately after deletion
       self.fetch_and_display_refdr_data()     

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.pushButton_3.setText(_translate("Form", "Add RefDr"))
        self.label_14.setText(_translate("Form", "Actions"))
        self.label_2.setText(_translate("Form", "Doctor Code"))
        self.label_3.setText(_translate("Form", "Doctor Name"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "RefDr Master"))
        self.label_18.setText(_translate("Form", "Mobile"))
        self.label_16.setText(_translate("Form", "Qualification"))
        self.label_12.setText(_translate("Form", "Doctor Name"))
        self.label_19.setText(_translate("Form", "Address"))
        self.label_13.setText(_translate("Form", "Doctor Code"))
        self.label_20.setText(_translate("Form", "Specialisation"))
        self.pushButton_3.clicked.connect(self.open_addrefdr_form)
        self.pushButton.clicked.connect(self.filter_refdr_data)

   
    def open_addrefdr_form(self):
        self.add_test_form = QtWidgets.QWidget()
        self.ui_add_test = Ui_refdrForm()
        self.ui_add_test.setupUi(self.add_test_form)
        self.add_test_form.show()
        self.ui_add_test.pushButton_5.clicked.connect(self.fetch_and_display_refdr_data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_refdrmasterForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
