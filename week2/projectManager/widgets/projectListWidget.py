from PySide6.QtWidgets import (
    QListWidget, QListWidgetItem
)
from PySide6.QtCore import Qt, Slot, Signal

import os
import settings
import createProject

class projectListClass(QListWidget):
    def __init__(self):
        super(projectListClass, self).__init__()

    def updateProjectList(self):
        self.clear()
        data = settings.Settings().load()
        path = data.get("path")
        if path:
            if os.path.exists(path):
                for f in os.listdir(path):
                    fullpath = os.path.join(path, f)
                    if self.is_project(fullpath):
                        item = self.add_project(f)
                        item.setData(32, fullpath) # 32 == userdata
        return data

    def is_project(self, path):
        return os.path.exists(os.path.join(path, createProject.project_file))

    def add_project(self, name):
        item = QListWidgetItem()
        item.setText(name)
        self.addItem(item)
        return item
