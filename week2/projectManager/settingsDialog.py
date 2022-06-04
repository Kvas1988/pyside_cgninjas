from PySide6.QtWidgets import (
    QDialog, QTableWidgetItem
)
from PySide6.QtCore import Qt, Slot, Signal

from widgets import settingsDialogUi as ui
import settings

class SettingsDialog(QDialog, ui.Ui_settingsDialog):
    def __init__(self, parent):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)
        # UI
        self.table.setColumnCount(2)

        # start
        self.fillTable()


    def fillTable(self):
        data = settings.Settings().load()
        for key, value in data.items():
            self.addParam(key, value)

    def addParam(self, param, value):
        self.table.insertRow(self.table.rowCount())
        item = QTableWidgetItem()
        item.setText(param)
        self.table.setItem(self.table.rowCount()-1, 0, item)

        item = QTableWidgetItem()
        item.setText(value)
        self.table.setItem(self.table.rowCount()-1, 1, item)

    def getTableData(self):
        data = dict()
        for i in range(self.table.rowCount()):
            param = self.table.item(i, 0).text()
            value = self.table.item(i, 1).text()
            data[param] = value
        return data