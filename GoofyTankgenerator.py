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
        self.tracks_section(layout)

        self.generate_tank_button = QtWidgets.QPushButton("Create Tank")
        layout.addWidget(self.generate_tank_button)
        self.generate_tank_button.clicked.connect(self.generate_tank)


#----GUI----#

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

        layout.addWidget(QtWidgets.QLabel("Gun Type"))
        self.gun_type = QtWidgets.QComboBox()
        self.gun_type.addItems([
            "Standard",
            "Laser",
            "Cannon"
        ])
        layout.addWidget(self.gun_type)

    def tracks_section(self, layout):
        layout.addWidget(QtWidgets.QLabel("Tracks"))

        layout.addWidget(QtWidgets.QLabel("Track Length"))
        self.track_length = QtWidgets.QDoubleSpinBox()
        #temporary values** Change v
        self.track_length.setRange(1, 5)
        self.track_length.setValue(1.0)
        layout.addWidget(self.track_length)

        layout.addWidget(QtWidgets.QLabel("Track Height"))
        self.track_height = QtWidgets.QDoubleSpinBox()
        #temporary values** Change v
        self.track_height.setRange(1, 5)
        self.track_height.setValue(1.0)
        layout.addWidget(self.track_height)

        layout.addWidget(QtWidgets.QLabel("Track Type"))
        self.track_type = QtWidgets.QComboBox()
        self.track_type.addItems([
            "Default",
            "Low Track",
            "High Track",
            "Wheeld Track"
        ])
        layout.addWidget(self.track_type)

    def generate_tank(self):
        inputs = self.get_input()
        print("If you read this: goofy tanks on their way")
        print(inputs)

    def get_input(self):
        inputs = {
            "Turret Length": self.turret_length.value(),

        }
        return inputs


generator_window = goofyTankUI()
generator_window.show()
