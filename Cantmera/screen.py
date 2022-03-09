#!/usr/bin/env python

import board as board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont

# Import the SSD1306 module.
import adafruit_ssd1306
import time
import threading

class Screen():
    def __init__(self):

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
        self.oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, dc_pin, reset_pin, cs_pin)

        self.clear()
        self.oled.show()

    def display(self, image):
        self.clear()
        self.oled.image(image)
        self.oled.show()

    def clear(self):
        # Clear display.
        self.oled.fill(0)
        self.oled.show()

    # if __name__ == "__main__":
    #     main()
