from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import qrcode
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QDialog
from patientregister import Ui_addpatientForm
from PyQt5.QtGui import QImage, QPixmap
from fpdf import FPDF
import os
from scan import Ui_scanForm
import barcode
from barcode import generate
from barcode.writer import ImageWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Ui_visitsummaryForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 588)
        Form.setMaximumSize(QtCore.QSize(851, 16777215))
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
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(310, 120, 201, 31))
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
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(320, 260, 151, 16))
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 100, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(20, 120, 121, 31))
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
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 120, 131, 31))
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
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(670, 260, 47, 13))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 120, 91, 31))
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
        self.label_10.setGeometry(QtCore.QRect(30, 260, 81, 16))
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 100, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(160, 260, 71, 16))
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:#0DBCC0;\n"
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
        
        self.visit_data = {}
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(-27, 280, 921, 421))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(-27, 280, 921, 421))
        self.textEdit.setObjectName("textEdit")
        
        self.listWidget = QtWidgets.QListWidget(Form)  # Initialize the listWidget
        self.listWidget.setGeometry(QtCore.QRect(-27, 280, 921, 421))
        self.listWidget.setObjectName("listWidget")

        # Use the listWidget to display data
        self.fetch_and_display_visit_data()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def fetch_and_display_visit_data(self):
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM visit")
        visit_data = cursor.fetchall()

        if visit_data:
            self.listWidget.clear()

            for row in visit_data:
                item = QtWidgets.QListWidgetItem()
                self.listWidget.addItem(item)

                custom_widget = QtWidgets.QWidget()
                custom_layout = QtWidgets.QHBoxLayout(custom_widget)
                label = QtWidgets.QLabel(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10}  ")
                custom_layout.addWidget(label)
                font = QtGui.QFont("Poppins", 8)  # Replace "8" with the desired font size
                label.setFont(font)
                custom_layout.addWidget(label)
                button_layout = QtWidgets.QHBoxLayout()  
               
                scan_button = QtWidgets.QPushButton()
                scan_button.setIcon(QtGui.QIcon(os.path.join('images', 'cam.png')))
                scan_button.setFixedSize(20, 20)
                scan_button.clicked.connect(lambda _, row=row: self.open_add_scan_form(row)) 
                button_layout.addWidget(scan_button)
               
                delete_button = QtWidgets.QPushButton()
                delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
                delete_button.setFixedSize(20, 20)
                delete_button.clicked.connect(lambda _, row=row: self.delete_visit(row[0])) 
                button_layout.addWidget(delete_button)
                
                QR_button = QtWidgets.QPushButton()
                QR_button.setIcon(QtGui.QIcon(os.path.join('images', 'qr.png')))
                QR_button.setFixedSize(20, 20)
                QR_button.clicked.connect(lambda _, row=row: self.generate_qr_code_pdf(row))
                button_layout.addWidget(QR_button)
                
                barcode_button = QtWidgets.QPushButton()
                barcode_button.setIcon(QtGui.QIcon(os.path.join('images', 'barcode.png')))
                barcode_button.setFixedSize(20, 20)
                barcode_button.clicked.connect(lambda _, row=row: self.generate_bar_code_pdf(row))
                button_layout.addWidget(barcode_button)
                
                button_layout.addSpacing(90)
                custom_layout.addLayout(button_layout)  # Add the button layout to the custom layout
                item.setSizeHint(custom_widget.sizeHint())
                self.listWidget.setItemWidget(item, custom_widget)
                item.visit_data = row
 
        conn.close()

    
    def delete_visit(self, visit_id):
     print("Deleting visit with visitid:", visit_id)
     
     # Connect to the database
     conn = sqlite3.connect('patient_data.db')
     cursor = conn.cursor()

     try:
         # Delete patient data from the database
         cursor.execute("DELETE FROM visit WHERE visitid = ?", (visit_id,))
         
         # Commit the transaction to save the changes
         conn.commit()
         
         print("Visit deleted successfully")
     except sqlite3.Error as e:
         print("Error deleting visit:", e)
         # Rollback the transaction in case of an error
         conn.rollback()
     finally:
        conn.close()

    # Refresh the displayed patient data immediately after deletion
     self.fetch_and_display_visit_data()

     
    def open_add_scan_form(self, visit_data):
       self.add_scan_form = QtWidgets.QWidget()
       self.ui_add_scan = Ui_scanForm()
       self.ui_add_scan.setupUi(self.add_scan_form)
   
       # Pass visit data to Ui_scanForm and update labels
       self.ui_add_scan.set_scan_data(visit_data)
   
       self.add_scan_form.show()
    
    
    def generate_bar_code_pdf(self, accession):
        # Extract the accession number from the row, assuming it's in a specific column (adjust as needed).
        accession_str = str(accession)

        # Generate the barcode image using the string representation of the accession number and save it to a file.
        barcode.generate('Code128', accession_str, writer=ImageWriter(), output=os.path.join('images', 'barcode.png'))
        x = 100  # Adjust the x-coordinate as needed
        y = 500  # Adjust the y-coordinate as needed
        width = 200  # Adjust the width as needed
        height = 50  
        # Create a PDF with the barcode image.
        pdf_filename = f'barcode_{accession[1]}.pdf'
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.drawImage(os.path.join('images', 'barcode.png'), x, y, width, height)  # Adjust x, y, width, height as needed
        c.showPage()
        c.save()

        # Optionally, you can open the generated PDF.
        os.system(pdf_filename)
    
    def generate_qr_code_pdf(self, visit_data):
        visitid, patient_id, patient_category, ref_dr, selected_test, visitid, date = visit_data

        # Retrieve patient information based on patient_id from the patients table
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT patientname, dob, age, gender, mobile, email FROM patients WHERE uhid = ?", (patient_id,))
        patient_info = cursor.fetchone()

        conn.close()

        if patient_info:
            patientname, dob, age, gender, mobile, email = patient_info

            # Create a formatted string with all the details
            details_string = (
                f"Visit ID: {visitid}\n"
                f"Patient ID: {patient_id}\n"
                f"Patient Name: {patientname}\n"
                f"DOB: {age}\n"
                f"Age: {gender}\n"
                f"Gender: {dob}\n"
                f"Mobile: {mobile}\n"
                f"Email: {email}\n"
                f"Patient Category: {patient_category}\n"
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
            qr_img.save(f'qr_code_{visitid}.png')

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
            pdf.image(f'qr_code_{visitid}.png', x=x_position, y=y_position, w=qr_size)

            # Add visit details to the PDF
            pdf.set_font("Arial", size=8)
            pdf.multi_cell(150, 10, details_string, border=0, align="L")

            # Set the PDF file path
            pdf_file_path = f'qr_code_{visitid}.pdf'

            # Output the PDF file
            pdf.output(pdf_file_path)

            QtWidgets.QMessageBox.information(
                None, 'QR Code PDF',
                f'QR code PDF for Visit ID {visitid} has been generated as "{pdf_file_path}"'
            )
  
    
               
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Visit Summary"))
        self.label_2.setText(_translate("Form", "From Date"))
        self.label_12.setText(_translate("Form", "Ref By / Test’s Asked"))
        self.label_3.setText(_translate("Form", "To Date"))
        self.label_13.setText(_translate("Form", "Actions"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_10.setText(_translate("Form", "Date / Visit ID"))
        self.label_4.setText(_translate("Form", "Pt.Name / Visit ID / Pt.ID"))
        self.label_11.setText(_translate("Form", "Patient Details"))
        self.pushButton_2.setText(_translate("Form", "Add Patient"))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_add_patient_form) 
    
    def open_add_patient_form(self):
        self.add_test_form = QtWidgets.QWidget()
        self.ui_add_test = Ui_addpatientForm()
        self.ui_add_test.setupUi(self.add_test_form)
        self.add_test_form.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_visitsummaryForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())