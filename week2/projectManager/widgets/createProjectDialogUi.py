# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createProjectDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        if not createDialog.objectName():
            createDialog.setObjectName(u"createDialog")
        createDialog.resize(346, 268)
        self.verticalLayout = QVBoxLayout(createDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(createDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.name_lb = QLineEdit(createDialog)
        self.name_lb.setObjectName(u"name_lb")

        self.gridLayout.addWidget(self.name_lb, 0, 1, 1, 1)

        self.label_2 = QLabel(createDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comment_pte = QPlainTextEdit(createDialog)
        self.comment_pte.setObjectName(u"comment_pte")

        self.gridLayout.addWidget(self.comment_pte, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_btn = QPushButton(createDialog)
        self.create_btn.setObjectName(u"create_btn")

        self.horizontalLayout.addWidget(self.create_btn)

        self.cancel_btn = QPushButton(createDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(createDialog)

        QMetaObject.connectSlotsByName(createDialog)
    # setupUi

    def retranslateUi(self, createDialog):
        createDialog.setWindowTitle(QCoreApplication.translate("createDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("createDialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("createDialog", u"Comment", None))
        self.create_btn.setText(QCoreApplication.translate("createDialog", u"Create", None))
        self.cancel_btn.setText(QCoreApplication.translate("createDialog", u"Cancel", None))
    # retranslateUi

