import maya.cmds as cmds


def make_tank(inputs):

    hull_length = inputs["Hull Length"]
    hull_height = inputs["Hull Height"]

    # Create hull
    hull = cmds.polyCube(
        name="Tank_Hull",
        width=hull_length,
        height=hull_height,
        depth=3
    )[0]

    # Position hull
    cmds.move(0, hull_height / 2, 0, hull)

    print("Hull successfully created!")

    return hull