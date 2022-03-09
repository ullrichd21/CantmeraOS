# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
import board as board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont

# Import the SSD1306 module.
import adafruit_ssd1306

# init SPI
spi = busio.SPI(board.SCLK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
cs_pin = digitalio.DigitalInOut(board.D27)    # any pin!
dc_pin = digitalio.DigitalInOut(board.D22)    # any pin!



WIDTH = 128
HEIGHT = 32
BORDER = 5

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, dc_pin, reset_pin, cs_pin)

# Clear display.
oled.fill(0)
oled.show()
