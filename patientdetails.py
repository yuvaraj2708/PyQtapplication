from PyQt5 import QtCore, QtGui, QtWidgets
from patientregister import Ui_addpatientForm
import sys
import sqlite3
# from addvisit import Ui_addvisitForm
import os
from editpatientregister import Ui_editpatientForm
from PyQt5.QtWidgets import QDateEdit, QCalendarWidget
from PyQt5.QtCore import QTime, QTimer
from registrationsummary import Ui_visitsummaryForm
import sys
import threading
import time
from fpdf import FPDF
from PyQt5.QtCore import * #QObject, pyqtSignal
from PyQt5.QtWidgets import * #QApplication, QLabel, QMainWindow
import qrcode
import barcode
from barcode.writer import ImageWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from report import Ui_reportingForm


class Ui_patientForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 889)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(450, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(870, 290, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 230, 121, 31))
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
        self.label_10.setGeometry(QtCore.QRect(57, 320, 101, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(-200, 320, 1500, 621))
        self.textEdit.setMinimumSize(QtCore.QSize(1500, 0))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(650, 140, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(430, 290, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(630, 290, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(230, 290, 111, 16))
        self.label_11.setObjectName("label_11")
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 70, 161, 31))
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
        self.lineEdit_17 = QtWidgets.QDateEdit(Form)
        self.lineEdit_17.setCalendarPopup(True) 
        self.lineEdit_17.setGeometry(QtCore.QRect(50, 160, 171, 31))
        self.lineEdit_17.setDate(QDate.currentDate())
        self.lineEdit_17.setDisplayFormat("dd-MMM-yyyy")#from date
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_17.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_17.setFrame(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_21 = QtWidgets.QDateEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(250, 160, 171, 31))
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
        self.lineEdit_21.setCalendarPopup(True) 
        self.lineEdit_21.setDate(QDate.currentDate())
        self.lineEdit_21.setDisplayFormat("dd-MMM-yyyy")
        self.lineEdit_21.setFrame(True)# to date
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(650, 160, 171, 31))
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
        self.lineEdit_23 = QtWidgets.QLineEdit(Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(450, 160, 171, 31))#patientname
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
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(70, 290, 101, 16))
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        
        self.pushButton_2.setObjectName("pushButton_2")
        

        self.patient_data = {}
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(-20, 350, 2000, 700))
        self.listWidget.setObjectName("listWidget")

        self.patient_data = {}

      

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # delete_patient_signal = QtCore.pyqtSignal(int)
        # self.lineEdit_16.textChanged.connect(self.fetch_and_display_patient_data)

           # Create a QTimer instance
        self.timer = QTimer(Form)
        # Set the interval to 1000 milliseconds (1 second)
        self.timer.setInterval(1000)
        # Connect the timeout signal to the function you want to call
        self.timer.timeout.connect(self.fetch_and_display_patient_data)
        # Start the timer
        self.timer.start()
       
        self.fetch_and_display_patient_data()
        
    def filter_patient_data(self):
      self.timer.stop()
      patient_name = self.lineEdit_23.text()
      mobile = self.lineEdit_22.text()
      from_date = self.lineEdit_17.date().toPyDate().strftime("%d%m%Y")
      to_date = self.lineEdit_21.date().toPyDate().strftime("%d%m%Y")

      # Connect to the database
      conn = sqlite3.connect('patient_data.db')
      cursor = conn.cursor()

      # Build the SQL query based on the filter criteria
      query = "SELECT * FROM patients WHERE "
      parameters = []

      if patient_name and mobile=='' and from_date=='' and to_date=='':
          query += "patientname LIKE ?"
          parameters.append('%' + patient_name + '%')
  
      elif mobile and patient_name=='' and from_date=='' and to_date=='':
          query += "mobile LIKE ?"
          parameters.append('%'+ mobile + '%')

      elif patient_name and mobile and from_date=='' and to_date=='':
          query += "patientname LIKE ? AND mobile LIKE ?"
          parameters.extend(['%'+patient_name+'%', '%'+mobile+'%'])
  
      elif from_date and to_date and mobile=='' and patient_name=='':
            query += "date BETWEEN ? AND ?"
            parameters.extend([from_date, to_date])
        
      elif from_date and to_date and mobile and patient_name:
            query+='date between ? and ? and mobile like ? and patientname like ?'
            parameters.extend([from_date,to_date,'%'+mobile+'%','%'+patient_name+'%'])

      elif from_date and to_date and mobile and patient_name=='':
          query+='(date between ? and ?) and mobile like ?'
          parameters.extend([from_date,to_date,'%'+mobile+'%'])

      elif from_date and to_date and mobile == '' and patient_name:
          query+='(date between ? and ?) and patientname like ?'
          parameters.extend([from_date,to_date,'%'+patient_name+'%'])

      # Fetch patient data with filters applied
      cursor.execute(query, parameters)
      filtered_patient_data = cursor.fetchall()
      
      # Clear the existing items in the QListWidget
      self.listWidget.clear()

      if filtered_patient_data:
          for row in filtered_patient_data:
              item = QtWidgets.QListWidgetItem()
              self.listWidget.addItem(item)

            #   custom_widget = QtWidgets.QWidget()
            #   custom_layout = QtWidgets.QHBoxLayout(custom_widget)

            #   label = QtWidgets.QLabel(
            #       f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[6]:<10} {row[7]:<10} {row[8]:<40}")
            #   custom_layout.addWidget(label)


              custom_widget = QtWidgets.QFrame()
              custom_widget.setFrameShape(QtWidgets.QFrame.Box) 
              custom_layout = QtWidgets.QHBoxLayout(custom_widget)
              custom_layout.setAlignment(QtCore.Qt.AlignLeft)
            
                    # Add an empty spacer for spacing above the patient data
                  

                    
                    

              i=0
              for value in row:
                               # Create a vertical line (a QLabel with a border)
                        
                        if i==0:
                            value=f'{value:>15}'
                        if i==10:
                            continue 

                        data_string = f'{value}'
                        label = QtWidgets.QLabel(data_string)
                        font = QtGui.QFont("Poppins", 8)  # Replace "8" with the desired font size
                        label.setFont(font)
                        #label.setFixedSize(60, 10)

                        if i==0:
                            
                            label.setFixedSize(70, 15)
                        elif i==1:
                            
                            label.setFixedSize(70, 15)
                        elif i==2:
                            
                            label.setFixedSize(20, 15)
                        elif i==3:
                            
                            label.setFixedSize(80, 15)
                        elif i==4:
                            label.setFixedSize(30, 15)
                        elif i==5:
                            label.setFixedSize(50, 15)
                        elif i==6:
                            label.setFixedSize(50, 15)
                        elif i==7:
                            label.setFixedSize(70, 15)
                        elif i==8:
                            label.setFixedSize(120, 15) 
                        elif i==9:
                            label.setFixedSize(70, 15)
                        
                        custom_layout.addWidget(label)

                        line_label = QtWidgets.QLabel()
                        line_label.setFrameShape(QtWidgets.QFrame.VLine)
                        line_label.setFrameShadow(QtWidgets.QFrame.Sunken)
                        if i==1 or i==6 or i==8 or i==9:
                            i=i+1
                            continue
                        
                        custom_layout.addWidget(line_label)


                        i=i+1

              button_layout = QtWidgets.QHBoxLayout()  # Create a layout for the buttons
              # Add buttons and layout as needed
              # ...

              delete_button = QtWidgets.QPushButton()
              delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
              delete_button.setFixedSize(20, 20)
              delete_button.clicked.connect(lambda _, row=row: self.delete_patient(row[0])) 
              button_layout.addWidget(delete_button)
                
              edit_button = QtWidgets.QPushButton()
              edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))  # Change to the correct icon
              edit_button.setFixedSize(20, 20)
              edit_button.clicked.connect(lambda _, row=row: self.edit_patient(row[0]))
              button_layout.addWidget(edit_button)
              
                
            #   add_visit_button = QtWidgets.QPushButton()
            #   add_visit_button.setIcon(QtGui.QIcon(os.path.join('images', 'addvisit.png')))
            #   add_visit_button.setFixedSize(20, 20)
            #   add_visit_button.clicked.connect(lambda _, row=row: self.open_add_visit_form(row))
            #   button_layout.addWidget(add_visit_button)
              
              more_button = QtWidgets.QPushButton()
              more_button.setIcon(QtGui.QIcon(os.path.join('images', 'qr.png')))
              more_button.setFixedSize(20, 20)
              more_button.clicked.connect(lambda _, row=row: self.generate_qr_code_pdf())
              button_layout.addWidget(more_button)
              
              more_button = QtWidgets.QPushButton()
              more_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
              more_button.setFixedSize(20, 20)
              more_button.clicked.connect(lambda _, row=row: self.generate_bar_code_pdf(row))
              button_layout.addWidget(more_button)
              # Add spacing between the label and buttons
              
              more_button = QtWidgets.QPushButton()
              more_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
              more_button.setFixedSize(20, 20)
              more_button.clicked.connect(lambda _, row=row: self.open_add_report_form(row))
              button_layout.addWidget(more_button)
              
              more_button = QtWidgets.QPushButton()
              more_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
              more_button.setFixedSize(20, 20)
              more_button.clicked.connect(lambda _, row=row: self.generate_bar_code_pdf(row))
              button_layout.addWidget(more_button)
              
              
                
                    # Add spacing between the label and buttons
              button_layout.addSpacing(90)
                

  
              spacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
              button_layout.addItem(spacer)  # Add an expanding spacer between buttons
  
              custom_layout.addLayout(button_layout)
              item.setSizeHint(custom_widget.sizeHint())
              self.listWidget.setItemWidget(item, custom_widget)
              item.patient_data = row
  
      else:
          # Handle case when no matching records are found
          pass
  
      conn.close()
  

    
    
    def fetch_and_display_patient_data(self):
        
        # Connect to the database
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()

        # Fetch patient data
        cursor.execute("SELECT * FROM patients")
        patient_data = cursor.fetchall()
        self.listWidget.clear()
        # Get the existing patient IDs already displayed
        existing_patient_ids = [item.patient_data[0] for item in self.listWidget.findItems("", QtCore.Qt.MatchContains)]

        if patient_data:
            for row in patient_data:
                patient_id = row[0]
                
                # Check if the patient ID is already displayed, if not, add it
                if patient_id not in existing_patient_ids:
                    item = QtWidgets.QListWidgetItem()
                    self.listWidget.addItem(item)
                
                    #custom_widget = QtWidgets.QWidget()
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
                        
                        if i==0:
                            value=f'{value:>10}'
                        if i==10:
                            continue   

                        data_string = f'{value}'
                        label = QtWidgets.QLabel(data_string)
                        font = QtGui.QFont("Poppins", 8)  # Replace "8" with the desired font size
                        label.setFont(font)
                        #label.setFixedSize(60, 10)

                        if i==0:
                            
                            label.setFixedSize(50, 15)
                        elif i==1:
                            
                            label.setFixedSize(70, 15)
                        elif i==2:
                            
                            label.setFixedSize(20, 15)
                        elif i==3:
                            
                            label.setFixedSize(80, 15)
                        elif i==4:
                            label.setFixedSize(30, 15)
                        elif i==5:
                            label.setFixedSize(50, 15)
                        elif i==6:
                            label.setFixedSize(50, 15)
                        elif i==7:
                            label.setFixedSize(70, 15)
                        elif i==8:
                            label.setFixedSize(120, 15) 
                        elif i==9:
                            label.setFixedSize(70, 15)
                        
                        custom_layout.addWidget(label)

                        line_label = QtWidgets.QLabel()
                        line_label.setFrameShape(QtWidgets.QFrame.VLine)
                        line_label.setFrameShadow(QtWidgets.QFrame.Sunken)
                        if i==1 or i==6 or i==8 or i==9:
                            i=i+1
                            continue
                        
                        custom_layout.addWidget(line_label)


                        i=i+1
                    
                    button_layout = QtWidgets.QHBoxLayout()  # Create a layout for the buttons
                    button_layout.setAlignment(QtCore.Qt.AlignLeft)

                    delete_button = QtWidgets.QPushButton()
                    delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
                    delete_button.setFixedSize(20, 20)
                    delete_button.clicked.connect(lambda _, row=row: self.delete_patient(row[0])) 
                    button_layout.addWidget(delete_button)
                
                    edit_button = QtWidgets.QPushButton()
                    edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))  # Change to the correct icon
                    edit_button.setFixedSize(20, 20)
                    edit_button.clicked.connect(lambda _, row=row: self.edit_patient(row[0]))
                   
                    
                    button_layout.addWidget(edit_button)
                
                    # add_visit_button = QtWidgets.QPushButton()
                    # add_visit_button.setIcon(QtGui.QIcon(os.path.join('images', 'addvisit.png')))
                    # add_visit_button.setFixedSize(20, 20)
                    # add_visit_button.clicked.connect(lambda _, row=row: self.open_add_visit_form(row))
                    # button_layout.addWidget(add_visit_button)
                    
                    more_button = QtWidgets.QPushButton()
                    more_button.setIcon(QtGui.QIcon(os.path.join('images', 'qr.png')))
                    more_button.setFixedSize(20, 20)
                    more_button.clicked.connect(lambda _, row=row: self.generate_qr_code_pdf())
                    button_layout.addWidget(more_button)
                    
                    more_button = QtWidgets.QPushButton()
                    more_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
                    more_button.setFixedSize(20, 20)
                    more_button.clicked.connect(lambda _, row=row: self.generate_bar_code_pdf(row))
                    button_layout.addWidget(more_button)
                    # Add spacing between the label and buttons
                  #  button_layout.addSpacing(90 00000)
                    more_button = QtWidgets.QPushButton()
                    more_button.setIcon(QtGui.QIcon(os.path.join('images', 'report.png')))
                    more_button.setFixedSize(20, 20)
                    more_button.clicked.connect(lambda _, row=row: self.open_add_report_form(row))
                    button_layout.addWidget(more_button)
                    
                    more_button = QtWidgets.QPushButton()
                    more_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
                    more_button.setFixedSize(20, 20)
                    more_button.clicked.connect(lambda _, row=row: self.generate_bar_code_pdf(row))
                    button_layout.addWidget(more_button)
                    
                    custom_layout.addLayout(button_layout)  # Add the button layout to the custom layout
                    item.setSizeHint(custom_widget.sizeHint())
                    self.listWidget.setItemWidget(item, custom_widget)
                    item.patient_data = row
    
    def open_add_report_form(self ,visit_data):
        #self.timer.start()
        self.add_test_form = QtWidgets.QWidget()
        self.ui_add_test = Ui_reportingForm()
        self.ui_add_test.setupUi(self.add_test_form)
        
        self.ui_add_test.set_patient_data(visit_data)
        
        self.add_test_form.show()   
        
    def generate_bar_code_pdf(self, accession):
        # Extract the accession number from the row, assuming it's in a specific column (adjust as needed).
        accession_number = accession[11]  # Assuming the accession number is in the second column (change as needed)
        accession_str = str(accession_number)
    
        # Define the barcode dimensions (adjust as needed)
        barcode_width = 200
        barcode_height = 50
    
        # Generate the barcode image using the string representation of the accession number and save it to a file.
        barcode.generate('Code128', accession_str, writer=ImageWriter(), output=os.path.join('images', 'barcode'))
    
        # Create a PDF with the barcode image.
        pdf_filename = f'barcode_{accession_number}.pdf'
        c = canvas.Canvas(pdf_filename, pagesize=letter)
    
        # Adjust the x, y, width, and height to position and size the barcode as needed.
        x = 100  # Adjust the x-coordinate as needed
        y = 500  # Adjust the y-coordinate as needed
    
        c.drawImage(os.path.join('images', 'barcode.png'), x, y, width=barcode_width, height=barcode_height)
        c.showPage()
        c.save()
    
        # Optionally, you can open the generated PDF.
        os.system(pdf_filename)


    
    
        
    def generate_qr_code_pdf(self):
    # visit_id, ref_dr, patient_category, patient_name, dob, age, gender, mobile, email, date, selected_test,acc= visit_data
 
     # Retrieve patient information based on patient_id from the patients table
     conn = sqlite3.connect('patient_data.db')
     cursor = conn.cursor()
 
     cursor.execute("""
             SELECT  patients.refdr, 
                    patients.patientname, patients.dob, patients.age, patients.gender, 
                    patients.mobile, patients.email, patients.date, patients.selected_test,patients.uhid
             FROM patients
             
         """)
     patient_info = cursor.fetchone()
 
     conn.close()
 
     if patient_info:
        ref_dr,patientname,dob, age, gender, mobile, email, date, selected_test,patient_id = patient_info

        # Create a formatted string with all the details
        details_string = (
            # f"Visit ID: {visit_id}\n"
            f"Patient ID: {patient_id}\n"
            f"Patient Name: {patientname}\n"
            f"DOB: {dob}\n"
            f"Age: {age}\n"
            f"Gender: {gender}\n"
            f"Mobile: {mobile}\n"
            f"Email: {email}\n"
            f"Referring Doctor: {ref_dr}\n"
            f"Selected Test: {selected_test}\n"
            f"Date: {date}\n"
        )

        # Generate the QR code using the formatted details string
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(details_string)
        qr.make(fit=True)

        # Generate the QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(f'qr_code_{patient_id}.png')

        # Create a PDF with mm as the unit
        pdf = FPDF()

        # Calculate the position and size for the QR code within the page
        x_position = (150 - 15) / 2  # Center the QR code horizontally
        y_position = (150 - 15) / 2  # Center the QR code vertically
        qr_size = 15

        # Set the page size to 15mm x 15mm by modifying the _page_format attribute
        pdf._page_format = [qr_size, qr_size]

        # Add a page
        pdf.add_page()

        # Add the QR code to the PDF
        pdf.image(f'qr_code_{patient_id}.png', x=x_position, y=y_position, w=qr_size)

        # Add visit details to the PDF
        pdf.set_font("Arial", size=8)
        pdf.multi_cell(150, 10, details_string, border=0, align="L")

        # Set the PDF file path
        pdf_file_path = f'qr_code_{patient_id}.pdf'

        # Output the PDF file
        pdf.output(pdf_file_path)

        QtWidgets.QMessageBox.information(
            None, 'QR Code PDF',
            f'QR code PDF for Visit ID {patient_id} has been generated as "{pdf_file_path}"'
        )


    def edit_patient(self, patient_uhid):
        
        self.edit_patient_form = QtWidgets.QWidget()
        self.ui_edit_patient = Ui_editpatientForm()  # Replace with the correct class name
        self.ui_edit_patient.setupUi(self.edit_patient_form, patient_uhid)  # Pass the patient ID
        #self.edit_patient_form.show()
        # Fetch patient data for the specified patient_id
        patient_data = self.fetch_patient_data_by_id(patient_uhid)
        if patient_data:
            self.ui_edit_patient.patient_data = patient_data  # Set the patient data in the edit form

        self.edit_patient_form.show()
        self.listWidget.clear()
        
        self.ui_edit_patient.pushButton_3.clicked.connect(self.fetch_and_display_patient_data)
        
       

    def fetch_patient_data_by_id(self, patient_uhid):
        # Connect to the database
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()

        # Fetch patient data by ID
        cursor.execute("SELECT * FROM patients WHERE uhid = ?", (patient_uhid,))
        patient_data = cursor.fetchone()

        return patient_data   
    
     
    def delete_patient(self, patient_uhid):
       
       # Connect to the database
       conn = sqlite3.connect('patient_data.db')
       cursor = conn.cursor()

       # Delete patient data from the database
       cursor.execute("DELETE FROM patients WHERE uhid = ?", (patient_uhid,))
       conn.commit()
       self.listWidget.clear()
       # Refresh the displayed patient data immediately after deletion
       self.fetch_and_display_patient_data()
       
            
    # def open_add_visit_form(self, patient_data):
    #     self.add_visit_form = QtWidgets.QWidget()
    #     self.ui_add_visit = Ui_addvisitForm()
    #     self.ui_add_visit.setupUi(self.add_visit_form)

    #     # Pass patient data to Ui_addvisitForm
    #     self.ui_add_visit.set_patient_data(patient_data)
    #     self.listWidget.clear()
    #     self.obj_form=QtWidgets.QWidget()
    #     self.obj=Ui_visitsummaryForm()
    #     self.obj.setupUi(self.obj_form)
    #     self.obj.timer.start()

    #     self.add_visit_form.show()

        



       

     
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.label.setText(_translate("Form", "Registration Summary"))
        self.label_2.setText(_translate("Form", "From Date"))
        self.label_5.setText(_translate("Form", "Mobile"))
        self.label_14.setText(_translate("Form", "Email ID"))
        self.label_3.setText(_translate("Form", "To Date"))
        self.label_12.setText(_translate("Form", "Mobile"))
        self.label_13.setText(_translate("Form", "Actions"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_10.setText(_translate("Form", "Date / UHID"))
        self.label_4.setText(_translate("Form", "Patient Name"))
        self.label_11.setText(_translate("Form", "Patient Details"))
        self.pushButton_2.setText(_translate("Form", "Add Patient"))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_add_patient_form) 
        self.pushButton.clicked.connect(self.filter_patient_data)
        
    def open_add_patient_form(self):
        #self.timer.start()
        self.add_test_form = QtWidgets.QWidget()
        self.ui_add_test = Ui_addpatientForm()
        self.ui_add_test.setupUi(self.add_test_form)
        self.add_test_form.show()
        self.ui_add_test.pushButton_2.clicked.connect(self.fetch_and_display_patient_data)
        # self.fetch_and_display_patient_data()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_patientForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
    