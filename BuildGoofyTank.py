import maya.cmds as cmds


def make_tank(inputs):

    hull_width = inputs["Hull Width"]
    hull_height = inputs["Hull Height"]
    
    turret_width = inputs["Turret Width"]
    turret_height = inputs["Turret Height"]

    track_length = inputs["Track Length"]
    track_height = inputs["Track Height"]

    barrel_length = inputs["Barrel Length"]
    barrel_thickness = inputs["Barrel Thickness"]

    hull_type = inputs["Hull Type"]


    hull_depth = 3

    if hull_type == "Default":
 
        hull = cmds.polyCube(
            name="Default_tankHull",
            width=hull_width,
            height=hull_height,
            depth=hull_depth
        )[0]

    elif hull_type == "Rounded": 
        hull = cmds.polySphere(
            name="Rounded_tankHull",
            radius=1
        )[0]
        cmds.scale(
            hull_width / 2,
            hull_height / 1.5,
            hull_depth / 2, 
        )

    # Position all polys 
    cmds.move(0, (hull_height / 2 +0.2), 0, hull)


    turret_depth = 2.0

    turret = cmds.polyCube(
        name="Tank_Turret",
        width=turret_width,
        height=turret_height,
        depth= turret_depth
    )[0]
    cmds.move(0, (hull_height + turret_height /2 + 0.2), 0, turret)


    track_depth = 0.5

    #L = Left
    l_track = cmds.polyCube(
        name="Tank_LTrack",
        width=track_depth,
        height=track_height,
        depth=track_length
    )[0]
    cmds.move((hull_width / 2), track_height / 2, 0 , l_track)


    #R = Right
    r_track = cmds.polyCube(
        name="Tank_RTrack",
        width=track_depth,
        height=track_height,
        depth=track_length
    )[0]
    cmds.move(-(hull_width /2), track_height / 2, 0 ,r_track)


    barrel = cmds.polyCylinder(
        name="Tank_Gun",
        radius=barrel_thickness * 0.1,
        height=barrel_length
    )[0]
    cmds.rotate(90,0,0, barrel)
    cmds.move(0, (hull_height + turret_height /2 + 0.2), 
              (turret_depth /2 + barrel_length /2 ), barrel)

    tank_group = cmds.group(
        hull,
        turret,
        barrel,
        l_track,
        r_track,
        name= "GoofyTank_GRP"
    )

    return tank_group


