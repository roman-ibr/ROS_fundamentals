#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
# from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest # Import the service message used by the service /gazebo/delete_model
import sys
import rospkg

# # Initialise a ROS node with the name service_client
# rospy.init_node('service_execute_trajectory_client') #service_execute_trajectory_client
# # Wait for the service client /trajectory_by_name to be running
# rospy.wait_for_service('/trajectory_by_name')
# # Create the connection to the service
# exec_traj_client = rospy.ServiceProxy('/trajectory_by_name', ExecTraj)
# # Create an object of type TrajByNameRequest
# execute_trajectory_request_object = ExecTrajRequest()


# rospack = rospkg.RosPack()
# # This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
# traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"



# # Fill the variable traj_name of this object with the desired value
# execute_trajectory_request_object.file = traj
# # Send through the connection the name of the trajectory to be executed by the robot
# result = exec_traj_client(execute_trajectory_request_object)
# # Print the result given by the service called
# print(result)

rospy.init_node('service_execute_trajectory_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/execute_trajectory') # Wait for the service client /execute_trajectory to be running
execute_trajectory_service_client = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Create the connection to the service
execute_trajectory_request_object = ExecTrajRequest() # Create an object of type ExecTrajRequest

rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.<br>
trajectory_file_path = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"


execute_trajectory_request_object.file = trajectory_file_path
result = execute_trajectory_service_client(execute_trajectory_request_object) # Send through the connection the path to the trajectory file to be executed
print (result) # Print the result type ExecTrajResponse