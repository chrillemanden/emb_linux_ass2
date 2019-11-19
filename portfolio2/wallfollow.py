
# Keep same distance to wall

import time
from gpiozero import DistanceSensor
from gpiozero import CamJamKitRobot

pinTrigger = 17
pinEcho = 18

wallDistance = 40 # cm
maxDiff = 5

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

motorspeed = 0.3

motorforward = (motorspeed, motorspeed)
motorbackward = (-motorspeed, -motorspeed)
motorleft = (motorspeed, 0)
motorright = (0, motorspeed)

try:
    while True:
        time.sleep(0.1)
        dist = sensor.distance * 100
        print("Distance: %.3f cm\n" % dist)
        if dist > (wallDistance + maxDiff):
            robot.value = motorright
        elif dist < (wallDistance - maxDiff):
            robot.value = motorleft
        else:
            robot.value = motorforward


except KeyboardInterrupt:
    print("Exiting")


