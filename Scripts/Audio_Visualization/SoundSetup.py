import bpy
import colorsys


def hsv_conversion_driver(hval, sval=1, vval=0.8):
    newhval = (-0.045853432 * hval) + 0.333
    return colorsys.hsv_to_rgb(newhval, sval, vval)  # returns rgb values based on hsv input


def sound_setup():
    bpy.app.driver_namespace['MatColorDriver'] = hsv_conversion_driver  # add function to driver_namespace
    print("Sound Setup Complete!")


if __name__ == "__main__":
    sound_setup()
