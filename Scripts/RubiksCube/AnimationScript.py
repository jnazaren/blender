import bpy
from math import pi


def CubeAnimation(startframe=0, turnLength=30):
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            override = {'area': area}
            bpy.ops.screen.screen_full_area(override)
            break
    bpy.data.scenes["Scene"].frame_current = startframe
    for object in bpy.context.scene.objects:
        if object.type == 'MESH' and object.name.startswith("Cube"):
            object.select = True
        else:
            object.select = False
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')

    turn = 1
    userInput = "NEW"
    while userInput != "":
        userInput = input("Enter command or blank to stop animating: ")
        if userInput == "L":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 1, -2.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "L'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 1, -2.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "MY":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 1, 0.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "MY'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 1, 0.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "R":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 1, 3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "R'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 1, 3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "U":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 2, 6.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(False, False, True))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "U'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 2, 6.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(False, False, True))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "MZ":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 2, 3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(False, False, True))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "MZ'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 2, 3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(False, False, True))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "D":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 2, 0.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(False, False, True))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "D'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 2, 0.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(False, False, True))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "F":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 0, 3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(True, False, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "F'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 0, 3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(True, False, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "MX":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 0, 0.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(True, False, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "MX'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 0, 0.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(True, False, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "B":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 0, -3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=(pi/2), constraint_axis=(True, False, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "B'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and polygon_found(object, 0, -3.0):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set(startframe + turnLength * turn)
            bpy.ops.transform.rotate(value=-(pi/2), constraint_axis=(True, False, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path="location")
                object.keyframe_insert(data_path="rotation_euler")

        elif userInput == "Next" or userInput == "next":
            for object in bpy.context.scene.objects:
                if object.type == 'MESH' and object.name.startswith("Cube"):
                    object.keyframe_insert(data_path="location")
                    object.keyframe_insert(data_path="rotation_euler")
                else:
                    continue
            turn += 1
            bpy.data.scenes['Scene'].update()

        else:
            userInput = ""
            bpy.data.scenes["Scene"].frame_set(startframe)
            break

def polygon_found(obj, index, value):
    lobj = [polygon.center for polygon in obj.data.polygons]
    lworld = [obj.matrix_world * vector for vector in lobj]
    for position in lworld:
        if (value - 0.1) < position[index] < (value + 0.1):
            return True
    return False


if __name__ == "__main__":
    CubeAnimation(bpy.data.scenes["Scene"].frame_current)
