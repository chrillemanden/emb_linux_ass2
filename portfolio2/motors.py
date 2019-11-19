
# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

motorspeed = 0.3

motorforward = (motorspeed, motorspeed)
motorleft = (motorspeed, 0)
motorright = (0, motorspeed)





robot.value = motorforward

# Wait for 3  second
time.sleep(3)

robot.value = motorleft

time.sleep(3)

robot.value = motorright

time.sleep(3)

robot.backward()

time.sleep(3)


robot.stop()


