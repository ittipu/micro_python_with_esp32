import machine
from machine import Pin
from time import sleep

led = Pin(12, Pin.OUT)

print("LED ON")
led.value(1)
sleep(1)
print("LED_OFF")
led.value(0)
sleep(1)


sleep(5)

print('Task Complete. Going to deepsleep Mode')
machine.deepsleep(10000)
