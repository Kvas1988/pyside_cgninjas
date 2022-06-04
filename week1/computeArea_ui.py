# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'computeArea.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_computeArea(object):
    def setupUi(self, computeArea):
        if not computeArea.objectName():
            computeArea.setObjectName(u"computeArea")
        computeArea.resize(416, 437)
        self.centralwidget = QWidget(computeArea)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shape_cmbbx = QComboBox(self.groupBox)
        self.shape_cmbbx.addItem("")
        self.shape_cmbbx.addItem("")
        self.shape_cmbbx.setObjectName(u"shape_cmbbx")

        self.verticalLayout.addWidget(self.shape_cmbbx)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.square_grpbx = QGroupBox(self.centralwidget)
        self.square_grpbx.setObjectName(u"square_grpbx")
        self.verticalLayout_3 = QVBoxLayout(self.square_grpbx)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.square_grpbx)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 0))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.square_height_spbx = QSpinBox(self.square_grpbx)
        self.square_height_spbx.setObjectName(u"square_height_spbx")
        self.square_height_spbx.setMaximum(999999999)
        self.square_height_spbx.setValue(1)

        self.horizontalLayout.addWidget(self.square_height_spbx)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.square_grpbx)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.square_width_spbx = QSpinBox(self.square_grpbx)
        self.square_width_spbx.setObjectName(u"square_width_spbx")
        self.square_width_spbx.setMaximum(999999999)
        self.square_width_spbx.setValue(1)

        self.horizontalLayout_2.addWidget(self.square_width_spbx)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.square_grpbx)

        self.circle_grpbx = QGroupBox(self.centralwidget)
        self.circle_grpbx.setObjectName(u"circle_grpbx")
        self.verticalLayout_4 = QVBoxLayout(self.circle_grpbx)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.circle_grpbx)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.circle_radius_spbx = QSpinBox(self.circle_grpbx)
        self.circle_radius_spbx.setObjectName(u"circle_radius_spbx")
        self.circle_radius_spbx.setMaximum(999999999)
        self.circle_radius_spbx.setValue(1)

        self.horizontalLayout_3.addWidget(self.circle_radius_spbx)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.circle_grpbx)

        self.compute_btn = QPushButton(self.centralwidget)
        self.compute_btn.setObjectName(u"compute_btn")

        self.verticalLayout_2.addWidget(self.compute_btn)

        self.result_lbl = QLabel(self.centralwidget)
        self.result_lbl.setObjectName(u"result_lbl")

        self.verticalLayout_2.addWidget(self.result_lbl)

        computeArea.setCentralWidget(self.centralwidget)

        self.retranslateUi(computeArea)

        QMetaObject.connectSlotsByName(computeArea)
    # setupUi

    def retranslateUi(self, computeArea):
        computeArea.setWindowTitle(QCoreApplication.translate("computeArea", u"Compute Area", None))
        self.groupBox.setTitle(QCoreApplication.translate("computeArea", u"Select Shape", None))
        self.shape_cmbbx.setItemText(0, QCoreApplication.translate("computeArea", u"Square", None))
        self.shape_cmbbx.setItemText(1, QCoreApplication.translate("computeArea", u"Circle", None))

        self.square_grpbx.setTitle(QCoreApplication.translate("computeArea", u"Square", None))
        self.label.setText(QCoreApplication.translate("computeArea", u"Height", None))
        self.label_2.setText(QCoreApplication.translate("computeArea", u"Width", None))
        self.circle_grpbx.setTitle(QCoreApplication.translate("computeArea", u"Circle", None))
        self.label_3.setText(QCoreApplication.translate("computeArea", u"Height", None))
        self.compute_btn.setText(QCoreApplication.translate("computeArea", u"Compute", None))
        self.result_lbl.setText(QCoreApplication.translate("computeArea", u"Result", None))
    # retranslateUi

