from machine import Pin
print("buttoncopy")
button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(16, Pin.OUT)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)