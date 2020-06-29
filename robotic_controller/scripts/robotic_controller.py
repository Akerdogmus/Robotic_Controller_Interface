#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robotic_controller.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from PyQt5.QtWidgets import qApp, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

#import icons_rc

#SPEED CONSTANTS
MAX_X = 5
MAX_Y = 5
MIN_X = -5
MIN_Y = -5

##Qt Designer Generated UI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(990, 560))
        MainWindow.setMaximumSize(QtCore.QSize(990, 560))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.robot_cont_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.robot_cont_label.setFont(font)
        self.robot_cont_label.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_cont_label.setObjectName("robot_cont_label")
        self.horizontalLayout_5.addWidget(self.robot_cont_label)
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_label.setFont(font)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.horizontalLayout_5.addWidget(self.info_label)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftButon = QtWidgets.QPushButton(self.centralwidget)
        self.leftButon.setMinimumSize(QtCore.QSize(80, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftButon.setIcon(icon)
        self.leftButon.setObjectName("leftButon")
        self.horizontalLayout.addWidget(self.leftButon)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.upButon = QtWidgets.QPushButton(self.centralwidget)
        self.upButon.setMinimumSize(QtCore.QSize(80, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/up-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upButon.setIcon(icon1)
        self.upButon.setObjectName("upButon")
        self.verticalLayout.addWidget(self.upButon)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.stopButon = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/no-stopping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButon.setIcon(icon2)
        self.stopButon.setObjectName("stopButon")
        self.verticalLayout.addWidget(self.stopButon)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.downButon = QtWidgets.QPushButton(self.centralwidget)
        self.downButon.setMinimumSize(QtCore.QSize(80, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downButon.setIcon(icon3)
        self.downButon.setObjectName("downButon")
        self.verticalLayout.addWidget(self.downButon)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.rightButon = QtWidgets.QPushButton(self.centralwidget)
        self.rightButon.setMinimumSize(QtCore.QSize(80, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightButon.setIcon(icon4)
        self.rightButon.setObjectName("rightButon")
        self.horizontalLayout.addWidget(self.rightButon)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.infoText = QtWidgets.QTextBrowser(self.centralwidget)
        self.infoText.setMinimumSize(QtCore.QSize(400, 60))
        self.infoText.setMaximumSize(QtCore.QSize(400, 60))
        self.infoText.setObjectName("infoText")
        self.verticalLayout_4.addWidget(self.infoText)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setMinimumSize(QtCore.QSize(80, 0))
        self.connectButton.setMaximumSize(QtCore.QSize(100, 100))
        self.connectButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectButton.setIcon(icon5)
        self.connectButton.setCheckable(True)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_4.addWidget(self.connectButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.speed_info_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.speed_info_label.setFont(font)
        self.speed_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_info_label.setObjectName("speed_info_label")
        self.verticalLayout_4.addWidget(self.speed_info_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem15)
        self.l_speed_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_speed_label.setFont(font)
        self.l_speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_speed_label.setObjectName("l_speed_label")
        self.verticalLayout_2.addWidget(self.l_speed_label)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.l_speed_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_speed_lcd.sizePolicy().hasHeightForWidth())
        self.l_speed_lcd.setSizePolicy(sizePolicy)
        self.l_speed_lcd.setMinimumSize(QtCore.QSize(120, 30))
        self.l_speed_lcd.setMaximumSize(QtCore.QSize(120, 30))
        self.l_speed_lcd.setMode(QtWidgets.QLCDNumber.Dec)
        self.l_speed_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.l_speed_lcd.setObjectName("l_speed_lcd")
        self.verticalLayout_2.addWidget(self.l_speed_lcd)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem17)
        self.posx_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.posx_label.setFont(font)
        self.posx_label.setAlignment(QtCore.Qt.AlignCenter)
        self.posx_label.setObjectName("posx_label")
        self.verticalLayout_2.addWidget(self.posx_label)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.x_pos_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.x_pos_lcd.setMinimumSize(QtCore.QSize(120, 30))
        self.x_pos_lcd.setMaximumSize(QtCore.QSize(120, 30))
        self.x_pos_lcd.setObjectName("x_pos_lcd")
        self.verticalLayout_2.addWidget(self.x_pos_lcd)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem21)
        self.a_speed_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.a_speed_label.setFont(font)
        self.a_speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.a_speed_label.setObjectName("a_speed_label")
        self.verticalLayout_3.addWidget(self.a_speed_label)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem22)
        self.a_speed_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_speed_lcd.sizePolicy().hasHeightForWidth())
        self.a_speed_lcd.setSizePolicy(sizePolicy)
        self.a_speed_lcd.setMinimumSize(QtCore.QSize(120, 30))
        self.a_speed_lcd.setMaximumSize(QtCore.QSize(120, 30))
        self.a_speed_lcd.setMode(QtWidgets.QLCDNumber.Dec)
        self.a_speed_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.a_speed_lcd.setObjectName("a_speed_lcd")
        self.verticalLayout_3.addWidget(self.a_speed_lcd)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem23)
        self.posy_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.posy_label.setFont(font)
        self.posy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.posy_label.setObjectName("posy_label")
        self.verticalLayout_3.addWidget(self.posy_label)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem24)
        self.y_pos_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.y_pos_lcd.setMinimumSize(QtCore.QSize(120, 30))
        self.y_pos_lcd.setMaximumSize(QtCore.QSize(120, 30))
        self.y_pos_lcd.setObjectName("y_pos_lcd")
        self.verticalLayout_3.addWidget(self.y_pos_lcd)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem25)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.robot_pos_info_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.robot_pos_info_label.setFont(font)
        self.robot_pos_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.robot_pos_info_label.setObjectName("robot_pos_info_label")
        self.verticalLayout_4.addWidget(self.robot_pos_info_label)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem27)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem28 = QtWidgets.QSpacerItem(30, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem28)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon6)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon7)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROS Robotic Controller"))
        self.robot_cont_label.setText(_translate("MainWindow", "Robot Controller Panel"))
        self.info_label.setText(_translate("MainWindow", "Information Terminal"))
        self.leftButon.setText(_translate("MainWindow", "Left"))
        self.upButon.setText(_translate("MainWindow", "Up"))
        self.stopButon.setText(_translate("MainWindow", "Stop"))
        self.downButon.setText(_translate("MainWindow", "Down"))
        self.rightButon.setText(_translate("MainWindow", "Right"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.speed_info_label.setText(_translate("MainWindow", "Speed Information"))
        self.l_speed_label.setText(_translate("MainWindow", "Linear Speed"))
        self.posx_label.setText(_translate("MainWindow", "Position X"))
        self.a_speed_label.setText(_translate("MainWindow", "Angular Speed"))
        self.posy_label.setText(_translate("MainWindow", "Position Y"))
        self.robot_pos_info_label.setText(_translate("MainWindow", "Robot Position Information"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
    
        """
        -> Robotic Controller Functions Side : In this section, all the 
        buttons and functions in the interface are found.
        
        """    
        self.infoText.setText("Welcome to Robotic Controller Interface...")
        twist.angular.z = twist.linear.x = twist.linear.y = 0.0       
        self.leftButon.clicked.connect(self.left_button_sel)
        self.rightButon.clicked.connect(self.right_button_sel)
        self.upButon.clicked.connect(self.up_button_sel)
        self.downButon.clicked.connect(self.down_button_sel)
        self.stopButon.clicked.connect(self.stop_button_sel)
        self.connectButton.clicked.connect(self.connect_button_sel)
        self.actionQuit.triggered.connect(self.quitApp)
        self.actionAbout.triggered.connect(self.aboutApp)
        self.connectButton.clicked.connect(self.connection_robot)
    
        """
        -> connection_robot Function: The purpose of this function is to create 
        followers on the "ROS odom topic" to get instant location information 
        when the robot's command to receive location data comes via the 
        "Connect" button.
    
        """
    
    def connection_robot(self):
        rospy.Subscriber('odom', Odometry, self.odomInfo)  
        
   
    """
    -> odomInfo Function: The purpose of this function is to transfer the odom 
    data from the connection_robot function to the corresponding LCDs in the 
    interface.
    
    """    
    
    def odomInfo(self,msg):
        self.x_pos_lcd.display(msg.pose.pose.position.x)
        self.y_pos_lcd.display(msg.pose.pose.position.y)
    
    """
    -> connect_button_sel Function: The purpose of this function is to activate 
    the "publisher" node that will transmit the speed commands to the robot to 
    the "ROS cmd_vel topic" of the interface.
    
    """
    
    def connect_button_sel(self):
        
        pub = rospy.Publisher('/cmd_vel',Twist, queue_size=1)               
    
        return pub
    
    """
    -> Rotation Buttons' Functions: These functions enable the key controls 
    that control the movement of the robot and the instant speed of the robot 
    to be broadcast on the relevant LCD displays.
    
    """
    
    def left_button_sel(self):
        
        self.infoText.setText("Left Clicked..")
        
        if twist.linear.y == MAX_Y:
            pass
        else:
            
            twist.linear.y += 1.0
            twist.angular.z = 0.5
            
        self.l_speed_lcd.display(twist.linear.x)
        self.a_speed_lcd.display(twist.angular.z)
        pub = self.connect_button_sel()
        pub.publish(twist)
        print("Left")
        
    def right_button_sel(self):
        
        self.infoText.setText("Right Clicked..")
        if twist.linear.y == MIN_Y:
            pass
        else:
            twist.linear.y += -1.0
            twist.angular.z = -0.5
        
        self.l_speed_lcd.display(twist.linear.x)
        self.a_speed_lcd.display(twist.angular.z)
        pub = self.connect_button_sel()
        pub.publish(twist)
        print("Right")
        
    def up_button_sel(self):
        
        self.infoText.setText("Up Clicked..")
        
        if twist.linear.x == MAX_X:
            pass
        else:
            
            twist.linear.x += 1.0
        
        self.l_speed_lcd.display(twist.linear.x)
        self.a_speed_lcd.display(twist.angular.z)
        pub = self.connect_button_sel()
        pub.publish(twist)
        print("Up")

        
    def down_button_sel(self):
        
        self.infoText.setText("Down Clicked..")
        
        if twist.linear.x == MIN_X:
            pass
        else:
            
            twist.linear.x += -1.0
        
        self.l_speed_lcd.display(twist.linear.x)
        self.a_speed_lcd.display(twist.angular.z)
        pub = self.connect_button_sel()
        pub.publish(twist)
        print("Down")
        
    def stop_button_sel(self):
        
        self.infoText.setText("Stopped..")
        self.l_speed_lcd.display(0)
        self.a_speed_lcd.display(0)
        twist.angular.z = twist.linear.x = twist.linear.y = 0.0
        pub = self.connect_button_sel()
        pub.publish(twist)
        print("Stop")
   
    """
    -> Top Menubar Functions: These functions enable the "about" and "exit" 
    buttons in the top menubar.
    """     
    def quitApp(self):

        qApp.quit()
        
    def aboutApp(self):
        self.infoText.setText("Designed by A.K.E.\nFor more information, please contact akerdogmus@gmail.com.")
         
        
if __name__ == "__main__":
    import sys
    
    rospy.init_node('robotic_controller_node')
    
    twist = Twist()
    odom = Odometry()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

        
