import maya.cmds as cmds

def change_shape_override_color(color):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True, dag=True, shapes=True)

    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    # Iterate through the selected objects and change the override color
    for obj in selected_objects:
        # Get the shape node of the object
        shape_node = cmds.listRelatives(obj, shapes=True, fullPath=True)

        if shape_node:
            # Check if the shape node has an override
            if cmds.getAttr(shape_node[0] + ".overrideColor"):
                # Change the override color
                cmds.setAttr(shape_node[0] + ".overrideColor", color)
                cmds.warning(f"Override color changed to {color} for {shape_node[0]}.")
            else:
                cmds.warning(f"{shape_node[0]} does not have an override color.")

# Example usage:
# Change the override color to red (color index 13)
change_shape_override_color(11)
