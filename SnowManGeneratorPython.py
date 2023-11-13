import maya.cmds as cmds

def create_snowman():
    # Create the body (three spheres representing the snowman's body parts)
    body_bottom = cmds.polySphere(radius=5, name="body_bottom")[0]
    body_middle = cmds.polySphere(radius=4, name="body_middle")[0]
    body_top = cmds.polySphere(radius=3, name="body_top")[0]

    # Position the body parts
    cmds.move(0, 0, 0, body_bottom)
    cmds.move(0, 8, 0, body_middle)
    cmds.move(0, 15, 0, body_top)

    # Create eyes (two small spheres)
    eye_left = cmds.polySphere(radius=0.5, name="eye_left")[0]
    eye_right = cmds.polySphere(radius=0.5, name="eye_right")[0]

    # Position the eyes relative to the head
    
    cmds.xform(eye_left, translation=(-0.5, 15.878, 2.677))
    cmds.xform(eye_right, translation=(0.878, 15.878, 2.745))

    # Create a nose (a cone)
    nose = cmds.polyCone(radius=0.3, height=2, name="nose")[0]

    # Position the nose
    cmds.move(0, 15.256, 4.137, nose)
    cmds.rotate(90, 0, 90, nose)  # Rotate the nose for a diagonal appearance

    # Create a mouth (a series of small spheres)
    mouth1 = cmds.polySphere(radius=0.3, name="mouth1")[0]
    mouth2 = cmds.polySphere(radius=0.3, name="mouth2")[0]
    mouth3 = cmds.polySphere(radius=0.3, name="mouth3")[0]

    # Position the mouth spheres
    cmds.move(-0.5, 14.556, 2.882, mouth1)
    cmds.move(.29, 14.361, 2.897, mouth2)
    cmds.move(1.132, 14.507, 2.916, mouth3)

    # Create a hat (a cylinder and a cone)
    hat_cylinder = cmds.polyCylinder(radius=4, height=1, name="hat_cylinder")[0]
    hat_cone = cmds.polyCone(radius=5, height=3, name="hat_cone")[0]

    # Position the hat parts
    cmds.move(0, 17.497, 0, hat_cylinder)
    cmds.move(0, 19.473, 0, hat_cone)

    # Group all the snowman parts
    snowman_group = cmds.group([body_bottom, body_middle, body_top, eye_left, eye_right, nose, mouth1, mouth2, mouth3, hat_cylinder, hat_cone],
                               name="snowman_group")

    cmds.warning("Snowman created!")

# Call the function to create the snowman
create_snowman()
