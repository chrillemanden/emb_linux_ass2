
#Return one measurement from the sensor

import time
from gpiozero import DistanceSensor

pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

print("%.3f" % (sensor.distance*100))







