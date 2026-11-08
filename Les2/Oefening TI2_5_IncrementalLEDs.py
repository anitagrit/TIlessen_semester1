from machine import Pin
from utime import sleep_ms
print("incrementalLEDs")
button = Pin(14, Pin.IN, Pin.PULL_UP)

leds = [
    Pin(16, Pin.OUT),  # 1
    Pin(17, Pin.OUT),  # 2
    Pin(18, Pin.OUT),  # 4
    Pin(19, Pin.OUT)   # 8
]

count = 0
last_button = 1

while True:

    current_button = button.value()

    if current_button == 0 and last_button == 1:

        count += 1

        if count > 15:
            count = 0

        for i in range(4):
            leds[i].value((count >> i) & 1)

    last_button = current_button

    sleep_ms(50)