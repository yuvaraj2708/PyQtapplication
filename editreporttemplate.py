from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor,QTextListFormat,QTextImageFormat
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTextCursor, QTextTableFormat, QTextCharFormat, QFont
from PyQt5.QtWidgets import QFileDialog
import os
import sqlite3

class Ui_editreportForm(object):
    def setupUi(self, Form,code):
        self.conn = sqlite3.connect("patient_data.db")
        self.cursor = self.conn.cursor()
        self.reportcode=code
        self.f=Form
        Form.setObjectName("Form")
        Form.resize(811, 561)
        Form.showMaximized() 
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: #ffffff;")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 9, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 20, -1, 20)
        self.gridLayout.setHorizontalSpacing(26)
        self.gridLayout.setVerticalSpacing(21)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 30))
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
        self.gridLayout.addWidget(self.lineEdit_18, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(26, 40))
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
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #5E6278;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout.addWidget(self.fontComboBox)
        self.toolButton_7 = QtWidgets.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/alignleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setObjectName("toolButton_7")
        self.horizontalLayout.addWidget(self.toolButton_7)
        self.toolButton_12 = QtWidgets.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/aligncenter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon1)
        self.toolButton_12.setObjectName("toolButton_12")
        self.horizontalLayout.addWidget(self.toolButton_12)
        self.toolButton_13 = QtWidgets.QToolButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/alignright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon2)
        self.toolButton_13.setObjectName("toolButton_13")
        self.horizontalLayout.addWidget(self.toolButton_13)
        self.toolButton_16 = QtWidgets.QToolButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_16.setIcon(icon3)
        self.toolButton_16.setObjectName("toolButton_16")
        self.horizontalLayout.addWidget(self.toolButton_16)
        self.toolButton_9 = QtWidgets.QToolButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon4)
        self.toolButton_9.setObjectName("toolButton_9")
        self.horizontalLayout.addWidget(self.toolButton_9)
        self.toolButton_8 = QtWidgets.QToolButton(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon5)
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout.addWidget(self.toolButton_8)
        self.toolButton_11 = QtWidgets.QToolButton(Form)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon6)
        self.toolButton_11.setObjectName("toolButton_11")
        self.horizontalLayout.addWidget(self.toolButton_11)
        self.toolButton_10 = QtWidgets.QToolButton(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon7)
        self.toolButton_10.setObjectName("toolButton_10")
        self.horizontalLayout.addWidget(self.toolButton_10)
        self.toolButton_14 = QtWidgets.QToolButton(Form)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/number.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon8)
        self.toolButton_14.setObjectName("toolButton_14")
        self.horizontalLayout.addWidget(self.toolButton_14)
        self.toolButton_17 = QtWidgets.QToolButton(Form)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/bullet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_17.setIcon(icon9)
        self.toolButton_17.setObjectName("toolButton_17")
        self.horizontalLayout.addWidget(self.toolButton_17)
        self.toolButton_15 = QtWidgets.QToolButton(Form)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon10)
        self.toolButton_15.setObjectName("toolButton_15")
        self.horizontalLayout.addWidget(self.toolButton_15)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(5, 40))
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
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self._2 = QtWidgets.QVBoxLayout()
        self._2.setObjectName("_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 250))
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setObjectName("textEdit")
        self._2.addWidget(self.textEdit)
        self.gridLayout_2.addLayout(self._2, 8, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 7, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 5, 0, 1, 1)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.populate_report_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Code"))
        self.pushButton_2.setText(_translate("Form", "Save Template"))
        self.label_4.setText(_translate("Form", "Name"))
        self.comboBox.setItemText(0, _translate("Form", "8"))
        self.comboBox.setItemText(1, _translate("Form", "10"))
        self.comboBox.setItemText(2, _translate("Form", "12"))
        self.comboBox.setItemText(3, _translate("Form", "14"))
        self.comboBox.setItemText(4, _translate("Form", "16"))
        self.comboBox.setItemText(5, _translate("Form", "18"))
        self.comboBox.setItemText(6, _translate("Form", "20"))
        self.comboBox.setItemText(7, _translate("Form", "22"))
        self.comboBox.setItemText(8, _translate("Form", "24"))
        self.comboBox.setItemText(9, _translate("Form", "26"))
        self.comboBox.setItemText(10, _translate("Form", "28"))
        self.comboBox.setItemText(11, _translate("Form", "30"))
        self.comboBox.setItemText(12, _translate("Form", "32"))
        self.comboBox.setItemText(13, _translate("Form", "34"))
        self.comboBox.setItemText(14, _translate("Form", "36"))
        self.toolButton_7.setText(_translate("Form", "B"))
        self.toolButton_12.setText(_translate("Form", "I"))
        self.toolButton_13.setText(_translate("Form", "..."))
        self.toolButton_16.setText(_translate("Form", "..."))
        self.toolButton_9.setText(_translate("Form", "..."))
        self.toolButton_8.setText(_translate("Form", "..."))
        self.toolButton_11.setText(_translate("Form", "..."))
        self.toolButton_10.setText(_translate("Form", "..."))
        self.toolButton_14.setText(_translate("Form", "..."))
        self.toolButton_17.setText(_translate("Form", "..."))
        self.toolButton_15.setText(_translate("Form", "..."))
        self.label_10.setText(_translate("Form", "Template"))
        self.label.setText(_translate("Form", "Report Format"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
   
        self.comboBox.currentIndexChanged.connect(self.changeFontSizeInTextEdit)
        self.fontComboBox.currentFontChanged.connect(self.changeFontInTextEdit)
        self.toolButton_7.clicked.connect(self.alignTableTextLeft)
        self.toolButton_8.clicked.connect(self.insertImage)
       # self.toolButton_9.clicked.connect()
        self.toolButton_10.clicked.connect(self.makeSelectedTextItalic)
       # self.toolButton_11.clikced.connect()
        self.toolButton_12.clicked.connect(self.alignTableTextCenter)
        self.toolButton_13.clicked.connect(self.alignTableTextRight)
        self.toolButton_14.clicked.connect(self.toggleNumberedList)
       # self.toolButton_15.clikced.connect()
        self.toolButton_16.clicked.connect(self.makeSelectedTextBold)
        self.toolButton_17.clicked.connect(self.toggleBulletList)
        self.pushButton_2.clicked.connect(self.save_template_to_database)

    def populate_report_data(self):
        if self.reportcode:
            # Fetch patient data for the specified patient_id
            reporttemplate_data = self.fetch_report_data_by_id(self.reportcode)
            if reporttemplate_data:
                # Populate the form fields with the patient data
                # Assuming the second item is the title
                self.lineEdit_18.setText(reporttemplate_data[0])  # Assuming the third item is the patient name
                self.lineEdit_6.setText(reporttemplate_data[1])
                self.textEdit.setPlainText(reporttemplate_data[2])

                

    def fetch_report_data_by_id(self, reporttemplate_code):
        self.cursor.execute("SELECT * FROM reporttemplates WHERE code=?", (reporttemplate_code,))
        reporttemplate_data = self.cursor.fetchone()
        return reporttemplate_data




    def save_template_to_database(self):
        code = self.lineEdit_18.text()
        name = self.lineEdit_6.text()
        template = self.textEdit.toPlainText()  # Get the plain text content of the QTextEdit

        # Connect to the database
        connection = sqlite3.connect("patient_data.db")
        cursor = connection.cursor()

        # Insert the template into the report_templates table
        cursor.execute("UPDATE reporttemplates SET code=?, name=?, template=? where code == ?",
                            (code,name,template,self.reportcode)) 

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        self.f.close()


    def changeFontSizeInTextEdit(self, index):
        font_size = int(self.comboBox.itemText(index))
        cursor = self.textEdit.textCursor()
        char_format = cursor.charFormat()
        char_format.setFontPointSize(font_size)
        self.textEdit.setFontPointSize(font_size)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_editreportForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())