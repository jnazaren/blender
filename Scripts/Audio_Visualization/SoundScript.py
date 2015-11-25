import bpy
import colorsys


def hsv_conversion_driver(hval, sval=1, vval=0.8):
    newhval = (-0.045853432 * hval) + 0.333
    return colorsys.hsv_to_rgb(newhval, sval, vval)  # returns rgb values based on hsv input


def sound_visualization_scene_setup(audiopath, cubenumber=10, startfreq=28, cubeheight=10):
    bpy.app.driver_namespace['MatColorDriver'] = hsv_conversion_driver  # add function to driver_namespace
    freq = startfreq
    planesize = (((cubenumber - 1) * 1.1) + 2) / 2
    ypos = -planesize + 1
    bpy.ops.mesh.primitive_plane_add(radius=planesize, location=[0, 0, 0])
    for num in range(0, cubenumber):
        print("Creating cube " + str(num + 1))
        bpy.ops.mesh.primitive_cube_add(radius=0.5, location=[0, ypos, -(cubeheight / 2)])
        cubename = str(freq) + "Hz Channel"
        bpy.context.scene.objects.active.name = cubename
        bpy.context.scene.objects.active.scale = [1, 1, cubeheight]
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)

        bpy.ops.anim.keyframe_insert_menu(type='Location')
        bpy.context.active_object.animation_data.action.fcurves[0].lock = True
        bpy.context.active_object.animation_data.action.fcurves[1].lock = True

        bpy.context.area.type = 'GRAPH_EDITOR'

        l = (freq - 0.25 * freq)
        h = (1.5 * freq)

        print("(" + str(l) + " <-- " + str(freq) + " --> " + str(h) + ")")

        bpy.ops.graph.sound_bake(filepath=audiopath, low=(l), high=(h))

        unbake_visualization_curves()
        print("Finished unbaking values for cube " + str(num + 1) + "\n")
        # bpy.context.active_object.animation_data.action.fcurves[2].lock = True

        ypos = (ypos + 1.1)
        freq = (freq * 2)

        matvar = ('Material ' + str(num))
        bpy.context.object.data.materials.append(bpy.data.materials.new(matvar))
        fcurve = bpy.data.materials[matvar].driver_add('diffuse_color')  # sets a driver for the material color
        for drivernum in range(0, 3):  # loop to set driver properties for all three color channels
            drv = fcurve[drivernum].driver
            drv.type = 'SCRIPTED'
            drivervar = drv.variables.new()
            drivervar.name = 'var'
            drivervar.type = 'TRANSFORMS'
            drivervar.targets.items()[0][1].id = bpy.context.active_object
            drivervar.targets.items()[0][1].transform_type = 'LOC_Z'
            drv.expression = ('MatColorDriver(var)[' + str(drivernum) + ']')

            # bpy.data.materials[matvar].animation_data.drivers.items()[drivernum][1].driver.variables['var'].targets.items()[0][1].id = bpy.context.active_object
            # bpy.data.materials[matvar].animation_data.drivers.items()[drivernum][1].driver.variables['var'].targets.items()[0][1].transform_type = 'LOC_Z'
            # bpy.data.materials[matvar].animation_data.drivers.items()[drivernum][1].driver.expression = ('MatColorDriver(var)[' + str(drivernum) + ']')

        bpy.ops.object.select_pattern(pattern="*Hz*")

    print("FINISHED!\n")


def unbake_visualization_curves():
    obj = bpy.context.active_object
    for c in obj.animation_data.action.fcurves:
        if c.sampled_points and c.select:
            obj.animation_data.action = bpy.data.actions.new(name='Lot_of_Keys')
            fcu = obj.animation_data.action.fcurves.new(data_path=c.data_path, index=c.array_index)
            sam = c.sampled_points
            fcu.keyframe_points.add(len(sam))
            for i in range(len(sam)):
                w = fcu.keyframe_points[i]
                w.co = w.handle_left = w.handle_right = sam[i].co


# class SoundVizPanel(bpy.types.Panel):
#    bl_idname = "OBJECT_PT_hello_world"
#    bl_label = "Hello World"
#    bl_space_type = 'PROPERTIES'
#    bl_region_type = 'WINDOW'
#    bl_context = "object"

#    def draw(self, context):
#        self.layout.label(text="Hello World")


# bpy.utils.register_class(HelloWorldPanel)


if __name__ == "__main__":
    sound_visualization_scene_setup(
        r"C:\\Users\\Jacobson\\Videos\\Audio Visualization Blender\\alesso_heroes_youtube.mp3")
