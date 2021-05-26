#! /usr/bin/env python

#===============================================================
#Name and Surname: Roman Ibrahimov
#Email address: ibrahir@purdue.edu
#Program Description: 
'''
This program is used to navigate a TurtleBot robot to an obstacle within one meter. 
The program uses PID controller which written on class. Depending on the distance, 
the robot's velocity is adgusted by the controller. 
References: 
https://en.wikipedia.org/wiki/PID_controller 
https://github.com/korfuri/ 
'''
#=================================================================


import rospy
from std_msgs.msg import Int32 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
import time
import math
import numpy as np

#this is the main PID class 
class PID:
    #here we are initializing all the parameters
    def __init__(self, Kp, Ki, Kd, origin_time=None):
        if origin_time is None:
            origin_time = time.time()

        self.Kp = Kp #proportional gain 
        self.Ki = Ki #integral gain
        self.Kd = Kd #derivative gain

        
        self.Cp = 0.0 #proportional correction 
        self.Ci = 0.0 #integral correction 
        self.Cd = 0.0 #derivative correctioni 

        self.previous_time = origin_time #setting up the time
        self.previous_error = 0.0


    #This function returns final controller value
    def Update(self, error, current_time=None):
        #calculating the time step for integral and derivative
        if current_time is None:
            current_time = time.time()
        dt = current_time - self.previous_time
        if dt <= 0.0:
            return 0
        de = error - self.previous_error

        self.Cp = error         #correction error for proportion term
        self.Ci += error * dt   #correction error for integral term
        self.Cd = de / dt       #correction term for derivative term 

        self.previous_time = current_time #setting up the time for the next iteration
        self.previous_error = error
        #In final, the function returns final PID value
        return (
            (self.Kp * self.Cp)    # proportional 
            +(self.Ki * self.Ci)  # integral 
            +(self.Kd * self.Cd)  # derivative 
        )

#### end ####
#this is the distance when the robot will stop; 1 meter from the wall
target = 1.0
#here we are calling PID class with PID terms 
my_pid = PID(1.18,  0.0001, 0.045) 

#velocity of the robot
v = Twist()
#distance left to the target position 
distance = Float32()
#the correction of PID controller 
correction = Float32()
def callback(msg):
    #current distance to the wall
    current = msg.ranges[360]
    #distance left to the desired position (1m to the wall)
    distance.data =msg.ranges[360]-1.0
    #error to the target 
    error = -(target - current)
    #here we feed back the error to get the corrected value 
    correction = my_pid.Update(error)
    #seeting in the corrected value into the system, which is forward velocity 
    v.linear.x = correction
    #keeping rotation zero
    v.angular.z = 0.0


#initializing the node 
rospy.init_node('topics_quiz_node')
#subscriber to read the laser sensor from the robot
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
#publisher to publish the corrected velocity
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
#publisher to publish the distance for the plotter
pub_2 = rospy.Publisher ('/distance', Float32, queue_size=10)
#update rate
rate= rospy.Rate(30)
v = Twist()
current = Float32()


while not rospy.is_shutdown():
    #publishing the corrected velocity into the robot
    pub.publish(v)
    #publishing the distance data 
    pub_2.publish(distance.data)

    rate.sleep()




