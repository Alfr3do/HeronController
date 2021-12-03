#!/usr/bin/env python
# Software License Agreement (BSD License)
#

import rospy
from std_msgs.msg import  Header, Bool
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped

class SimpleController:

    def __init__(self):
	print('Initializing this');
        self_rate = rospy.Rate(10) #10hz
	self.thruster_0_on = rospy.Publisher("/heron/thrusters/0/is_on", Bool, queue_size=1)
	self.thruster_0 = rospy.Publisher("/heron/thrusters/0/input",FloatStamped, queue_size=10)
	self.thruster_1_on = rospy.Publisher("/heron/thrusters/1/is_on",Bool, queue_size=1)
	self.thruster_1 = rospy.Publisher("/heron/thrusters/1/input",FloatStamped, queue_size=10)

	self.thruster_0_on.publish(Bool(True))
	self.thruster_1_on.publish(Bool(True))

	self.timer = rospy.Timer(rospy.Duration(3.0/10.0), self.sendCommand)
	print(self.timer)
	cmd = FloatStamped(Header(), 5000)
	self.thruster_0.publish(cmd)
	self.thruster_1.publish(cmd)
   
    def __del__(self):
	self.thruster_0_on.unregister()
	self.thruster_1_on.unregister()
	self.thruster_0.unregister()
	self.thruster_1.unregister()
        self.timer.shutdown()

    def sendCommand(self, event):
        print('Calling')
	cmd = FloatStamped(Header(), 500)
	self.thruster_0.publish(cmd)
	self.thruster_1.publish(cmd)


if __name__ == '__main__':
    rospy.init_node('heron_controller')
    try:
        node = SimpleController()
        rospy.spin()
    except rospy.ROSInterruptException:
        print('caught exception')
    print('exiting')
