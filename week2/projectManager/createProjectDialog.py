from PySide6.QtWidgets import (
    QDialog
)
from PySide6.QtCore import Qt, Slot, Signal

from widgets import createProjectDialogUi as ui

class CreateProjectDialog(QDialog, ui.Ui_createDialog):
    def __init__(self, parent):
        super(CreateProjectDialog, self).__init__(parent)
        self.setupUi(self)

        # connections
        self.create_btn.clicked.connect(self.do_create)
        self.cancel_btn.clicked.connect(self.reject)

    def do_create(self):
        if self.name_lb.text():
            self.accept()

    def get_dialog_data(self):
        return dict(
            name=self.name_lb.text(),
            comment=self.comment_pte.toPlainText()
        )