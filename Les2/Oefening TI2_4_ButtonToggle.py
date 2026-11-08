from machine import Pin
from utime import sleep_ms
print("buttontoggle")
button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(16, Pin.OUT)

led_state = False
last_button = 1

while True:
    current_button = button.value()
    if current_button == 0 and last_button == 1:
        led_state = not led_state
        if led_state:
            led.value(1)
        else:
            led.value(0)
    last_button = current_button
    sleep_ms(50)