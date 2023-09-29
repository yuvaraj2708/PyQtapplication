from PyQt5 import QtCore, QtGui, QtWidgets
from patientregister import Ui_addpatientForm
import sys
import sqlite3
# from addvisit import Ui_addvisitForm
import os
from editpatientregister import Ui_editpatientForm
from PyQt5.QtWidgets import QDateEdit, QCalendarWidget
from PyQt5.QtCore import QTime, QTimer
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
from PyQt5.QtGui import QIcon, QPixmap, QFont

class Ui_patientForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(835, 552)
        Form.showMaximized() 
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(55)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font_poppins = QFont("Poppins", 15)
        #Form.setStyleSheet("backgound-color:white;")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QLineEdit{\n"
"height:40px;\n"
"}\n"
"QDateEdit{\n"
"height:40px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 50, 70, 50)
        self.gridLayout.setHorizontalSpacing(21)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(179, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(179, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet(
    "QLineEdit {"
    "    font-size: 15px;"
    "    font-weight: 400;"
    "    color: #212529;"
    "    background-color: #ffffff;"
    "    background-clip: padding-box;"
    "    border: 1px solid #ced4da;"
    "    border-radius: 1px;"
    "    padding: 0px 10px;"
    "}"
    "QLineEdit:focus {"
    "    border: 1px solid #3F4254;"
    "}"
)
        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(179, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(179, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")


        self.lineEdit_3.setStyleSheet(
    "QLineEdit {"
    "    font-size: 15px;"
    "    font-weight: 400;"
    "    color: #212529;"
    "    background-color: #ffffff;"
    "    background-clip: padding-box;"
    "    border: 1px solid #ced4da;"
    "    border-radius: 1px;"
    "    padding: 0px 10px;"
    "}"
    "QLineEdit:focus {"
    "    border: 1px solid #3F4254;"
    "}"
)
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setMaximumDate(QDate.currentDate())
        self.dateEdit.setDisplayFormat("dd-MMM-yyyy")
        self.dateEdit.setMinimumSize(QtCore.QSize(155, 40))
        self.dateEdit.setMaximumSize(QtCore.QSize(183, 40))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet(
    "QDateEdit {"
    "    font-size: 15px;"
    "    font-weight: 400;"
    "    color: #212529;"
    "    background-color: #ffffff;"
    "    background-clip: padding-box;"
    "    border: 1px solid #ced4da;"
    "    border-radius: 1000px;"
    "    padding: 0px 10px;"
    "}"
    "QDateEdit::drop-down {"
    "    subcontrol-origin: padding;"
    "    subcontrol-position: right center;"
    "    width: 20px;"
    "    border: none;"
    "    background-color: #ffffff;"
    "}"
    "QDateEdit::down-arrow {"
    "    image: url(down_arrow.png);"
    "}"
    "QDateEdit:focus {"
    "    border: 1px solid #3F4254;"
    "}"
)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setMaximumDate(QDate.currentDate())
        self.dateEdit_2.setDisplayFormat("dd-MMM-yyyy")
        self.dateEdit_2.setMinimumSize(QtCore.QSize(150, 40))
        self.dateEdit_2.setMaximumSize(QtCore.QSize(179, 40))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setStyleSheet(
    "QDateEdit {"
    "    font-size: 15px;"
    "    font-weight: 400;"
    "    color: #212529;"
    "    background-color: #ffffff;"
    "    background-clip: padding-box;"
    "    border: 1px solid #ced4da;"
    "    border-radius: 1000px;"
    "    padding: 0px 10px;"
    "}"
    "QDateEdit::drop-down {"
    "    subcontrol-origin: padding;"
    "    subcontrol-position: right center;"
    "    width: 20px;"
    "    border: none;"
    "    background-color: #ffffff;"
    "}"
    "QDateEdit::down-arrow {"
    "    image: url(down_arrow.png);"
    "}"
    "QDateEdit:focus {"
    "    border: 1px solid #3F4254;"
    "}"
)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QDate.currentDate())

        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setFont(font_poppins)
        self.pushButton_2.setStyleSheet("margin-right:10px;\n"
"height:70px;\n"
"width:120px;\n"
"background-color: #0DBCC0;\n"
"color:white;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"margin-top:5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_3.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/qr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 3, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("margin-right:10px;\n"
"height:40px;\n"
"width:120px;\n"
"background-color: #0DBCC0;\n"
"color:white;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    
    def fetch_and_display_patient(self):

        self.tableWidget.setColumnCount(12)
        self.tableWidget.setColumnWidth(0,70)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,70)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setColumnWidth(5,100)
        self.tableWidget.setColumnWidth(6,50)
        self.tableWidget.setColumnWidth(7,100)
        self.tableWidget.setColumnWidth(8,170)
        self.tableWidget.setColumnWidth(9,100)
        self.tableWidget.setColumnWidth(10,70)
        self.tableWidget.setColumnWidth(11,130)
        
        self.tableWidget.setHorizontalHeaderLabels(['UHID','Date','Title','Patient Name','Gender','DOB','Age','Mobile','Email','Ref Dr','Accession','Actions'])
        #set header height
        vertical_header = self.tableWidget.verticalHeader()
        vertical_header.setDefaultSectionSize(40) 


        conn=sqlite3.connect('patient_data.db')
        cursor=conn.cursor()
        cursor.execute("SELECT uhid,date,title,patientname,gender,dob,age,mobile,email,refdr,accession FROM patients")
        patient_data = cursor.fetchall()
        count=len(patient_data)
        
        self.tableWidget.setRowCount(count)
        r=0
        c=0
        for row in patient_data:
            c=0
            for col in row:
                self.tableWidget.setItem(r,c,QTableWidgetItem("   "+str(col)))
                c=c+1
            # Create a container widget to hold the "Edit" and "Delete" buttons
            button_container = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout(button_container)

            delete_button = QtWidgets.QPushButton()
            delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
            delete_button.setFixedSize(20, 20)
            delete_button.clicked.connect(lambda _, uhid=row[0]: self.delete_patient(uhid))
            button_layout.addWidget(delete_button)

            edit_button = QtWidgets.QPushButton()
            edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))  # Change to the correct icon
            edit_button.setFixedSize(20, 20)
            edit_button.clicked.connect(lambda _, uhid=row[0]: self.edit_patient(uhid))
            button_layout.addWidget(edit_button)

            qr_code_button = QtWidgets.QPushButton()
            qr_code_button.setIcon(QtGui.QIcon(os.path.join('images', 'qr.png')))
            qr_code_button.setFixedSize(20, 20)
            qr_code_button.clicked.connect(lambda _, row=row[0]: self.generate_qr_code_pdf(row))
            button_layout.addWidget(qr_code_button)

            bar_code_button = QtWidgets.QPushButton()
            bar_code_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
            bar_code_button.setFixedSize(20, 20)
            bar_code_button.clicked.connect(lambda _, row=row[10]: self.generate_bar_code_pdf(row))
            button_layout.addWidget(bar_code_button)

            more_button = QtWidgets.QPushButton()
            more_button.setIcon(QtGui.QIcon(os.path.join('images', 'report.png')))
            more_button.setFixedSize(20, 20)
            more_button.clicked.connect(lambda _, row=row: self.open_add_report_form(row[0]))
            button_layout.addWidget(more_button)
            
            more_button = QtWidgets.QPushButton()
            more_button.setIcon(QtGui.QIcon(os.path.join('images', 'print.png')))
            more_button.setFixedSize(20, 20)
            more_button.clicked.connect(lambda _, row=row: self.display_report_details(row[0]))
            button_layout.addWidget(more_button)
            
            more_button = QtWidgets.QPushButton()
            more_button.setIcon(QtGui.QIcon(os.path.join('images', 'share.png')))
            more_button.setFixedSize(20, 20)
            button_layout.addWidget(more_button)
            


            self.checkbox=QtWidgets.QCheckBox()
            self.checkbox.setChecked(False)
            self.checkbox.stateChanged.connect(lambda _,row=row: self.addqr(row[0]))
            button_layout.addWidget(self.checkbox)


            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setAlignment(QtCore.Qt.AlignCenter)

            # Set the container widget as a cell widget in the last column
            self.tableWidget.setCellWidget(r, c, button_container)
            r=r+1
    
    def open_add_report_form(self ,visit_data):
        #self.timer.start()
        self.add_test_form = QtWidgets.QWidget()
        self.ui_add_test = Ui_reportingForm()
        self.ui_add_test.setupUi(self.add_test_form)
        
        self.ui_add_test.set_patient_data(visit_data)
        
        self.add_test_form.show()   
    
    
    def filter_patient_data(self):
      

      self.tableWidget.setColumnCount(12)
      self.tableWidget.setColumnWidth(0,70)
      self.tableWidget.setColumnWidth(1,100)
      self.tableWidget.setColumnWidth(2,70)
      self.tableWidget.setColumnWidth(3,100)
      self.tableWidget.setColumnWidth(4,100)
      self.tableWidget.setColumnWidth(5,100)
      self.tableWidget.setColumnWidth(6,50)
      self.tableWidget.setColumnWidth(7,100)
      self.tableWidget.setColumnWidth(8,170)
      self.tableWidget.setColumnWidth(9,100)
      self.tableWidget.setColumnWidth(10,70)
      self.tableWidget.setColumnWidth(11,130)
        
      self.tableWidget.setHorizontalHeaderLabels(['UHID','Date','Title','Patient Name','Gender','Dob','Age','Mobile','Email','Ref Dr','Accession','Actions'])
        #set header height
      vertical_header = self.tableWidget.verticalHeader()
      vertical_header.setDefaultSectionSize(40) 
      patient_name = self.lineEdit_3.text()
      mobile = self.lineEdit_4.text()
      from_date = self.dateEdit.date().toPyDate().strftime("%d%m%Y")
      to_date = self.dateEdit_2.date().toPyDate().strftime("%d%m%Y")

      # Connect to the database
      conn = sqlite3.connect('patient_data.db')
      cursor = conn.cursor()

      # Build the SQL query based on the filter criteria
      query = "SELECT uhid,date,title,patientname,gender,dob,age,mobile,email,refdr,accession FROM patients WHERE "
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
      filter_patient_data = cursor.fetchall()
      count=len(filter_patient_data)
        
      self.tableWidget.setRowCount(count)
      r=0
      c=0
      for row in filter_patient_data:
            c=0
            for col in row:
                self.tableWidget.setItem(r,c,QTableWidgetItem("   "+str(col)))
                c=c+1
            # Create a container widget to hold the "Edit" and "Delete" buttons
            button_container = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout(button_container)

            delete_button = QtWidgets.QPushButton()
            delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
            delete_button.setFixedSize(20, 20)
            delete_button.clicked.connect(lambda _, uhid=row[0]: self.delete_patient(uhid))
            button_layout.addWidget(delete_button)

            edit_button = QtWidgets.QPushButton()
            edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))  # Change to the correct icon
            edit_button.setFixedSize(20, 20)
            edit_button.clicked.connect(lambda _, uhid=row[0]: self.edit_patient(uhid))
            button_layout.addWidget(edit_button)

            qr_code_button = QtWidgets.QPushButton()
            qr_code_button.setIcon(QtGui.QIcon(os.path.join('images', 'qr.png')))
            qr_code_button.setFixedSize(20, 20)
            qr_code_button.clicked.connect(lambda _, row=row[0]: self.generate_qr_code_pdf(row))
            button_layout.addWidget(qr_code_button)

            bar_code_button = QtWidgets.QPushButton()
            bar_code_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
            bar_code_button.setFixedSize(20, 20)
            bar_code_button.clicked.connect(lambda _, row=row[10]: self.generate_bar_code_pdf(row))
            button_layout.addWidget(bar_code_button)

            more_button = QtWidgets.QPushButton()
            more_button.setIcon(QtGui.QIcon(os.path.join('images', 'report.png')))
            more_button.setFixedSize(20, 20)
            more_button.clicked.connect(lambda _, row=row: self.open_add_report_form(row[0]))
            button_layout.addWidget(more_button)
            
            more_button = QtWidgets.QPushButton()
            more_button.setIcon(QtGui.QIcon(os.path.join('images', 'print.png')))
            more_button.setFixedSize(20, 20)
            more_button.clicked.connect(lambda _, report_id=row[0]: self.display_report_details(report_id))
            button_layout.addWidget(more_button)
            
            more_button = QtWidgets.QPushButton()
            more_button.setIcon(QtGui.QIcon(os.path.join('images', 'share.png')))
            more_button.setFixedSize(20, 20)
            button_layout.addWidget(more_button)


            self.checkbox=QtWidgets.QCheckBox()
            self.checkbox.setChecked(False)
            self.checkbox.stateChanged.connect(lambda _,row=row: self.addqr(row[0]))
            button_layout.addWidget(self.checkbox)


            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setAlignment(QtCore.Qt.AlignCenter)

            # Set the container widget as a cell widget in the last column
            self.tableWidget.setCellWidget(r, c, button_container)
            r=r+1
    
    def display_report_details(self, patient_id):
     connection = sqlite3.connect("patient_data.db")  # Replace with your actual database file
     cursor = connection.cursor()

     # Fetch details for the given patient_id
     cursor.execute("SELECT * FROM patient_reports WHERE report_id = ?", (patient_id,))
     report_details = cursor.fetchone()
     print(report_details)
     # Check if report_details is not None (i.e., the patient_id exists)
     if report_details:
         report_id, patient_name, report_template, pathologist, report_content, report_date = report_details
         print(f"Report ID: {report_id}")
         print(f"Patient Name: {patient_name}")
         print(f"Report Template: {report_template}")
         print(f"Pathologist: {pathologist}")
         print(f"Report Content: {report_content}")
         print(f"Report Date: {report_date}")
     else:
         print(f"Report with ID {patient_id} not found.")

     connection.close()
    
    
    def addqr(self, id):

        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()

        # Create the qrcodetable table with the 'id' column as Integer and NOT NULL
        cursor.execute("CREATE TABLE IF NOT EXISTS qrcodetable (id INTEGER NOT NULL);")

        cursor.execute("SELECT * FROM qrcodetable")
        all_ids = [row[0] for row in cursor.fetchall()]


        if id in all_ids:
            # Use the DELETE statement to remove rows with a specific ID
            cursor.execute("DELETE FROM qrcodetable WHERE id = ?", (id,))
        else:
            # Use the INSERT statement to insert a single value
            cursor.execute("INSERT INTO qrcodetable VALUES (?)", (id,))

        # Commit the changes to the database
        conn.commit()
        conn.close()


    def selected_qrcode_generate(self):
        
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()
    
        
        cursor.execute("SELECT * FROM patients INNER JOIN qrcodetable ON patients.uhid == qrcodetable.id")
        patient_info_all = cursor.fetchall()
        
    
        conn.close()
        img_group=[]
        for patient_info in patient_info_all:
            if patient_info:
                
               # visit_id, ref_dr, patient_category, patientname, gender, dob, age, mobile, email, date, selected_test,patient_id = patient_info
                uhid,date,title,patientname,dob,age,gender,mobile,email,refdr,selectedtest,accession,id=patient_info
                # Create a formatted string with all the details
                details_string = (
                    #f"Visit ID: {visit_id}\n"
                    f"Patient ID: {uhid}\n"
                    f"Patient Name: {title} {patientname}\n"
                    f"DOB: {dob}\n"
                    f"Age: {age}\n"
                    f"Gender: {gender}\n"
                    f"Mobile: {mobile}\n"
                    f"Email: {email}\n"
                   # f"Patient Category: {patient_category}\n"
                    f"Referring Doctor: {refdr}\n"
                    f"Selected Test: {selectedtest}\n"
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
                
                qr_img.save(f'qr_code_{id}.png')
                img_group.append(f'qr_code_{id}.png')

        pdf = FPDF()
        pdf.add_page()

        # Loop through the image paths and add each image to the PDF along with patient names
        x_size = 10
        y_size = 10
        c = 0
        for patient_info, img_path in zip(patient_info_all, img_group):
            if not patient_info:
                continue
                
            uhid, date, title, patientname, dob, age, gender, mobile, email, refdr, selectedtest, accession, id = patient_info

            # Add patient name above the QR code
            pdf.set_xy(x_size, y_size - 5)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, patientname + "|" + uhid, align='L')
            # Add the QR code image
            pdf.image(img_path, x=x_size, y=y_size + 5, w=30)  # Adjust y and w as needed

            x_size = x_size + 33
            c = c + 1
            if c % 5 == 0:
                y_size = y_size + 50
                x_size = 10
            if y_size == 240:
                pdf.add_page()

        # Output the PDF
        pdf.output("qrcodes.pdf")

                
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()
    
        cursor.execute("""
                delete from qrcodetable
            """)
        conn.commit()
    
        conn.close()
        self.fetch_and_display_patient()
        

    def addpatient(self):
        self.add_test_form = QtWidgets.QWidget()
        self.ui_add_test = Ui_addpatientForm()
        self.ui_add_test.setupUi(self.add_test_form)
        self.add_test_form.show()
        self.ui_add_test.pushButton_3.clicked.connect(self.fetch_and_display_patient)

    def delete_patient(self, patient_uhid):
    # Create a confirmation dialog
      confirm_dialog = QMessageBox()
      confirm_dialog.setIcon(QMessageBox.Question)
      confirm_dialog.setText("Are you sure you want to delete this patient?")
      confirm_dialog.setWindowTitle("Confirm Deletion")
      confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
  
      # Show the dialog and wait for the user's response
      response = confirm_dialog.exec_()
  
      # If the user confirms deletion, proceed with deletion
      if response == QMessageBox.Yes:
          # Connect to the database
          conn = sqlite3.connect('patient_data.db')
          cursor = conn.cursor()
  
          # Delete patient data from the database
          cursor.execute("DELETE FROM patients WHERE uhid = ?", (patient_uhid,))
          conn.commit()
  
          # Refresh the displayed patient data immediately after deletion
          self.fetch_and_display_patient()
  
  
    def edit_patient(self, patient_uhid):
        
        self.edit_patient_form = QtWidgets.QWidget()
        self.ui_edit_patient = Ui_editpatientForm()  # Replace with the correct class name
        self.ui_edit_patient.setupUi(self.edit_patient_form, patient_uhid)  # Pass the patient ID
        #self.edit_patient_form.show()
        # Fetch patient data for the specified patient_id
       # patient_data = self.fetch_patient_data_by_id(patient_uhid)
       # if patient_data:
        #    self.ui_edit_patient.patient_data = patient_data  # Set the patient data in the edit form

        self.edit_patient_form.show()
        self.ui_edit_patient.pushButton_3.clicked.connect(self.fetch_and_display_patient)


    def generate_bar_code_pdf(self, access):
        barcode.generate('Code128', str(access), output=os.path.join('images', 'barcode1'))
        x = 100  # Adjust the x-coordinate as needed
        y = 500  # Adjust the y-coordinate as needed
        width = 200  # Adjust the width as needed
        height = 50  
        # Create a PDF with the barcode image.
        pdf_filename = f'barcode_{access[1]}.pdf'
        c = canvas.Canvas(pdf_filename)
        c.drawImage(os.path.join('images', 'barcode.png'),x,y,height=100)  # Adjust x, y, width, height as needed
        c.showPage()
        c.save()

        # Optionally, you can open the generated PDF.
        os.system(pdf_filename)



    def generate_qr_code_pdf(self,pid):
    # visit_id, ref_dr, patient_category, patient_name, dob, age, gender, mobile, email, date, selected_test,acc= visit_data
 
        # Retrieve patient information based on patient_id from the patients table
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()
    
        # cursor.execute("""
        #         SELECT visit.visitid, visit.ref_dr, visit.patient_category,
        #                 patients.patientname, patients.dob, patients.age, patients.gender, 
        #                 patients.mobile, patients.email, visit.date, visit.selected_test,patients.uhid
        #         FROM visit
        #         INNER JOIN patients ON visit.patient_id = patients.uhid
        #     """)
        cursor.execute("SELECT * FROM patients where uhid==?",(pid,))
        patient_info = cursor.fetchone()
    
        conn.close()
    
        if patient_info:
            uhid,date,title,patientname,dob,age,gender,mobile,email,refdr,selectedtest,accession=patient_info

            # Create a formatted string with all the details
            details_string = (
              #  f"Visit ID: {visit_id}\n"
                f"Patient ID: {uhid}\n"
                f"Patient Name: {patientname}\n"
                f"DOB: {dob}\n"
                f"Age: {age}\n"
                f"Gender: {gender}\n"
                f"Mobile: {mobile}\n"
                f"Email: {email}\n"
              #  f"Patient Category: {patient_category}\n"
                f"Referring Doctor: {refdr}\n"
                f"Selected Test: {selectedtest}\n"
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
            qr_img.save(f'qr_code_{uhid}.png')

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
            pdf.image(f'qr_code_{uhid}.png', x=x_position, y=y_position, w=qr_size)

            # Add visit details to the PDF
            #pdf.set_font("Arial", size=8)
        # pdf.multi_cell(150, 10, details_string, border=0, align="L")

            # Set the PDF file path
            pdf_file_path = f'qr_code_{uhid}.pdf'

            # Output the PDF file
            pdf.output(pdf_file_path)

            QtWidgets.QMessageBox.information(
                None, 'QR Code PDF',
                f'QR code PDF for Visit ID {uhid} has been generated as "{pdf_file_path}"'
            )

    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.label_4.setText(_translate("Form", "Patient Name"))
        self.label_2.setText(_translate("Form", "From Date"))
        self.label_3.setText(_translate("Form", "To Date"))
        self.label_5.setText(_translate("Form", "Mobile"))
        self.pushButton_2.setText(_translate("Form", "search"))
        self.label.setText(_translate("Form", "Registration Summary"))
        self.pushButton.setText(_translate("Form", "Add Patient"))


        self.fetch_and_display_patient()
        self.pushButton.clicked.connect(self.addpatient)
        self.pushButton_3.clicked.connect(self.selected_qrcode_generate)
        self.pushButton_2.clicked.connect(self.filter_patient_data)
        





    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_patientForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
    