from PySide6  import QtWidgets, QtCore
import maya.cmds as cmds

class goofyTankUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Goofy Tanks Proxy Generator")
        self.setMinimumWidth(500)
        layout = QtWidgets.QVBoxLayout(self)
        self.turret_section(layout)


#Turret should have a input or have a spinbox 
    def turret_section(self, layout): 
        layout.addWidget(QtWidgets.QLabel("Turret"))

        layout.addWidget(QtWidgets.QLabel("Turret Length"))
        self.turret_length = QtWidgets.QDoubleSpinBox()
        #temporary values** Change v
        self.turret_length.setRange(1, 2)
        self.turret_length.setValue(1.0)
        layout.addWidget(self.turret_length)

        layout.addWidget(QtWidgets.QLabel("Turret Height"))
        self.turret_height = QtWidgets.QDoubleSpinBox()
        #temporary values** Change v
        self.turret_height.setRange(1, 2)
        self.turret_height.setValue(1.0)
        layout.addWidget(self.turret_height)
        


    


   # def hull_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Hull"))
        pass

   # def barrel_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Barrel"))
        pass

   # def tracks_section(self, layout)
        layout.addWidget(QtWidgets.QLabel("Tracks"))
        pass



generator_window = goofyTankUI()
generator_window.show()