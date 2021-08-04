#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import cv2
import random
import time

def nothing(x):
	pass

def talker():
    cv2.namedWindow('controls', 1)
    cv2.createTrackbar('Joint1', 'controls', -100, 100, nothing)
    cv2.createTrackbar('Joint2', 'controls', -100, 100, nothing)
    
    pub1 = rospy.Publisher('/mrm/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/mrm/joint2_position_controller/command', Float64, queue_size=10)
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.5) # 0.5hz -> 2sec

    while not rospy.is_shutdown():
        msg1 = cv2.getTrackbarPos('Joint1', 'controls')*3.14/100
        msg2 = cv2.getTrackbarPos('Joint2', 'controls')*0.81/100

        print("Printing",  cv2.getTrackbarPos('Joint2', 'controls'))
        rospy.loginfo(str(msg1) + " " + str(msg2))
        pub1.publish(msg1)
        pub2.publish(msg2)
        rate.sleep()

    cv2.waitKey(1)
    cv2.destroyAllWindows()
   
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass