# Micro-Python
# Control LED With LDR Sensor 
# Md. Kamruzzaman Tipu
# IoT Engineer, BRACNet Limited.
# it.ktipu@gmail.com, +8801715497977 (Whats app)


from machine import Pin, ADC
from time import sleep
thresholdValue = 400 # Set the threshold value for led turn on


pot = ADC(Pin(34)) # Connect the LDR pin to D34 of ESP32
led = Pin(22, Pin.OUT) # Connect the LED pin to D22 of ESP32

pot.atten(ADC.ATTN_11DB) # Full range: 3.3v

while True:
    pot_value = pot.read()
    print("The value of light/ldr: {}".format(pot_value))
    
    if pot_value < thresholdValue:
        print("Light value below threshold!!Turning light ON")
        led.value(1)
    else:
        led.value(0)
    sleep(0.1)
