#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes 
from move_bb8 import MoveBB8 
# from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
                                                                                    # generated from MyCustomServiceMessage.srv.

# int32 duration    # The time (in seconds) during which BB-8 will keep moving in circles

# bool success      # Did it achieve it? 

"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the square
int32 repetitions    # The number of times BB-8 has to execute the square movement when the service is called
---
bool success         # Did it achieve it?
"""
def my_callback(request):
    movebb8_object = MoveBB8()

    repetitions_of_square = request.duration + 1
    for i in range(repetitions_of_square):
        # rospy.loginfo("Start Movement with side = "+str(new_side)+"Repetition = "+str(i))
        movebb8_object.move_square()
    rospy.loginfo("Finished service move_bb8_in_square that was called called")
    response = MyCustomServiceMessageResponse()
    response.success = True
    return response
    
rospy.init_node('bb8_custom_service_server') 
my_service = rospy.Service('/move_bb8_in_square_custom', MyCustomServiceMessage , my_callback) # create the Service called move_bb8_in_square with the defined callback
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin() # mantain the service open.