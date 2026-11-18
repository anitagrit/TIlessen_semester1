import time

from machine import SPI, Pin

from max7219 import Max7219
print("led matrix")
spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
screen = Max7219(8, 8, spi, Pin(5))

while True:
    for x in range(48, 122):
        screen.fill(0)
        screen.text(chr(x), 0, 0, 1)
        screen.show()
        time.sleep(1)
