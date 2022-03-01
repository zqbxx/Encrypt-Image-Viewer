# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'urllist.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(400, 434, 221, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(29, 49, 591, 361))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 241, 18))
        self.readFromFileButton = QPushButton(Dialog)
        self.readFromFileButton.setObjectName(u"readFromFileButton")
        self.readFromFileButton.setGeometry(QRect(390, 10, 231, 30))
        icon = QIcon()
        icon.addFile(u":/assets/open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.readFromFileButton.setIcon(icon)
        self.readFromFileButton.setIconSize(QSize(26, 26))
        self.toClipboardButton = QPushButton(Dialog)
        self.toClipboardButton.setObjectName(u"toClipboardButton")
        self.toClipboardButton.setGeometry(QRect(29, 436, 51, 30))
        icon1 = QIcon()
        icon1.addFile(u":/assets/clipboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toClipboardButton.setIcon(icon1)
        self.toClipboardButton.setIconSize(QSize(24, 24))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(49, 406, 21, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.fromClipboardButton = QPushButton(Dialog)
        self.fromClipboardButton.setObjectName(u"fromClipboardButton")
        self.fromClipboardButton.setGeometry(QRect(92, 436, 41, 30))
        icon2 = QIcon()
        icon2.addFile(u":/assets/paste_from_clipboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fromClipboardButton.setIcon(icon2)
        self.fromClipboardButton.setIconSize(QSize(36, 36))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(109, 405, 21, 31))
        self.label_8.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(282, 416, 21, 18))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.clearButton = QPushButton(Dialog)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(260, 436, 51, 30))
        icon3 = QIcon()
        icon3.addFile(u":/assets/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(icon3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Open custom image URLs", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"List of image URLs. Commented lines start with '#'. Commented lines and blank lines are ignored.", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Paste in a list of image URLs:", None))
        self.readFromFileButton.setText(QCoreApplication.translate("Dialog", u" &Read list from a text file", None))
#if QT_CONFIG(tooltip)
        self.toClipboardButton.setToolTip(QCoreApplication.translate("Dialog", u"copy to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.toClipboardButton.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u2193", None))
#if QT_CONFIG(tooltip)
        self.fromClipboardButton.setToolTip(QCoreApplication.translate("Dialog", u"paste from clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.fromClipboardButton.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u2191", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"|", None))
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("Dialog", u"clear", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText("")
    # retranslateUi

