from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor,QTextListFormat,QTextImageFormat
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTextCursor, QTextTableFormat, QTextCharFormat, QFont
from PyQt5.QtWidgets import QFileDialog
import os
import sqlite3

class Ui_reportForm(object):
    def setupUi(self, Form):
        self.f=Form
        Form.setObjectName("Form")
        Form.resize(1157, 642)
        self.toolButton_14 = QtWidgets.QToolButton(Form)
        self.toolButton_14.setGeometry(QtCore.QRect(430, 270, 25, 19))
        self.toolButton_14.setObjectName("toolButton_14")
        
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.label_10.setObjectName("label_10")
        self.toolButton_16 = QtWidgets.QToolButton(Form)
        self.toolButton_16.setGeometry(QtCore.QRect(280, 270, 25, 19))
        self.toolButton_16.setObjectName("toolButton_16")
        self.toolButton_12 = QtWidgets.QToolButton(Form)
        self.toolButton_12.setGeometry(QtCore.QRect(220, 270, 25, 19))
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_8 = QtWidgets.QToolButton(Form)
        self.toolButton_8.setGeometry(QtCore.QRect(340, 270, 25, 19))
        self.toolButton_8.setObjectName("toolButton_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(300, 170, 201, 31))
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
        self.toolButton_15 = QtWidgets.QToolButton(Form)
        self.toolButton_15.setGeometry(QtCore.QRect(490, 270, 25, 19))
        self.toolButton_15.setObjectName("toolButton_15")
        self.toolButton_13 = QtWidgets.QToolButton(Form)
        self.toolButton_13.setGeometry(QtCore.QRect(250, 270, 25, 19))
        self.toolButton_13.setObjectName("toolButton_13")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(300, 150, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.toolButton_11 = QtWidgets.QToolButton(Form)
        self.toolButton_11.setGeometry(QtCore.QRect(370, 270, 25, 19))
        self.toolButton_11.setObjectName("toolButton_11")
        self.lineEdit_22 = QtWidgets.QLineEdit(Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(70, 170, 201, 31))
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
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 260, 1161, 41))
        self.tableView.setObjectName("tableView")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 300, 791, 201))
        self.textEdit.setObjectName("textEdit")
        self.toolButton_17 = QtWidgets.QToolButton(Form)
        self.toolButton_17.setGeometry(QtCore.QRect(310, 270, 25, 19))
        self.toolButton_17.setObjectName("toolButton_15")
        self.toolButton_17.setIcon(QtGui.QIcon(os.path.join('images', 'redo.png')))
        self.toolButton_17.clicked.connect(self.textEdit.redo)
        self.toolButton_17.setObjectName("toolButton_17")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 580, 131, 31))
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
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontComboBox.setGeometry(QtCore.QRect(80, 270, 111, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.fontComboBox.currentFontChanged.connect(self.changeFontInTextEdit)
        self.fontComboBox.setToolTip("FontFamily")
        self.toolButton_9 = QtWidgets.QToolButton(Form)
        self.toolButton_9.setGeometry(QtCore.QRect(250, 270, 25, 19))
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_9.clicked.connect(self.alignTableTextRight)#alignright
        self.toolButton_9.setToolTip("RightAlign")
        self.toolButton_9.setIcon(QtGui.QIcon(os.path.join('images', 'alignright.png')))
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 300, 1161, 261))
        self.textEdit.setObjectName("textEdit")
        self.toolButton_10 = QtWidgets.QToolButton(Form)
        self.toolButton_10.setGeometry(QtCore.QRect(280, 270, 25, 19))
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_10.clicked.connect(self.makeSelectedTextBold)# bold
        self.toolButton_10.setIcon(QtGui.QIcon(os.path.join('images', 'bold.png')))
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 270, 41, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.changeFontSizeInTextEdit)
        self.comboBox.addItems(["8", "10", "12", "14", "16", "18", "20", "24", "28", "32"])
        self.comboBox.setToolTip("FontSize")
        
        self.toolButton_7 = QtWidgets.QToolButton(Form)
        self.toolButton_7.setGeometry(QtCore.QRect(190, 270, 25, 19))
        self.toolButton_7.setObjectName("toolButton_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(70, 150, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(70, 50, 211, 35))
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
        self.toolButton_18 = QtWidgets.QToolButton(Form)
        self.toolButton_18.setGeometry(QtCore.QRect(370, 270, 25, 19))
        self.toolButton_18.setObjectName("toolButton_18")
        self.toolButton_18.setToolTip("Insert Table")
        self.toolButton_18.setIcon(QtGui.QIcon(os.path.join('images', 'table.png')))
        self.toolButton_19 = QtWidgets.QToolButton(Form)
        self.toolButton_19.setGeometry(QtCore.QRect(340, 270, 25, 19))
        self.toolButton_19.setObjectName("toolButton_19")
        self.toolButton_19.clicked.connect(self.insertImage) # insert image
        self.toolButton_19.setIcon(QtGui.QIcon(os.path.join('images', 'image.png')))
        self.toolButton_20 = QtWidgets.QToolButton(Form)
        self.toolButton_20.setGeometry(QtCore.QRect(220, 270, 25, 19))
        self.toolButton_20.setObjectName("toolButton_20")
        self.toolButton_20.clicked.connect(self.alignTableTextCenter) #align center 
        self.toolButton_20.setIcon(QtGui.QIcon(os.path.join('images', 'aligncenter.png')))
        self.toolButton_21 = QtWidgets.QToolButton(Form)
        self.toolButton_21.setGeometry(QtCore.QRect(400, 270, 25, 19))
        self.toolButton_21.setObjectName("toolButton_21")
        self.toolButton_21.clicked.connect(self.makeSelectedTextItalic)# italic
        self.toolButton_21.setIcon(QtGui.QIcon(os.path.join('images', 'italic.png')))
        self.toolButton_22 = QtWidgets.QToolButton(Form)
        self.toolButton_22.setGeometry(QtCore.QRect(490, 270, 25, 19))
        self.toolButton_22.setObjectName("toolButton_22")
        self.toolButton_22.clicked.connect(self.toggleBulletList)# bullet
        self.toolButton_22.setIcon(QtGui.QIcon(os.path.join('images', 'bullet.png')))
        self.toolButton_24 = QtWidgets.QToolButton(Form)
        self.toolButton_24.setGeometry(QtCore.QRect(430, 270, 25, 19))
        self.toolButton_24.setObjectName("toolButton_24")
        self.toolButton_24.clicked.connect(self.toggleNumberedList)# number list
        self.toolButton_24.setIcon(QtGui.QIcon(os.path.join('images', 'number.png')))
        self.toolButton_25 = QtWidgets.QToolButton(Form)
        self.toolButton_25.setGeometry(QtCore.QRect(460, 270, 25, 19))
        self.toolButton_25.setObjectName("toolButton_25")
        self.toolButton_25.clicked.connect(self.alignTableTextRight)#alignright
        self.toolButton_25.setIcon(QtGui.QIcon(os.path.join('images', 'alignright.png')))
        
        
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
            
        # cursor = self.textEdit.textCursor()

        # # Find the table at the cursor position
        # table = cursor.currentTable()
        # if table:
        #     table_format = table.format()

        #     # Set table properties
        #     table_format.setAlignment(Qt.AlignRight)  # Set alignment to left

        #     table.setFormat(table_format)
    
    
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
        Form.setWindowTitle(_translate("Form", "Ekon"))
        self.toolButton_14.setText(_translate("Form", "B"))
        self.label_10.setText(_translate("Form", "Template"))
        self.toolButton_16.setText(_translate("Form", "..."))
        self.toolButton_12.setText(_translate("Form", "I"))
        self.toolButton_8.setText(_translate("Form", "..."))
        self.toolButton_15.setText(_translate("Form", "..."))
        self.toolButton_13.setText(_translate("Form", "..."))
        self.label_7.setText(_translate("Form", "Name"))
        self.toolButton_11.setText(_translate("Form", "..."))
        self.toolButton_17.setText(_translate("Form", "..."))
        self.pushButton_5.setText(_translate("Form", "Save Template"))
        self.toolButton_9.setText(_translate("Form", "ar"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.toolButton_10.setText(_translate("Form", "rd"))
        self.toolButton_7.setText(_translate("Form", "B"))
        self.label_8.setText(_translate("Form", "Code"))
        self.label.setText(_translate("Form", "Report Format"))
        self.toolButton_18.setText(_translate("Form", "tab"))
        self.toolButton_19.setText(_translate("Form", "img"))
        self.toolButton_20.setText(_translate("Form", "c"))
        self.toolButton_21.setText(_translate("Form", "I"))
        self.toolButton_22.setText(_translate("Form", "BU"))
        self.toolButton_24.setText(_translate("Form", "num"))
        self.toolButton_25.setText(_translate("Form", "ra"))
        self.pushButton_5.clicked.connect(self.save_template_to_database)
    def save_template_to_database(self):
        code = self.lineEdit_8.text()
        name = self.lineEdit_22.text()
        template = self.textEdit.toPlainText()  # Get the plain text content of the QTextEdit

        # Connect to the database
        connection = sqlite3.connect("patient_data.db")
        cursor = connection.cursor()

        # Insert the template into the report_templates table
        cursor.execute("INSERT INTO reporttemplates (code, name, template) VALUES (?, ?, ?)", (code, name, template))

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        self.f.close()
        print("Template saved to database.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_reportForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())