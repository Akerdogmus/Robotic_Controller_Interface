# Robotic_Controller_Interface
This interface is a basic controller that allows simple movement controls of the robots that are operated on the ROS system and take the robot's instant position.

# Issues

If the robot's location information (odom info) cannot be obtained when you press the "connect" button, this may be because the robot's "odom" and "cmd_vel" topics have different names. To fix this problem, look at the naming of these two topics with the "rostopic list" command and copy these two names, in the "script / robotic_controller.py" file,

    rospy.Subscriber ('odom', Odometry, self.odomInfo)
    pub = rospy.Publisher ('/ cmd_vel', Twist, queue_size = 1)

correct the lines with these topics.


# Maintainer
------------
Alim Kerem ERDOĞMUŞ
