# Micro-Python
# Blink Led with esp32 in 1s interval
# Md. Kamruzzaman Tipu
# IoT Engineer, BRACNet Limited.
# it.ktipu@gmail.com, +8801715497977 (Whats app)


from machine import Pin # import Pin from machine Module
from time import sleep

led = Pin(23, Pin.OUT) # connect the led pin to pin D23 of ESP32(30 pins esp32).
delay = 1   # set delay in seconds

while True: # infinity loop
    led.value(1) # 1 for led high
    sleep(delay) # delay for 1s, keep the led high upto 1s
    led.value(0) # 0 for led low
    sleep(delay) # delay 1s, keep the led low upto 1s