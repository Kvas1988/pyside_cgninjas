import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel,
    QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PySide6.QtCore import Qt, Slot, Signal

from computeArea_ui import Ui_computeArea
from math import pi


class ComputeArea(QMainWindow):
    def __init__(self):
        super(ComputeArea, self).__init__()
        self.ui = Ui_computeArea()
        self.ui.setupUi(self)

        # connects
        self.ui.shape_cmbbx.currentIndexChanged.connect(self.update_ui)
        self.ui.compute_btn.clicked.connect(self.compute)

        # start
        self.update_ui()

    def update_ui(self):
        self.ui.square_grpbx.setVisible(self.ui.shape_cmbbx.currentIndex() == 0)
        self.ui.circle_grpbx.setVisible(self.ui.shape_cmbbx.currentIndex() == 1)

    def compute(self):
        if self.ui.shape_cmbbx.currentIndex() == 0:
            self.computeSquare()
        elif self.ui.shape_cmbbx.currentIndex() == 1:
            self.computeCircle()

    def computeSquare(self):
        h = self.ui.square_height_spbx.value()
        w = self.ui.square_width_spbx.value()
        area = w * h
        self.showResult(area)

    def computeCircle(self):
        r = self.ui.circle_radius_spbx.value()
        area = pi * (r**2)
        self.showResult(area)

    def showResult(self, result):
        self.ui.result_lbl.setText("Result: %.3f" % result)


def main():
    app = QApplication(sys.argv)
    w = ComputeArea()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()
