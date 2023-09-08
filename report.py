from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor,QTextListFormat,QTextImageFormat
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTextCursor, QTextTableFormat, QTextCharFormat, QFont
from PyQt5.QtWidgets import QFileDialog
import os

class Ui_reportingForm(object):
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
        self.label.setGeometry(QtCore.QRect(380, 20, 211, 35))
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
        self.groupBox.setGeometry(QtCore.QRect(0, 60, 961, 571))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 470, 131, 31))
        self.pushButton_2.clicked.connect(self.saveReport)
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
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #5E6278;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setGeometry(QtCore.QRect(20, 70, 161, 31))
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
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 250, 791, 201))
        self.textEdit.setObjectName("textEdit")
        
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 210, 791, 41))
        self.tableView.setObjectName("tableView") 
        
        
        self.comboBox_26 = QtWidgets.QComboBox(Form)
        self.comboBox_26.setGeometry(QtCore.QRect(190, 130, 161, 31))
        self.comboBox_26.currentIndexChanged.connect(self.previewReport)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Fetch and populate data from the database
        self.populate_report_templates()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.toolButton_7 = QtWidgets.QToolButton(Form)
        self.toolButton_7.setGeometry(QtCore.QRect(180, 220, 25, 19))
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_7.clicked.connect(self.makeSelectedTextBold)# bold
        self.toolButton_7.setIcon(QtGui.QIcon(os.path.join('images', 'bold.png')))
        self.toolButton_7.setToolTip("Bold")
        self.toolButton_8 = QtWidgets.QToolButton(Form)
        self.toolButton_8.setGeometry(QtCore.QRect(330, 220, 25, 19))
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_8.clicked.connect(self.insertTable) #insert table
        self.toolButton_8.setToolTip("Insert Table")
        self.toolButton_8.setIcon(QtGui.QIcon(os.path.join('images', 'table.png')))
        self.toolButton_9 = QtWidgets.QToolButton(Form)
        self.toolButton_9.setGeometry(QtCore.QRect(300, 220, 25, 19))
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_9.clicked.connect(self.insertImage) # insert image
        self.toolButton_9.setIcon(QtGui.QIcon(os.path.join('images', 'image.png')))
        self.toolButton_9.setToolTip("Insert Image")
        self.toolButton_10 = QtWidgets.QToolButton(Form)
        self.toolButton_10.setGeometry(QtCore.QRect(390, 220, 25, 19))
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_10.clicked.connect(self.alignTableTextCenter) #align center 
        self.toolButton_10.setIcon(QtGui.QIcon(os.path.join('images', 'aligncenter.png'))) 
        self.toolButton_10.setToolTip("Center")
        self.toolButton_11 = QtWidgets.QToolButton(Form)
        self.toolButton_11.setGeometry(QtCore.QRect(360, 220, 25, 19))
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_11.clicked.connect(self.alignTableTextLeft) # leftalign
        self.toolButton_11.setIcon(QtGui.QIcon(os.path.join('images', 'alignleft.png')))
        self.toolButton_11.setToolTip("AlignLeft")
        self.toolButton_12 = QtWidgets.QToolButton(Form)
        self.toolButton_12.setGeometry(QtCore.QRect(210, 220, 25, 19))
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_12.clicked.connect(self.makeSelectedTextItalic)# italic
        self.toolButton_12.setIcon(QtGui.QIcon(os.path.join('images', 'italic.png')))
        self.toolButton_12.setToolTip("Italic")
        self.toolButton_13 = QtWidgets.QToolButton(Form)
        self.toolButton_13.setGeometry(QtCore.QRect(240, 220, 25, 19))
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_13.clicked.connect(self.toggleBulletList)# bullet
        self.toolButton_13.setIcon(QtGui.QIcon(os.path.join('images', 'bullet.png')))
        self.toolButton_13.setToolTip("Bullet List")
        self.toolButton_16 = QtWidgets.QToolButton(Form)
        self.toolButton_16.setGeometry(QtCore.QRect(270, 220, 25, 19))
        self.toolButton_16.setObjectName("toolButton_16")
        self.toolButton_16.clicked.connect(self.toggleNumberedList)# number list
        self.toolButton_16.setToolTip("Number List")
        self.toolButton_16.setIcon(QtGui.QIcon(os.path.join('images', 'number.png')))
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontComboBox.setGeometry(QtCore.QRect(70, 220, 111, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.fontComboBox.currentFontChanged.connect(self.changeFontInTextEdit)
        self.fontComboBox.setToolTip("FontFamily")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 220, 41, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.changeFontSizeInTextEdit)
        self.comboBox.addItems(["8", "10", "12", "14", "16", "18", "20", "24", "28", "32"])
        self.comboBox.setToolTip("FontSize")
        self.toolButton_14 = QtWidgets.QToolButton(Form)
        self.toolButton_14.setGeometry(QtCore.QRect(420, 220, 25, 19))
        self.toolButton_14.setObjectName("toolButton_14")
        self.toolButton_14.clicked.connect(self.alignTableTextRight)#alignright
        self.toolButton_14.setToolTip("RightAlign")
        self.toolButton_14.setIcon(QtGui.QIcon(os.path.join('images', 'alignright.png')))
        self.toolButton_15 = QtWidgets.QToolButton(Form)
        self.toolButton_15.setGeometry(QtCore.QRect(480, 220, 25, 19))
        self.toolButton_15.setObjectName("toolButton_15")
        self.toolButton_15.setIcon(QtGui.QIcon(os.path.join('images', 'redo.png')))
        self.toolButton_15.clicked.connect(self.textEdit.redo) 
        self.toolButton_15.setToolTip("Redo")
        self.toolButton_17 = QtWidgets.QToolButton(Form)
        self.toolButton_17.setGeometry(QtCore.QRect(450, 220, 25, 19))
        self.toolButton_17.setObjectName("toolButton_17")
        self.toolButton_17.setIcon(QtGui.QIcon(os.path.join('images', 'undo.png')))
        self.toolButton_17.clicked.connect(self.textEdit.undo)
        self.toolButton_17.setToolTip("Undo")  # Set the tooltip for the button

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def changeFontSizeInTextEdit(self, index):
        font_size = int(self.comboBox.itemText(index))
        cursor = self.textEdit.textCursor()
        char_format = cursor.charFormat()
        char_format.setFontPointSize(font_size)
        cursor.setCharFormat(char_format)
    
    def changeFontInTextEdit(self, font):
       cursor = self.textEdit.textCursor()
       char_format = cursor.charFormat()
       char_format.setFont(font)
       cursor.setCharFormat(char_format)
       self.textEdit.setCurrentFont(font)
    
    def alignTableTextLeft(self):
      cursor = self.textEdit.textCursor()
  
      # Check if a table is not selected (i.e., the cursor is within regular text)
      if cursor.currentTable() is None:
          block_format = cursor.blockFormat()
          block_format.setAlignment(Qt.AlignLeft)
          cursor.setBlockFormat(block_format)

            
    def alignTableTextCenter(self):
         cursor = self.textEdit.textCursor()
  
      # Check if a table is not selected (i.e., the cursor is within regular text)
         if cursor.currentTable() is None:
             block_format = cursor.blockFormat()
             block_format.setAlignment(Qt.AlignCenter)
             cursor.setBlockFormat(block_format)   
               
    def alignTableTextRight(self):
         cursor = self.textEdit.textCursor()
  
      # Check if a table is not selected (i.e., the cursor is within regular text)
         if cursor.currentTable() is None:
             block_format = cursor.blockFormat()
             block_format.setAlignment(Qt.AlignRight)
             cursor.setBlockFormat(block_format)      
            
     
    
    def insertTable(self):
        cursor = self.textEdit.textCursor()

        # Get the number of rows and columns from the user
        rows, ok1 = QtWidgets.QInputDialog.getInt(None, "Table Rows", "Enter number of rows:")
        cols, ok2 = QtWidgets.QInputDialog.getInt(None, "Table Columns", "Enter number of columns:")
        
        if ok1 and ok2:
            table = cursor.insertTable(rows, cols)
            table_format = table.format()

            # Set table properties
            table_format.setAlignment(Qt.AlignCenter)
            table_format.setBorder(1)
            table_format.setCellSpacing(0)
            table_format.setCellPadding(10)

            table.setFormat(table_format)

            # Set cell font properties
            new_font = QFont("Arial", 14)  # Adjust font size and family
            cell_format = QTextCharFormat()
            cell_format.setFont(new_font)

            # Apply the new font to all cells in the table
            for row in range(rows):
                for col in range(cols):
                    cell_cursor = table.cellAt(row, col).firstCursorPosition()
                    cell_cursor.setCharFormat(cell_format)
                    
    def insertImage(self):
        cursor = self.textEdit.textCursor()

        # Get the path to the image file
        image_path, _ = QFileDialog.getOpenFileName(None, "Insert Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")
        if not image_path:
            return

        # Create an image format and insert it at the cursor position
        image_format = QTextImageFormat()
        image_format.setName(image_path)

        # Specify the desired image size (adjust these values as needed)
        image_width = 200  # in pixels
        image_height = 150  # in pixels
        image_format.setWidth(image_width)
        image_format.setHeight(image_height)

        cursor.insertImage(image_format)
        
        
    def toggleNumberedList(self):
        cursor = self.textEdit.textCursor()
        list_format = QTextListFormat()

        if cursor.currentList():
            cursor.endEditBlock()
            cursor.createList(list_format)
        else:
            cursor.beginEditBlock()
            list_format.setStyle(QTextListFormat.ListDecimal)
            cursor.createList(list_format)
            cursor.insertText("")  # Inserts an empty item to start the list

        cursor.endEditBlock()
    
    def toggleBulletList(self):
        cursor = self.textEdit.textCursor()
        list_format = QTextListFormat()

        if cursor.currentList():
            cursor.endEditBlock()
            cursor.createList(list_format)
        else:
            cursor.beginEditBlock()
            list_format.setStyle(QTextListFormat.ListDisc)
            cursor.createList(list_format)
            cursor.insertText("")  # Inserts an empty item to start the list

        cursor.endEditBlock()
        
    
    
    def makeSelectedTextItalic(self):
        cursor = self.textEdit.textCursor()
        if not cursor.hasSelection():
            return

        current_format = cursor.charFormat()
        font = current_format.font()
        font.setItalic(not font.italic())

        new_format = QtGui.QTextCharFormat()
        new_format.setFont(font)
        
        cursor.mergeCharFormat(new_format)
        self.textEdit.mergeCurrentCharFormat(new_format)
        
    def makeSelectedTextBold(self):
        cursor = self.textEdit.textCursor()
        if not cursor.hasSelection():
            return

        current_format = cursor.charFormat()
        font = current_format.font()
        font.setBold(not font.bold())

        new_format = QtGui.QTextCharFormat()
        new_format.setFont(font)
        
        cursor.mergeCharFormat(new_format)
        self.textEdit.mergeCurrentCharFormat(new_format)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.toolButton_7.setText(_translate("Form", "B"))
        self.toolButton_8.setText(_translate("Form", "tab"))
        self.toolButton_9.setText(_translate("Form", "img"))
        self.toolButton_10.setText(_translate("Form", "c"))
        self.toolButton_11.setText(_translate("Form", "al"))
        self.toolButton_12.setText(_translate("Form", "I"))
        self.toolButton_13.setText(_translate("Form", "BU"))
        self.toolButton_16.setText(_translate("Form", "num"))
        self.toolButton_14.setText(_translate("Form", "ra"))
        self.toolButton_15.setText(_translate("Form", "rd"))
        self.toolButton_17.setText(_translate("Form", "ud"))
    def previewReport(self, index):
      # Get the selected item from the combo box
      selected_report = self.comboBox_26.currentText()
  
      # Fetch and display the report content based on the selected report
      report_content = self.fetch_report_content(selected_report)
      self.textEdit.setPlainText(report_content)
  
      # Show or hide the table and rich text editor based on the report content
      if "table" in report_content.lower():
          self.tableView.show()
          self.textEdit.hide()
      else:
          self.tableView.hide()
          self.textEdit.show()

    def fetch_report_content(self, name):
        # You need to fetch the report content from your database based on the report name.
        # Implement the database retrieval logic here and return the report content as a string.
        # For this example, I'm assuming you have a table named "reporttemplates" with a column "content"
        # where you store the report content.

        connection = sqlite3.connect("patient_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM reporttemplates WHERE name = ?", (name,))
        result = cursor.fetchone()
        connection.close()

        if result:
            return result[0]  # Return the report content as a string
        else:
            return "Report not found."

    def populate_report_templates(self):
        # Fetch report templates from the database and add them to the combo box
        connection = sqlite3.connect("patient_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reporttemplates")
        reports = cursor.fetchall()
        connection.close()

        # Extract the report names and add them to the combo box
        report_names = [report[1] for report in reports]
        self.comboBox_26.addItems(report_names)
 
    def saveReport(self):
        # Get the selected report template
        selected_report = self.comboBox_26.currentText()
        report_content = self.fetch_report_content(selected_report)

        # Get patient information (you can modify this part to get patient data)
        patient_name = self.lineEdit_18.text()
        # Here, you can add more fields like patient ID, date, etc.

        # Get the report content from the QTextEdit
        edited_report = self.textEdit.toPlainText()

        # Create a new record in the patient-specific reports table
        connection = sqlite3.connect("patient_data.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO patient_reports (patient_name, report_template, report_content) VALUES (?, ?, ?)",
            (patient_name, selected_report, edited_report),
        )
        connection.commit()
        connection.close()

        # Optionally, you can show a message or update the UI to indicate that the report has been saved.

        # Clear the QTextEdit if needed
        self.textEdit.clear()
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Report "))
        self.pushButton_2.setText(_translate("Form", "Report Study"))
        self.label_2.setText(_translate("Form", "Patient Name"))
        self.label_3.setText(_translate("Form", "Report Template"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_reportingForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())