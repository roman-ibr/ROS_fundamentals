#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse # import the service message python classes 

from scan_sub import getScan
from geometry_msgs.msg import Twist,Vector3
def my_callback(request):
    #print(Scan.ranges)
    my_response = TriggerResponse()
    
    right= Scan.ranges[125:135]
    front = Scan.ranges[355:365]
    left = Scan.ranges[525:535]

    my_response.success = True
      
    if min(left) < 0.7 and min(front) >= 1.0 :#  if min(left) < 0.7 and min(front) >= 1.0 :
        # If it's close to the wall, go forward
        # and keep closing to the wall
        my_response.message = "right" #Go_Right
        
        
    elif min(right) < 0.7 and min(front) >= 1.0 :
        # If it's close to the wall, go forward
        # and keep closing to the wall

        my_response.message = "left" 
        
    elif  min(front) < 0.8 :# hecne 0.3
        message = Twist(
        Vector3(-9.5, 0, 0),
        Vector3(0, 0, 0) )
        my_response.message = "Back"     
    elif min(left) < 0.50 : # 0.20 :
        # If the robot is very close to the wall,
        # only rotates to the other side
        message = Twist(
            Vector3(0, 0, 0),
            Vector3(0, 0, -0.25) )
        my_response.message = "Rotate_Right"
       
        
    elif min(right) < 0.50 :
        # If the robot is very close to the wall,
        # only rotates to the other side
        message = Twist(
            Vector3(0, 0, 0),
            Vector3(0, 0, 0.25))
        my_response.message = "Rotate_Left" 
        
        
    elif min(left) < 1.0 and min(front) < 1.3 :
        # If it's closing to the wall,
        # slows the velocity and rotate agressively
        message = Twist(
            Vector3(2.25, 0, 0),
            Vector3(0, 0, 1.65))
        my_response.message = "Turn_Right" 
        
        
    elif min(right) < 1.0 and min(front) < 1.3 :
        message = Twist(
        Vector3(1.25, 0, 0),
        Vector3(0, 0, 1.65))
        my_response.message = "Turn_Left"   #edited hecne yox idi

  
        
        
    else :
        # Move forward
        my_response.success = False

        my_response.message = "front"  
        
        
    #print(min(left),min(front),min(right))
    #rospy.loginfo("request")
    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse

rospy.init_node('service_server') 
my_service = rospy.Service('/crash_direction_service', Trigger , my_callback) # create the Service called my_service with the defined callback

#Odom = getOdom()
Scan = getScan()
rospy.spin() # maintain the service open.