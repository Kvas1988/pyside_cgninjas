from PySide6.QtWidgets import QWidget, QTreeWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from widgets import templateEditorUi as ui
import os
import json

templateFile = os.path.join(os.path.dirname(__file__), "template.json")

class templateEditor(QWidget, ui.Ui_templateEditor):
    def __init__(self):
        super(templateEditor, self).__init__()
        self.setupUi(self)
        # UI
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # connections
        self.add_btn.clicked.connect(self.add_item)
        self.remove_btn.clicked.connect(self.remove_item)
        self.save_btn.clicked.connect(self.save_template)
        self.cancel_btn.clicked.connect(self.close)
        # start
        self.loadTemplate()

    def add_item(self, name="Folder", parent=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        item = QTreeWidgetItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable |
                      Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        item.setText(0, name)
        item.setExpanded(1)
        parent.addChild(item)
        return item

    def remove_item(self):
        items = self.tree.selectedItems()
        for i in items:
            (i.parent() or self.tree.invisibleRootItem()).takeChild(self.tree.indexFromItem(i).row())

    def save_template(self):
        template = self.getStructure()
        # print(template)
        with open(templateFile, "w") as f:
            json.dump(template, f, indent=4)
        self.close()

    def getStructure(self, parent=None):
        structure = []
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in range(parent.childCount()):
            ch = parent.child(i)
            content = self.getStructure(ch)
            structure.append({"name": ch.text(0), "content": content})
        return structure

    def loadTemplate(self):
        if os.path.exists(templateFile):
            with open(templateFile) as f:
                template = json.load(f)
                self.restoreStructure(template)

    def restoreStructure(self, data, parent=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in data:
            item = self.add_item(i["name"], parent)
            self.restoreStructure(i["content"], item)