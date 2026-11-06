import maya.cmds as cmds


def make_tank(inputs):

    hull_length = inputs["Hull Length"]
    hull_height = inputs["Hull Height"]
    
    turret_length = inputs["Turret Length"]
    turret_height = inputs["Turret Height"]

    # Creates all polys 
    hull = cmds.polyCube(
        name="Tank_Hull",
        width=hull_length,
        height=hull_height,
        depth=3
    )[0]

    # Position all polys 
    cmds.move(0, hull_height / 2, 0, hull)

    print("Hull successfully created!")

    turret = cmds.polyCube(
        name="Tank_Turret",
        width=turret_length,
        height=turret_height,
        depth=2
    )[0]
    cmds.move(0, hull_height + turret_height /2, 0, turret)

    print("Turret created!")

