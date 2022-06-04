# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectManager.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

class Ui_ProjectManager(object):
    def setupUi(self, ProjectManager):
        if not ProjectManager.objectName():
            ProjectManager.setObjectName(u"ProjectManager")
        ProjectManager.resize(800, 600)
        self.centralwidget = QWidget(ProjectManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.project_list_ly = QVBoxLayout(self.verticalLayoutWidget)
        self.project_list_ly.setObjectName(u"project_list_ly")
        self.project_list_ly.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.verticalLayoutWidget)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.create_btn = QPushButton(self.widget)
        self.create_btn.setObjectName(u"create_btn")

        self.verticalLayout.addWidget(self.create_btn)

        self.template_btn = QPushButton(self.widget)
        self.template_btn.setObjectName(u"template_btn")

        self.verticalLayout.addWidget(self.template_btn)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info_lbl = QLabel(self.groupBox)
        self.info_lbl.setObjectName(u"info_lbl")
        self.info_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.info_lbl)


        self.verticalLayout.addWidget(self.groupBox)

        self.settings_btn = QPushButton(self.widget)
        self.settings_btn.setObjectName(u"settings_btn")

        self.verticalLayout.addWidget(self.settings_btn)

        self.splitter.addWidget(self.widget)

        self.horizontalLayout.addWidget(self.splitter)

        ProjectManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProjectManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        ProjectManager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProjectManager)
        self.statusbar.setObjectName(u"statusbar")
        ProjectManager.setStatusBar(self.statusbar)

        self.retranslateUi(ProjectManager)

        QMetaObject.connectSlotsByName(ProjectManager)
    # setupUi

    def retranslateUi(self, ProjectManager):
        ProjectManager.setWindowTitle(QCoreApplication.translate("ProjectManager", u"Project Manager", None))
        self.create_btn.setText(QCoreApplication.translate("ProjectManager", u"Create Project", None))
        self.template_btn.setText(QCoreApplication.translate("ProjectManager", u"Template Editor", None))
        self.groupBox.setTitle(QCoreApplication.translate("ProjectManager", u"Info", None))
        self.info_lbl.setText(QCoreApplication.translate("ProjectManager", u"TextLabel", None))
        self.settings_btn.setText(QCoreApplication.translate("ProjectManager", u"Settings", None))
    # retranslateUi

