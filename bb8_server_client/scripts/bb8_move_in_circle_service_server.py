#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from move_bb8 import MoveBB8
# import bb8_move_circle_class

def my_callback(request):
    rospy.loginfo("Hi, the service has been called")
    move_robot = MoveBB8()
    move_robot.move_square()
    # print("My_callback has been called")
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 
rospy.init_node('bb8_service_server') 
my_service = rospy.Service('/move_bb8_in_square', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.

