# Micro-Python
# Control LED with HCSR04 Ultrasonic Sensor and ESP32 using Micro-Python 
# Md. Kamruzzaman Tipu
# IoT Engineer, BRACNet Limited.
# it.ktipu@gmail.com, +8801715497977 (Whats app)
# youtube link https://www.youtube.com/channel/UC_Y7VIu1nsfXuUhJGLTRaog/videos

from hcsr04 import HCSR04
from time import sleep
from machine import Pin

sensor = HCSR04(trigger_pin = 5, echo_pin = 18, echo_timeout_us = 10000)
led = Pin(22, Pin.OUT)

while True:
    distance = sensor.distance_cm()
    print("Distance: ", distance, 'cm')
    if distance <= 15:
        led.value(1)
        print("Warning!!!Object is too close")
        print("LED ON")
    else:
        led.value(0)
    sleep(0.5)