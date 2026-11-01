from PySide6  import QtWidgets, QtCore
import maya.cmds as cmds

class goofyTankUI(QtWidgets.QDialog):

    def __init_(self):
        super().__init__()

        self.setWindowTitle("Goofy Tanks Proxy Generator")
        self.create_layout()
        self.create_connections()

    


generator_window = goofyTankUI()
generator_window.show()