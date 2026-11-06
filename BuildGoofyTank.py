import maya.cmds as cmds


def make_tank(inputs):

    hull_length = inputs["Hull Length"]
    hull_height = inputs["Hull Height"]
    
    turret_length = inputs["Turret Length"]
    turret_height = inputs["Turret Height"]

    track_length = inputs["Track Length"]
    track_height = inputs["Track Height"]


    hull_depth = 3

    # Creates all polys 
    hull = cmds.polyCube(
        name="Tank_Hull",
        width=hull_length,
        height=hull_height,
        depth=hull_depth
    )[0]

    # Position all polys 
    cmds.move(0, hull_height / 2, 0, hull)

    print("Hull successfully created!")


    turret_depth = 2.5

    turret = cmds.polyCube(
        name="Tank_Turret",
        width=turret_length,
        height=turret_height,
        depth= turret_depth
    )[0]
    cmds.move(0, hull_height + turret_height /2, 0, turret)

    print("Turret created!")


    track_depth = 0.5
    #L = Left
    l_track = cmds.polyCube(
        name="Tank_LTrack",
        width=track_depth,
        height=track_height,
        depth=track_length
    )[0]
    cmds.move((hull_length / 2), track_height / 2, 0 , l_track)

    #R = Right
    r_track = cmds.polyCube(
        name="Tank_RTrack",
        width=track_depth,
        height=track_height,
        depth=track_length
    )[0]
    cmds.move(-(hull_length /2), track_height / 2, 0 ,r_track)



