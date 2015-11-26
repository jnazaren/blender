import bpy
import math
import Redraw
import Intersection

def CubeAnimation(startframe = 1, turnLength = 30):
    """bpy.utils.register_class(ModalTimerOperator)"""
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
    bpy.ops.anim.keyframe_insert_menu(type = 'BUILTIN_KSI_LocRot')

    turn = 1
    userInput = "NEW"
    while userInput != "":
        userInput = input("Enter command or blank to stop animating: ")
        if userInput == "L":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and Intersection.bmesh_check_intersect_objects(object, bpy.data.objects['Plane_VL']):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set((startframe-1) + turnLength*turn)
            bpy.ops.transform.rotate(value = -(math.pi/2), constraint_axis = (False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path = "location")
                object.keyframe_insert(data_path = "rotation_euler")
            bpy.data.scenes["Scene"].frame_set(startframe)

        elif userInput == "M":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and Intersection.bmesh_check_intersect_objects(object, bpy.data.objects['Plane_VM']):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set((startframe-1) + turnLength*turn)
            bpy.ops.transform.rotate(value = -(math.pi/2), constraint_axis = (False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path = "location")
                object.keyframe_insert(data_path = "rotation_euler")
            bpy.data.scenes["Scene"].frame_set(startframe)

        elif userInput == "R'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and Intersection.bmesh_check_intersect_objects(object, bpy.data.objects['Plane_VR']):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set((startframe-1) + turnLength*turn)
            bpy.ops.transform.rotate(value = -(math.pi/2), constraint_axis = (False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path = "location")
                object.keyframe_insert(data_path = "rotation_euler")
            bpy.data.scenes["Scene"].frame_set(startframe)

        elif userInput == "L'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and Intersection.bmesh_check_intersect_objects(object, bpy.data.objects['Plane_VL']):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set((startframe-1) + turnLength*turn)
            bpy.ops.transform.rotate(value = (math.pi/2), constraint_axis = (False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path = "location")
                object.keyframe_insert(data_path = "rotation_euler")
            bpy.data.scenes["Scene"].frame_set(startframe)

        elif userInput == "M'":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and Intersection.bmesh_check_intersect_objects(object, bpy.data.objects['Plane_VM']):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set((startframe-1) + turnLength*turn)
            bpy.ops.transform.rotate(value = (math.pi/2), constraint_axis = (False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path = "location")
                object.keyframe_insert(data_path = "rotation_euler")
            bpy.data.scenes["Scene"].frame_set(startframe)

        elif userInput == "R":
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and Intersection.bmesh_check_intersect_objects(object, bpy.data.objects['Plane_VR']):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set((startframe-1) + turnLength*turn)
            bpy.ops.transform.rotate(value = (math.pi/2), constraint_axis = (False, True, False))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path = "location")
                object.keyframe_insert(data_path = "rotation_euler")
            bpy.data.scenes["Scene"].frame_set(startframe)

        elif userInput == "U":
            bpy.data.scenes['Scene'].update()
            for object in bpy.context.scene.objects:
                if object.name.startswith("Cube") and Intersection.bmesh_check_intersect_objects(object, bpy.data.objects['Plane_HT']):
                    object.select = True
                else:
                    object.select = False
            bpy.data.scenes["Scene"].frame_set((startframe-1) + turnLength*turn)
            bpy.ops.transform.rotate(value = -(math.pi/2), constraint_axis = (False, False, True))
            bpy.data.scenes['Scene'].update()
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            for object in bpy.context.selected_objects:
                object.keyframe_insert(data_path = "location")
                object.keyframe_insert(data_path = "rotation_euler")
            bpy.data.scenes["Scene"].frame_set(startframe)

        elif userInput == "Next" or userInput == "next":
            bpy.data.scenes["Scene"].frame_set(startframe + (turnLength*turn))
            for object in bpy.context.scene.objects:
                if object.type == 'MESH' and object.name.startswith("Cube"):
                    object.keyframe_insert(data_path = "location")
                    object.keyframe_insert(data_path = "rotation_euler")
                else:
                    continue
            bpy.data.scenes["Scene"].frame_set(startframe)
            turn += 1
            bpy.data.scenes['Scene'].update()

        else:
            userInput = ""
            break



if __name__ == "__main__":
    CubeAnimation(bpy.data.scenes["Scene"].frame_current)