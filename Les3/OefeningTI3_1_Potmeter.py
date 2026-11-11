# Elektronica - Potentiometer Demo
# je krijgt verschillende waardes zonder de potmeter aan te raken
# Omdat de ADC in de RP2040 is niet perfect.  Er zit altijd
# wat elektrische ruis op de meting.

print("potmeter")
from machine import Pin, ADC
from utime import sleep_ms

# Define the ADC GPIO pin for the potentiometer
POT_PIN = 26

# Initialize the ADC
adc = ADC(Pin(POT_PIN))

while True:
    val = adc.read_u16()
    print(val)
    sleep_ms(1000)
