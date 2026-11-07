import maya.cmds as cmds
import random


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
    turret_type = inputs["Turret Type"]
    gun_type = inputs["Gun Type"]



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
            hull
        )

    elif hull_type == "Sloped":

        hull = cmds.polyCube(
            name="Sloped_tankHull",
            width=hull_width,
            height=hull_height,
            depth=hull_depth
        )[0]

        for i in range(cmds.polyEvaluate(hull, vertex=True)):
                vertex = f"{hull}.vtx[{i}]"

                pos = cmds.xform(
                    vertex,
                    query=True,
                    objectSpace=True,
                    translation=True
                )

                if pos[1] > 0 and pos[2] > 0:
                    pos[2] -= hull_depth * 0.2

                    cmds.xform(
                        vertex,
                        objectSpace=True,
                        translation=pos
                    )

    elif hull_type == "Trapezoid":
        hull = cmds.polyCube(
            name="Trapzoid_tankHull",
            width=hull_width,
            height=hull_height,
            depth=hull_depth
        )[0]

        vertex_count = cmds.polyEvaluate(hull, vertex=True)

        for i in range(vertex_count):
            vertex = f"{hull}.vtx[{i}]"
            trap_position = cmds.xform(
                vertex,
                query=True,
                worldSpace=True,
                translation=True
            )
            if trap_position[1] > hull_height * 0.4:
                cmds.scale(0.75, 1, 0.75, vertex, relative=True)

    # Position to all hull
    cmds.move(0, (hull_height / 2 +0.2), 0, hull)



    turret_depth = 2.0

    if turret_type == "Default":
        turret = cmds.polyCube(
            name="Tank_Turret",
            width=turret_width,
            height=turret_height,
            depth= turret_depth
        )[0]

    elif turret_type == "Rounded": 
        turret = cmds.polySphere(
            name="Rounded_tankTurret",
            radius=1 
        )[0]

        cmds.scale(
            turret_width /1.5, 
            turret_height /2,
            turret_depth /2,
            turret
        )

    elif turret_type == "Sloped":
        turret = cmds.polyCube(
            name="Sloped_tankTurret",
            width=turret_width,
            height=turret_height,
            depth= turret_depth
        )[0]

        for i in range(cmds.polyEvaluate(turret, vertex=True)):
                vertex = f"{turret}.vtx[{i}]"

                pos = cmds.xform(
                    vertex,
                    query=True,
                    objectSpace=True,
                    translation=True
                )

                if pos[1] > 0 and pos[2] > 0:
                    pos[2] -= turret_depth * 0.2

                    cmds.xform(
                        vertex,
                        objectSpace=True,
                        translation=pos
                    )


    elif turret_type == "Trapezoid":
        turret = cmds.polyCube(
            name="Sloped_tankTurret",
            width=turret_width,
            height=turret_height,
            depth= turret_depth
        )[0]

        for i in range(cmds.polyEvaluate(turret, vertex=True)):
            vertex = f"{turret}.vtx[{i}]"
        
            pos = cmds.xform(
                vertex,
                query=True,
                objectSpace=True,
                translation=True
            )
        
            if pos[1] > 0:
                pos[0] *= 0.75
                pos[2] *=0.75
        
                cmds.xform(
                    vertex,
                    objectSpace=True,
                    translation=pos
            )


    # Position to all turrets
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




    barrel_y = hull_height + turret_height /2 + 0.2
    barrel_z = turret_depth /2 + barrel_length / 2 -0.2

    if gun_type == "Default":
        barrel = cmds.polyCylinder(
            name="Default_tankGun",
            radius=barrel_thickness * 0.1,
            height=barrel_length   
        )[0]
        cmds.rotate(90, 0, 0, barrel)

    elif gun_type == "Laser":
        barrel = cmds.polyCube(
            name="Laser_tankGun",
            width=barrel_thickness * 0.25,
            height=barrel_thickness * 0.5,
            depth =barrel_length
        )[0]


    elif gun_type == "Cannon":

        barrel = cmds.polyCylinder(
            name="Cannon_tankGun",
            radius=barrel_thickness * 0.1,
            height=barrel_length,
            subdivisionsHeight=8,
            subdivisionsAxis=16
        )[0]
        cmds.rotate(90, 0, 0, barrel)

        vertex_count = cmds.polyEvaluate(barrel, vertex=True)

        for i in range(vertex_count):

            vertex = f"{barrel}.vtx[{i}]"

            pos = cmds.xform(
                vertex,
                query=True,
                objectSpace=True,
                translation=True
            )

            if pos[1] > barrel_length * 0.25:

                factor = 1 + (
                    0.8 *
                    (pos[1] - barrel_length * 0.25) /
                    (barrel_length * 0.5 - barrel_length * 0.25)
                )
            
                cmds.xform(
                    vertex,
                    objectSpace=True,
                    translation=[
                        pos[0] * factor,
                        pos[1],
                        pos[2] * factor
                    ]
                )
    cmds.move(0, barrel_y, barrel_z, barrel)

    tank_group = cmds.group(
        hull,
        turret,
        barrel,
        l_track,
        r_track,
        name= "GoofyTank_GRP"
    )

    return tank_group

def random_tank_inputs():
    return{
        "Hull Width": round(random.uniform(2.5, 5.5), 2)
    }






