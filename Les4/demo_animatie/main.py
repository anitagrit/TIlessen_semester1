import time
from machine import SPI, Pin
from max7219 import Matrix8x8

spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
screen = Matrix8x8(spi, Pin(5), 1)   # 1 = één LED matrix
screen.brightness(5)

# 1 = LED aan, 0 = LED uit
#Je kunt het patroon lezen als een tekening.
# Elke regel is een rij LEDs van boven naar beneden,
# en elke 1 is een LED die aan gaat. 8 rijen en 8 kolommen.
hart_groot = """
01100110
11111111
11111111
11111111
01111110
00111100
00011000
00000000
"""

hart_klein = """
00000000
00100100
01111110
01111110
00111100
00011000
00000000
00000000
"""


def toon_figuur(figuur, wachttijd):
    """Laat één figuur zien en wacht een aantal seconden."""
    screen.write_pattern(figuur)
    screen.show()
    time.sleep(wachttijd)


def kloppend_hart(snelheid=0.4):
    """Laat het hart één keer kloppen: groot, dan klein."""
    toon_figuur(hart_groot, snelheid)
    toon_figuur(hart_klein, snelheid)


# Animatie: een kloppend hart
while True:
    kloppend_hart()

# import time
# from machine import SPI, Pin
# from max7219 import Matrix8x8
#
# spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
# screen = Matrix8x8(spi, Pin(5), 1)   # 1 = één LED matrix
# screen.brightness(5)
#
# # 1 = LED aan, 0 = LED uit
# hart_groot = """
# 01100110
# 11111111
# 11111111
# 11111111
# 01111110
# 00111100
# 00011000
# 00000000
# """
#
# hart_klein = """
# 00000000
# 00100100
# 01111110
# 01111110
# 00111100
# 00011000
# 00000000
# 00000000
# """
#
# # Animatie: een kloppend hart
# while True:
#     screen.write_pattern(hart_groot)
#     screen.show()
#     time.sleep(0.4)
#
#     screen.write_pattern(hart_klein)
#     screen.show()
#     time.sleep(0.4)
