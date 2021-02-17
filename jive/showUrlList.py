# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jive/urllist.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(400, 434, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 49, 591, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 241, 18))
        self.label.setObjectName("label")
        self.readFromFileButton = QtWidgets.QPushButton(Dialog)
        self.readFromFileButton.setGeometry(QtCore.QRect(390, 10, 231, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/open_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.readFromFileButton.setIcon(icon)
        self.readFromFileButton.setIconSize(QtCore.QSize(26, 26))
        self.readFromFileButton.setObjectName("readFromFileButton")
        self.toClipboardButton = QtWidgets.QPushButton(Dialog)
        self.toClipboardButton.setGeometry(QtCore.QRect(29, 436, 51, 30))
        self.toClipboardButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/assets/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toClipboardButton.setIcon(icon1)
        self.toClipboardButton.setIconSize(QtCore.QSize(24, 24))
        self.toClipboardButton.setObjectName("toClipboardButton")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(49, 406, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.fromClipboardButton = QtWidgets.QPushButton(Dialog)
        self.fromClipboardButton.setGeometry(QtCore.QRect(92, 436, 41, 30))
        self.fromClipboardButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/assets/paste_from_clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromClipboardButton.setIcon(icon2)
        self.fromClipboardButton.setIconSize(QtCore.QSize(36, 36))
        self.fromClipboardButton.setObjectName("fromClipboardButton")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(109, 405, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(282, 416, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.clearButton = QtWidgets.QPushButton(Dialog)
        self.clearButton.setGeometry(QtCore.QRect(260, 436, 51, 30))
        self.clearButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/assets/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon3)
        self.clearButton.setObjectName("clearButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open custom image URLs"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "List of image URLs. Commented lines start with \'#\'. Commented lines and blank lines are ignored."))
        self.label.setText(_translate("Dialog", "Paste in a list of image URLs:"))
        self.readFromFileButton.setText(_translate("Dialog", " &Read list from a text file"))
        self.toClipboardButton.setToolTip(_translate("Dialog", "copy to clipboard"))
        self.label_7.setText(_translate("Dialog", "↓"))
        self.fromClipboardButton.setToolTip(_translate("Dialog", "paste from clipboard"))
        self.label_8.setText(_translate("Dialog", "↑"))
        self.label_2.setText(_translate("Dialog", "|"))
        self.clearButton.setToolTip(_translate("Dialog", "clear"))

from jive import icons_rc