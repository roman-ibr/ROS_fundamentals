#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

class getOdom(object):
    def __init__(self):
        self.data = Odometry()
        sub = rospy.Subscriber('/odometry/filtered', Odometry, self.callback)
    def callback(self,msg):
        self.data = msg
    
 
 