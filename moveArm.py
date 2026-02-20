import smbus
import time 
import numpy as np
from Arm_Lib import Arm_Device
000

Arm = Arm_Device()
#put delays 
#time.sleep(1)

#function that allows you to send the degree of rotation for all of the motors: 

Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 500) #moved it completely straight
time.sleep(1)

def move_arm_to_position(positions, time):
    Arm.Arm_serial_servo_write6(*positions, time)

 move_arm_to_position((0, 0, 0, 0, 0, 0), 500)
 time.sleep(1)

 move_arm_to_position((90, 0, 0, 0, 0, 0,), 500)

 #move it to the right
 move_arm_to_position((135, 90, 90, 90, 90, 90),500)

 #maybe move straight 
 move_arm_to_position((90, 90, 90, 90, 90, 90),500)


#testing various positions

#move_arm_to_position((0, 0, 0, 0, 0, 0), 500)
#time.sleep(1)
#move_arm_to_position((0,45 ,90 ,135 ,180 ,90 ), 500)
#time.sleep(1)
#move_arm_to_position((180, 135, 90, 45, 0, 90), 500)
#time.sleep(1)
# def move_arm_to_position(positions, time):
#     Arm.Arm_serial_servo_write6(*positions, time)
#
# #testing various positions
#
# move_arm_to_position((0, 0, 0, 0, 0, 0), 500)
# time.sleep(1)
# move_arm_to_position((0,45 ,90 ,135 ,180 ,90 ), 500)
# time.sleep(1)
# move_arm_to_position((180, 135, 90, 45, 0, 90), 500)
# time.sleep(1)
#
# #to move it left
# move_arm_to_position((45, 90, 90, 90, 90, 90),500)
#
# #move it to the right
# move_arm_to_position((135, 90, 90, 90, 90, 90),500)
#
# #maybe move straight 
# move_arm_to_position((90, 90, 90, 90, 90, 90),500)
#
#def move_arm (direction):
#    if direction == "left":
#        move_arm_to_position((45, 90, 90, 90, 90, 90),500)
#
