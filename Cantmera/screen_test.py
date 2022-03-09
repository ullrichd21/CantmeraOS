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

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Draw a white background
# draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Load default font.
font = ImageFont.truetype("Roboto-Thin.ttf", 15)

# Draw Some Text
text = "Can'tmera"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()
