# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'templateEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_templateEditor(object):
    def setupUi(self, templateEditor):
        if not templateEditor.objectName():
            templateEditor.setObjectName(u"templateEditor")
        templateEditor.resize(482, 374)
        self.verticalLayout = QVBoxLayout(templateEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_btn = QPushButton(templateEditor)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.add_btn)

        self.remove_btn = QPushButton(templateEditor)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.remove_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tree = QTreeWidget(templateEditor)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree.setHeaderItem(__qtreewidgetitem)
        self.tree.setObjectName(u"tree")
        self.tree.setColumnCount(1)
        self.tree.header().setVisible(False)

        self.verticalLayout.addWidget(self.tree)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.save_btn = QPushButton(templateEditor)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_2.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(templateEditor)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(templateEditor)

        QMetaObject.connectSlotsByName(templateEditor)
    # setupUi

    def retranslateUi(self, templateEditor):
        templateEditor.setWindowTitle(QCoreApplication.translate("templateEditor", u"Form", None))
        self.add_btn.setText(QCoreApplication.translate("templateEditor", u"Add", None))
        self.remove_btn.setText(QCoreApplication.translate("templateEditor", u"Remove", None))
        self.save_btn.setText(QCoreApplication.translate("templateEditor", u"Save", None))
        self.cancel_btn.setText(QCoreApplication.translate("templateEditor", u"Cancel", None))
    # retranslateUi

