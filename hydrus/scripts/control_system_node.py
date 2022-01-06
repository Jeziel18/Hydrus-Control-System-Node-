#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from uuv_sensor_ros_plugins_msgs.msg import DVL
from sensor_msgs.msg import FluidPressure
from hydrus.msg import ControlSystemMsg

class ControlsSystemNode:
    def __init__(self):
        
        hydrusMsg = ControlSystemMsg()
        pub = rospy.Publisher('hydrus_custom_msg', ControlSystemMsg, queue_size = 10)
        self.angular_velocity = rospy.Subscriber('/rexrov2/imu', Imu, self.callback_angular_velocity)
        self.velocity = rospy.Subscriber('/rexrov2/dvl', DVL, self.callback_velocity)
        self.fluid_pressure = rospy.Subscriber('/rexrov2/fluid_pressure', FluidPressure, self.callback_fluid_pressure)
        
    def callback_angular_velocity(self, msg):
        self.hydrusMsg.angular_velocity = msg.angular_velocity
        self.pub.publish(self.hydrusMsg)

    def callback_velocity(self, msg):
        self.hydrusMsg.velocity = msg.velocity
        self.pub.publish(self.hydrusMsg)

    def callback_fluid_pressure(self, msg):
        self.hydrusMsg.fluid_pressure = msg.fluid_pressure
        self.pub.publish(self.hydrusMsg)


if __name__ == "__main__":
    rospy.init_node('controls_systems-node', anonymous = True)
    ControlsSystemNode = ControlsSystemNode()
    rospy.spin()