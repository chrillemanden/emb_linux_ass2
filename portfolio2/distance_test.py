
# Worksheet 6 - Measuring Distance

import time
from gpiozero import DistanceSensor

pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

print("Ultrasonic Measurement")

#da_distance = sensor.distance / 2.0 

try:
    # Repeat the next indented block forever
    while True:
        print("Distance: %.3f cm\n" % (sensor.distance*100))
        time.sleep(0.1)

# If you CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")


