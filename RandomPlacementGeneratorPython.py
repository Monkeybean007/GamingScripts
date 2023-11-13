import maya.cmds as cmds
import random

def duplicate_and_disperse(num_duplicates, min_x, max_x, min_y, max_y, min_z, max_z):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True, dag=True, long=True)

    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    # Duplicate the selected objects
    duplicated_objects = cmds.duplicate(selected_objects, returnRootsOnly=True)

    # Check if any objects were duplicated
    if not duplicated_objects:
        cmds.warning("Failed to duplicate objects.")
        return

    # Randomly disperse the duplicated objects
    for i in range(num_duplicates):
        # Check if the index is within the range of duplicated objects
        if i < len(duplicated_objects):
            # Get random positions within the specified range
            random_x = random.uniform(min_x, max_x)
            random_y = random.uniform(min_y, max_y)
            random_z = random.uniform(min_z, max_z)

            # Translate the duplicated object to the random position
            cmds.move(random_x, random_y, random_z, duplicated_objects[i])

            cmds.warning(f"{duplicated_objects[i]} duplicated and dispersed to ({random_x}, {random_y}, {random_z}).")


# Duplicate and disperse the selected object(s) 5 times within the specified range
duplicate_and_disperse(5, -10, 10, -5, 5, 0, 20)
