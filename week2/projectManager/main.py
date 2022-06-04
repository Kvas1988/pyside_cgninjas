import subprocess
import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel,
    QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PySide6.QtCore import Qt, Slot, Signal

import createProjectDialog
import settingsDialog
import tempateEditor
import settings
import createProject

from widgets import projectManagerUi
from widgets import projectListWidget

class ProjectManager(QMainWindow, projectManagerUi.Ui_ProjectManager):
    def __init__(self):
        super(ProjectManager, self).__init__()
        # self.ui = projectManagerUi.Ui_ProjectManager()
        self.setupUi(self)
        # widgets
        self.project_list_lwdg = projectListWidget.projectListClass()
        self.project_list_ly.addWidget(self.project_list_lwdg)

        # connections
        self.create_btn.clicked.connect(self.createProject)
        self.settings_btn.clicked.connect(self.openSettingsDialog)
        self.template_btn.clicked.connect(self.openTemplateEditorDialog)
        self.project_list_lwdg.itemClicked.connect(self.showInfo)
        self.project_list_lwdg.itemDoubleClicked.connect(self.open_project)

        # start
        self.updateList()
        self.info_lbl.setText("")


    def updateList(self):
        if not self.project_list_lwdg.updateProjectList():
            self.create_btn.setEnabled(0)
        else:
            self.create_btn.setEnabled(1)

    def openSettingsDialog(self):
        self.dial = settingsDialog.SettingsDialog(self)
        if self.dial.exec():
            # print("Settings OK")
            data = self.dial.getTableData()
            settings.Settings().save(data)
        self.updateList()

    def openTemplateEditorDialog(self):
        self.dial = tempateEditor.templateEditor()
        self.dial.show()

    def createProject(self):
        self.dial = createProjectDialog.CreateProjectDialog(self)
        if self.dial.exec():
            data = self.dial.get_dialog_data()
            createProject.create_project(data)
            self.updateList()


    def showInfo(self, item):
        info = createProject.get_project_info(item.data(32))
        if info:
            text = """Name:
%s

Comment:
%s
            """ % (info["name"], info["comment"])
        else:
            text =""
        self.info_lbl.setText(text)

    def open_project(self, item):
        path = item.data(32)
        # webbrowser.open(path)
        # if sys.platform == "darwin": # darwin\linux2\win32
        subprocess.check_call(["open", "--", path]) # macOs(darwin)
        # subprocess.check_call(["xdg-open", "--", path])  # linux2
        # subprocess.check_call(['explorer', path])  # win32


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ProjectManager()
    w.show()
    app.exec()
