#!/usr/bin/env python
import rospy

from sensor_msgs.msg import Imu
from uuv_sensor_ros_plugins_msgs.msg import DVL
from sensor_msgs.msg import FluidPressure
from hydrus.msg import ControlSystemMsg

class ControlsSystemNode:
    # This class is to create the node and make the Subscriptions and Publishing the message

    def __init__(self):
        # This function initialize the node, message, publisher and subscriber

        hydrusMsg = ControlSystemMsg()  # making the custom message an object
        pub = rospy.Publisher('hydrus_custom_msg', ControlSystemMsg, queue_size = 10)  # publishing the new message
        self.angular_velocity = rospy.Subscriber('/rexrov2/imu', Imu, self.callback_angular_velocity)  # subscribing to Imu to get the angular velocity
        self.velocity = rospy.Subscriber('/rexrov2/dvl', DVL, self.callback_velocity)  # subscribing to DVL to get the velocity
        self.fluid_pressure = rospy.Subscriber('/rexrov2/fluid_pressure', FluidPressure, self.callback_fluid_pressure)  # subscribing to FluidPressure to get the fluid pressure


    def callback_angular_velocity(self, msg):
        # This callback function gets the angular velocity from the IMU

        self.hydrusMsg.angular_velocity = msg.angular_velocity  # getting the angular velocity in the custom message
        self.pub.publish(self.hydrusMsg)  # publishing custom message


    def callback_velocity(self, msg):
        # This callback function gets the velocity from the DVL

        self.hydrusMsg.velocity = msg.velocity  # getting the velocity in the custom message
        self.pub.publish(self.hydrusMsg)  # publishing custom message


    def callback_fluid_pressure(self, msg):
        # This callback function gets the fluid pressure from the FluidPressure

        self.hydrusMsg.fluid_pressure = msg.fluid_pressure  # getting the fluid pressure in the custom message
        self.pub.publish(self.hydrusMsg)  # publishing custom message


if __name__ == "__main__":
    rospy.init_node('controls_systems-node', anonymous = True)
    ControlsSystemNode = ControlsSystemNode()
    rospy.spin()