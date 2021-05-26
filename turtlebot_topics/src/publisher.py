#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
from geometry_msgs.msg import Twist
# from std_msgs.msg import Float32
###new code
from sensor_msgs.msg import LaserScan
###
# def callback(msg): 
#     print (msg.ranges[360])

# ###
# rospy.init_node('laser_subscriber')
# ###
# sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

# # rospy.init_node('topic_publisher')
# # pub = rospy.Publisher('/counter', Int32, queue_size = 1)
# # pub_2 = rospy.Publisher('/counter_2', String, queue_size = 10)
# pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3 )
# rate = rospy.Rate(2000)
# count = Int32()
# count.data=0

# var = Twist()
# var.linear.x = 0.3
# var.angular.z =1

# while not rospy.is_shutdown():
#     # pub_2.publish("Hi there")
#     # rate.sleep()
#     # pub.publish(count)
#     # count.data +=1
#     pub.publish(var)
#     rate.sleep()
v = Twist()
def callback(msg):
    print(msg.ranges[360])
    if msg.ranges[360]>1:
        v.linear.x = 0.2
        v.angular.z = 0
    #left
    elif msg.ranges[360]<1 or msg.ranges[0]<1:
        v.linear.x = 0.2
        v.angular.z = -0.5
    #right
    elif msg.ranges[0] <1:
        v.linear.x = 0.2
        v.angular.z = 0.5
    # v.angular.z = 0

rospy.init_node('publisher')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
rate= rospy.Rate(1)
v = Twist()



while not rospy.is_shutdown():
    pub.publish(v)
    rate.sleep()