#Button state
#Uitlezen wat de knop doet
from machine import Pin

button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())


#Met sleep time
from machine import Pin
from utime import sleep_ms

button = Pin(14, Pin.IN, Pin.PULL_UP)
print("button")
while True:
    if button.value() == 0:
        print("Button ingedrukt")
    else:
        print("Button niet ingedrukt")

    sleep_ms(200)