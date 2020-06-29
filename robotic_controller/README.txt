# ROBOTIC CONTROLLER ROS PACKAGE v1.0 - 21.5.20
#############################################
Information
-----------
The Robotic Controller package is a package for operating the "Robotic Control Interface" on ROS.
This study was developed as a project for Object Oriented Programming II course in Eskişehir Osmangazi University Electrical and Electronics Engineering Department.

Contents
-----------
- robotic_controller.py
- robotic_controller.launch (for using in ROS)
- robotic_controller.ui (Qt file)
- images and icons.qrc files

Descriptions
------------

- To use the interface, any ROS robot must be running (or roscore).
- The package must be installed in any ROS working environment for the interface to work.The python file should then be activated:
	$ chmod +x robotic_controller.py
- To run the launch file:
	$ roslaunch robotic_controller robotic_controller.launch
- To run the python file directly:
	$ rosrun robotic_controller robotic_controller.py

What the Program Can Do
-----------------------
- Motion control of a robot spawned to the Gazebo environment can be provided.
- Instant location information of this robot can be obtained.

What the Program Can't Do
-------------------------
- Since the icon files cannot be converted to python form, the icons in the interface are not visible.

Contributor
-----------
- Alim Kerem ERDOĞMUŞ
