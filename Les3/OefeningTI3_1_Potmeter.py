# Elektronica - Potentiometer Demo
# je krijgt verschillende waardes zonder de potmeter aan te raken
# Omdat de ADC in de RP2040 is niet perfect.  Er zit altijd
# wat elektrische ruis op de meting.

# Bij een potentiometer op GPIO26 meet de ADC een
# spanning tussen 0 V en 3,3 V. Die spanning wordt
# door de RP2040 omgezet naar een waarde
# tussen 0 en 65535.

# Helemaal links	0 V	0
# 25%	            0,825 V	±16384
# Midden	        1,65 V	±32768
# 75%	            2,475 V	±49152
# Helemaal rechts	3,3 V	65535

from machine import Pin, ADC
from utime import sleep_ms

print("potmeter")
def lees_potmeter(pin_nummer):
    adc = ADC(Pin(pin_nummer))

    while True:
        waarde = adc.read_u16()
        print(waarde)
        sleep_ms(1000)


print("Potmeter")

# Start de functie op GPIO26
lees_potmeter(26)
