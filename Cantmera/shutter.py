import io
import os.path
from time import sleep

from PIL import Image
# import matplotlib.image as mpimg
from picamera import PiCamera

import config as config
import graphic


class Shutter:
    def __init__(self):
        self.screen_status = False
        self.camera = None
        self.stream = None
        self.finished = False
        self.init_camera()

        self.screen = None

        self.update_screen()

    def handle_input(self, button):
        if button == "pressed":
            self.take_photo()
        elif button == "held":
            print("No function.")

    def init_camera(self):
        self.camera = PiCamera(resolution=(4056, 3040))
        # Set ISO to the desired value
        self.camera.iso = 200
        # Wait for the automatic gain control to settle
        sleep(2)
        # Now fix the values
        self.camera.shutter_speed = self.camera.exposure_speed
        self.camera.exposure_mode = 'auto'

        if not os.path.exists("/home/pi/photos"):
            os.mkdir("/home/pi/photos")

    def take_photo(self):
        if config.values['photos_taken'] >= config.values['roll_size']:
            self.finished = True
            return

        self.stream = io.BytesIO()
        file_name = f"{str(config.get_value('photos_taken'))}_capture.jpg"
        self.camera.capture(self.stream, format="jpeg")

        config.update_value("photos_taken", 1, increment=True)
        self.update_screen()

        self.stream.seek(0)

        if config.get_value("BW"):
            self.convert_to_grayscale(file_name)
        else:
            Image.open(self.stream).save(f"/home/pi/photos/{file_name}")
            self.stream.close()

    def convert_to_grayscale(self, photo_name):
        img = Image.open(self.stream).convert('L')
        img.save(f"/home/pi/photos/{photo_name}")
        self.stream.close()

        # img = mpimg.imread(f"./photos/{photo_name}")
        # R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        # imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B  # Convert all channels to grayscale.
        # mpimg.imsave(f"./photos/{photo_name}", imgGray, cmap='gray')

    def get_roll_status(self):
        return self.finished

    def get_screen_status(self):
        return self.screen_status

    def get_screen(self):
        self.screen_status = False
        return self.screen

    def update_screen(self):
        self.screen_status = True
        img = graphic.generate_image("Shutter",
                                     f"{str(config.values['photos_taken'])}/{str(config.values['roll_size'])}",
                                     highlighted=False, next=False)
        # print(f"{type(img)}: {str(img)}")
        self.screen = img
