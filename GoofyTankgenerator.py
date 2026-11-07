import importlib

from PySide6  import QtWidgets, QtCore
import maya.cmds as cmds

import BuildGoofyTank
importlib.reload(BuildGoofyTank)

class goofyTankUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Goofy Tanks Proxy Generator")
        self.setMinimumWidth(500)
        layout = QtWidgets.QVBoxLayout(self)
        self.turret_section(layout)
        self.hull_section(layout)
        self.barrel_section(layout)
        self.tracks_section(layout)

        self.generate_tank_button = QtWidgets.QPushButton("Create Tank")
        layout.addWidget(self.generate_tank_button)
        self.generate_tank_button.clicked.connect(self.generate_tank)


#----GUI----#

#Hull spinbox 
    def hull_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Hull"))

        layout.addWidget(QtWidgets.QLabel("Hull Width"))
        self.hull_width = QtWidgets.QDoubleSpinBox()
        self.hull_width.setRange(0.2, 5)
        self.hull_width.setValue(1.0)
        layout.addWidget(self.hull_width)
        
        layout.addWidget(QtWidgets.QLabel("Hull Height"))
        self.hull_height = QtWidgets.QDoubleSpinBox()
        self.hull_height.setRange(0.2, 3)
        self.hull_height.setValue(1.0)
        layout.addWidget(self.hull_height)

        layout.addWidget(QtWidgets.QLabel("Hull Type"))
        self.hull_type = QtWidgets.QComboBox()
        self.hull_type.addItems([
            "Default",
            "Sloped",
            "Rounded",
            "Trapezoid"
        ])
        layout.addWidget(self.hull_type)


#Turret should have a input or have a spinbox 
    def turret_section(self, layout): 
        layout.addWidget(QtWidgets.QLabel("Turret"))

        layout.addWidget(QtWidgets.QLabel("Turret Width"))
        self.turret_width = QtWidgets.QDoubleSpinBox()
        self.turret_width.setRange(0.2, 5)
        self.turret_width.setValue(1.0)
        layout.addWidget(self.turret_width)

        layout.addWidget(QtWidgets.QLabel("Turret Height"))
        self.turret_height = QtWidgets.QDoubleSpinBox()
        self.turret_height.setRange(0.2, 5)
        self.turret_height.setValue(1.0)
        layout.addWidget(self.turret_height)

        layout.addWidget(QtWidgets.QLabel("Turret Type"))
        self.turret_type = QtWidgets.QComboBox()
        self.turret_type.addItems([
            "Default",
            "Sloped",
            "Rounded",
            "Trapezoid"
        ])
        layout.addWidget(self.turret_type)

                
    def barrel_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Barrel"))
        
        layout.addWidget(QtWidgets.QLabel("Barrel Length"))
        self.barrel_length = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.barrel_length.setRange(0.2, 5)
        self.barrel_length.setValue(1.0)
        layout.addWidget(self.barrel_length)

        layout.addWidget(QtWidgets.QLabel("Barrel Thickness"))
        self.barrel_thickness = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.barrel_thickness.setRange(0.2, 5)
        self.barrel_thickness.setValue(1.0)
        layout.addWidget(self.barrel_thickness)

        layout.addWidget(QtWidgets.QLabel("Gun Type"))
        self.gun_type = QtWidgets.QComboBox()
        self.gun_type.addItems([
            "Default",
            "Laser",
            "Cannon"
        ])
        layout.addWidget(self.gun_type)


    def tracks_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Tracks"))

        layout.addWidget(QtWidgets.QLabel("Track Length"))
        self.track_length = QtWidgets.QDoubleSpinBox()
        self.track_length.setRange(0.2, 5)
        self.track_length.setValue(1.0)
        layout.addWidget(self.track_length)

        layout.addWidget(QtWidgets.QLabel("Track Height"))
        self.track_height = QtWidgets.QDoubleSpinBox()
        self.track_height.setRange(0.2, 3)
        self.track_height.setValue(1.0)
        layout.addWidget(self.track_height)

    def generate_tank(self):

        inputs = self.get_input()
        BuildGoofyTank.make_tank(inputs)
        print("If you read this: goofy tanks on their way")
        print(inputs)

    def get_input(self):
        inputs = {

            "Hull Width": self.hull_width.value()+1.5,
            "Hull Height": self.hull_height.value(),
            "Hull Type": self.hull_type.currentText(),


            "Turret Width": self.turret_width.value()+0.4,
            "Turret Height": self.turret_height.value(),
            "Turret Type": self.turret_type.currentText(),


            "Barrel Length": self.barrel_length.value()+0.5,
            "Barrel Thickness": self.barrel_thickness.value(),
            "Gun Type": self.gun_type.currentText(),


            "Track Length": self.track_length.value()+2.5 ,
            "Track Height": self.track_height.value(),
        }
        return inputs

