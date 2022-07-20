from machine import Pin, PWM
from time import sleep

frequency = 1000
led = PWM(Pin(23), frequency)
brightness = 0
delayTime = 0.01

while True:
    print(brightness)
    led.duty(brightness)
    brightness = brightness + 5
    
    if (brightness >= 1023):
        for i in range(brightness):
            brightness = brightness - 5
            led.duty(brightness)
            print(brightness)
            sleep(delayTime)
            if (brightness <= 0):
                break
    sleep(delayTime)
