from PySide6  import QtWidgets, QtCore
import maya.cmds as cmds

class goofyTankUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Goofy Tanks Proxy Generator")
        self.setMinimumWidth(500)
        layout = QtWidgets.QVBoxLayout(self)
        self.turret_section(layout)
        self.hull_section(layout)
        self.barrel_section(layout)


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

        layout.addWidget(QtWidgets.QLabel("Turret Type"))
        self.turret_type = QtWidgets.QComboBox()
        self.turret_type.addItems([
            "Default",
            "Sloped",
            "Rounded",
            "Trapezoid"
        ])
        layout.addWidget(self.turret_type)

        
#Hull spinbox 
    def hull_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Hull"))

        layout.addWidget(QtWidgets.QLabel("Hull Length"))
        self.hull_length = QtWidgets.QDoubleSpinBox()
        #temporary values** Change v
        self.hull_length.setRange(1, 2)
        self.hull_length.setValue(1.0)
        layout.addWidget(self.hull_length)
        
        layout.addWidget(QtWidgets.QLabel("Hull Height"))
        self.hull_height = QtWidgets.QDoubleSpinBox()
        #temporary values** Change v
        self.hull_height.setRange(1, 2)
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
        
                
    def barrel_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Barrel"))
        
        layout.addWidget(QtWidgets.QLabel("Barrel Length"))
        self.barrel_length = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        #temporary values** Change v
        self.barrel_length.setRange(1, 5)
        self.barrel_length.setValue(1.0)
        layout.addWidget(self.barrel_length)

        layout.addWidget(QtWidgets.QLabel("Barrel Thickness"))
        self.barrel_thickness = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        #temporary values** Change v
        self.barrel_thickness.setRange(1, 5)
        self.barrel_thickness.setValue(1.0)
        layout.addWidget(self.barrel_thickness)
        

   # def tracks_section(self, layout)
        layout.addWidget(QtWidgets.QLabel("Tracks"))
        pass

generator_window = goofyTankUI()
generator_window.show()
