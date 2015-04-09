#!/usr/bin/env python2

import dynamixel
import time

serial = dynamixel.SerialStream(port="/dev/ttyUSB0",
                                baudrate=1000000,
                                timeout=1)
net = dynamixel.DynamixelNetwork(serial)

actuator = dynamixel.Dynamixel(1, net)
net._dynamixel_map[1] = actuator
#actuator.cw_angle_limit = 0
#actuator.ccw_angle_limit = 0
actuator.moving_speed = 1024+800
actuator.torque_enable = True
actuator.torque_limit = 1023
actuator.max_torque = 1023
actuator.goal_position = 512
net.synchronize()

time.sleep(0.6)

while True:
    actuator.moving_speed = 800
    net.synchronize()
    time.sleep(0.6)

    actuator.moving_speed = 1024
    net.synchronize()
    time.sleep(4)

    actuator.moving_speed = 1024+800
    net.synchronize()
    time.sleep(0.6)

    actuator.moving_speed = 1024
    net.synchronize()
    time.sleep(4)



#while True:
#    print "Current speed: ", actuator.current_speed
#    time.sleep(0.5)
