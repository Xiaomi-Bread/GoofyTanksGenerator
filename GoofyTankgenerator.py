from PySide6  import QtWidgets, QtCore
import maya.cmds as cmds

class goofyTankUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Goofy Tanks Proxy Generator")
        self.setMinimumWidth(500)

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(QtWidgets.QLabel("Turret"))
        layout.addWidget(QtWidgets.QLabel("Hull"))
        layout.addWidget(QtWidgets.QLabel("Barrel"))
        layout.addWidget(QtWidgets.QLabel("Tracks"))


generator_window = goofyTankUI()
generator_window.show()