# Blender Scripts & Addons
This repository contains scripts and addons I make for Blender (http://www.blender.org/). Projects include the following:

## Audio Spectrum Visualization
This is a script I created to create an animated set of audio spectrum bars from an audio file. The script takes the audio file's directory and amount of bars/frequencies (optional) the user wants to visualize as arguments, and uses a separate scripts to set the variable color scheme of each bar's material. 

## Rubik's Cube Animaion
This is a script which allows a user to easily animate a fully-textured model of a Rubik's Cube, based on commands entered into the Blender console window. The script takes into consideration the current frame and makes it the start of the animation (by default, but this argument can optionally be changed). It also takes an optional argument for the amount of frames per turn. 
**Note: Blender console window must be open while the script is running, and screen will update the 3D viewport every time a user enters a turn command. 

-- My hope is to eventually turn these primative Blender 'scripts' into full Blender addons, but this will take some more experimentation with the Blender python API

###Jacob Nazarenko