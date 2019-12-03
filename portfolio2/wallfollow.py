
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

motorspeed = 0.7

motorforward = (-motorspeed, -motorspeed)
motorbackward = (motorspeed, motorspeed)
motorleft = (-motorspeed, -0.8*motorspeed)
motorright = (-0.8*motorspeed, -motorspeed)

try:
    while True:
        time.sleep(0.05)
        dist = sensor.distance * 100
        print("Distance: %.3f cm\n" % dist)
        if dist > (wallDistance + maxDiff):
            motorspeed = 0.5
            motorrigt = (-0.8*motorspeed, -motorspeed)
            robot.value = motorright
            #motorspeed = 0.5
        elif dist < (wallDistance - maxDiff):
            motorspeed = 0.5
            motorleft = (-motorspeed, -0.8*motorspeed)
            robot.value = motorleft
            #motorspeed = 0.5
        else:
            motorspeed = 0.7
            robot.value = motorforward
except KeyboardInterrupt:
    print("Exiting")


