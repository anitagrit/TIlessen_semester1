"""
Opdracht: Bouw een schakeling op waarbij een LED aan een GPIO pin is
aangesloten (vergeet de weerstand niet!)
Schrijf code die er voor zorgt dat de LED constant knippert -
hoe lang de LED aan/uit is mag je zelf kiezen
Verwerk deze functionaliteit nu in een functie waarbij je
aan de functie mee kunt geven welke LED er moet blinken
en hoe lang de LED aan en uit moet zijn.
"""
"""
Uitwerking: plaats jumper in GPIO 16
"""

#Een keer blink
print("een keer blink")
from machine import Pin
from utime import sleep_ms

led = Pin(16, Pin.OUT)

led.value(1)  # LED on
sleep_ms(1000)  # Wait 1s
led.value(0)  # LED off

#Elke seconde met while
from machine import Pin
from utime import sleep_ms
print("while loop")
led = Pin(16, Pin.OUT)

while True:
    led.value(1)      # LED aan
    sleep_ms(1000)    # 1 seconde wachten

    led.value(0)      # LED uit
    sleep_ms(1000)    # 1 seconde wachten

#Elke seconde met functie
from machine import Pin
from utime import sleep_ms
print("functie_LEDBlink")
def blink_led(led, tijd_aan, tijd_uit):
    led.value(1)          # LED aan
    sleep_ms(tijd_aan)    # Wachten
    led.value(0)          # LED uit
    sleep_ms(tijd_uit)    # Wachten

# LED op GPIO16
led = Pin(16, Pin.OUT)

while True:
    blink_led(led, 1000, 500)