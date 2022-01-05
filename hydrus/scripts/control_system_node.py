#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from uuv_sensor_ros_plugins_msgs.msg import DVL
from sensor_msgs.msg import FluidPressure
from hydrus.msg import ControlSystemMsg

class ControlsSystemNode:
    def __init__(self):
        pub = rospy.Publisher('hydrus_custom_msg', ControlSystemMsg, queue_size = 10)
        hydrusMsg = ControlSystemMsg()
        self.angular_velocity = rospy.Subscriber('/rexrov2/imu', Imu, self.callback_angular_velocity)
        self.velocity = rospy.Subscriber('/rexrov2/dvl', DVL, self.callback_velocity)
        self.fluid_pressure = rospy.Subscriber('/rexrov2/fluid_pressure', FluidPressure, self.callback_fluid_pressure)

    def callback_angular_velocity(self, msg):
        hydrusMsg.angular_velocity = msg.angular_velocity


    def callback_velocity(self, msg):
        hydrusMsg.velocity = msg.velocity

    def callback_fluid_pressure(self, msg):
        hydrusMsg.fluid_pressure = msg.fluid_pressure

    pub.publish(hydrusMsg)

if __name__ == "__main__":
    rospy.init.node('controls_systems-node', anonymous = True)
    ControlsSystemNode = ControlsSystemNode()
    rospy.spin()