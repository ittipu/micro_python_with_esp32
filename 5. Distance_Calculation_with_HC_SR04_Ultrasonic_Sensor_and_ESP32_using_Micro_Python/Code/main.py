# Micro-Python
# Distance Calculation With HCSR04 Ultrasonic Sensor and ESP32 using Micro-Python 
# Md. Kamruzzaman Tipu
# IoT Engineer, BRACNet Limited.
# it.ktipu@gmail.com, +8801715497977 (Whats app)
# youtube link https://www.youtube.com/channel/UC_Y7VIu1nsfXuUhJGLTRaog/videos

from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin = 5, echo_pin = 18, echo_timeout_us = 10000)

while True:
    distance = sensor.distance_cm()
    print("Distance: ", distance, 'cm')
    sleep(1)