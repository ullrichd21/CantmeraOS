from signal import pause

from screen import Screen
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from time import sleep
import config as config
import graphic


class Shutter:
    def __init__(self):
        self.camera = None
        self.init_camera()

        self.screen = Screen()

        self.button = Button(5, bounce_time=0.1)
        self.button.when_pressed = self.take_photo



        self.update_screen()
        pause()

    def init_camera(self):
        self.camera = PiCamera(resolution=(4056, 3040))
        # Set ISO to the desired value
        self.camera.iso = 100
        # Wait for the automatic gain control to settle
        sleep(2)
        # Now fix the values
        self.camera.shutter_speed = camera.exposure_speed
        self.camera.exposure_mode = 'off'
        g = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = g

    def take_photo(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(self.camera.capture(f"{dt_string}_{str(config.get_value('photos_taken'))}_capture.jpg"))
        config.update_value("photos_taken", 1, increment = True)
        self.update_screen()

    def update_screen(self):
        img = graphic.generate_image("Shutter", f"{str(config.values['photos_taken'])}/{str(config.values['roll_size'])}",
                                     highlighted=False, next=False)
        # print(f"{type(img)}: {str(img)}")
        self.screen.display(img)

