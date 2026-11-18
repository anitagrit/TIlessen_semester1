# Elektronica - Keypad
from machine import Pin, ADC
from utime import sleep_ms
# Bij mij de waarden:
# midden: 47803
# links:  192
# boven:  9426
# onder:  21349
# rechts: 32615

# Define the ADC GPIO pin for the 5-button keypad
KEYPAD_PIN = 26  # Adjust this pin number as needed

# Initialize the ADC
adc = ADC(Pin(KEYPAD_PIN))
#### met if statements
def read_keypad():
    # Read the ADC value
    adc_value = adc.read_u16()  # Read the ADC value (0-65535)
    print(adc_value)

    # Map the ADC value to a key
    adc_value = adc.read_u16()
    print(adc_value)
    # marge van ongeveer 1000
    if adc_value < 1000:
        return "Links"
    elif 8500 <= adc_value <= 10500:
        return "Boven"
    elif 20000 <= adc_value <= 22500:
        return "Onder"
    elif 31500 <= adc_value <= 34000:
        return "Rechts"
    elif 46500 <= adc_value <= 49000:
        return "Midden"
    else:
        return "Geen knop"

def main():
    print("Start van de keypad")

    while True:
        key = read_keypad()
        print(f"{key} ingedrukt")
        sleep_ms(500)  # Wait half a second before reading again

if __name__ == "__main__":
    main()
####### met dictonary mooier omdat je dan makkelijk kunt aanpassen en toevoegen
buttons = {
    "Links": 192,
    "Boven": 9426,
    "Onder": 21349,
    "Rechts": 32615,
    "Midden": 47803
}

def read_keypad():

    adc_value = adc.read_u16()
    closest_button = None
    smallest_difference = 65535

    for button, value in buttons.items():
        difference = abs(adc_value - value)
        if difference < smallest_difference:
            smallest_difference = difference
            closest_button = button
    if smallest_difference < 1500:
        return closest_button
    return "Geen knop"