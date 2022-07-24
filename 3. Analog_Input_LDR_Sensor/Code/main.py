# Micro-Python
# LDR value(analog) input
# Md. Kamruzzaman Tipu
# IoT Engineer, BRACNet Limited.
# it.ktipu@gmail.com, +8801715497977 (Whats app)


from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))

pot.atten(ADC.ATTN_11DB) # Full range: 3.3v

while True:
    pot_value = pot.read()
    print(pot_value)
    sleep(0.1)
