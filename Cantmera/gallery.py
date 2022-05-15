import os.path
from io import BytesIO
from time import sleep

from PIL import Image
from picamera import PiCamera

import config as config
import graphic
from graphic import generate_image


class Gallery:
    def __init__(self, screen=None):
        self.screen_status = False
        self.camera = None
        self.stream = None
        self.finished = False
        self.init_camera()
        self.screen_obj = screen

        self.screen = None

        self.update_screen()
        self.photos_taken = 0
        self.photo_taken = False

    def handle_input(self, button):
        if button == "pressed":
            self.take_photo()
        elif button == "held":
            print("No function.")

    def init_camera(self):
        self.camera = PiCamera(resolution=(4056, 3040), sensor_mode=0, framerate=12)
        self.camera.start_preview()
        # Wait for the automatic gain control to settle
        sleep(2)

        # Now fix the values
        # self.camera.meter_mode = "average"
        # self.camera.shutter_speed = self.camera.exposure_speed
        # self.camera.exposure_mode = 'off'
        # self.camera.exposure_compensation = 0

        if not os.path.exists("/home/pi/photos"):
            os.mkdir("/home/pi/photos")

    def take_photo(self):
        print(f"Shutter Speed: {self.camera.exposure_speed}")
        self.stream = BytesIO()
        self.photos_taken += 1
        self.photo_taken = True
        file_name = f"{str(self.photos_taken)}_capture.jpg"
        self.camera.capture(self.stream, format="jpeg")

        # self.stream.seek(0)

        print("Finishing photo...")

        if config.get_value("BW"):
            print("Converting to BW...")
            if self.screen_obj is not None:
                self.screen_obj.display(generate_image("", "Converting to BW...", highlighted=True))
            self.convert_to_grayscale(file_name)
        else:
            Image.open(self.stream).save(f"/home/pi/photos/{file_name}")
            self.stream.close()

        print("Taking Photo")

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

    def new_photo_taken(self):
        if self.photo_taken:
            self.photo_taken = False
            return True

        return False

    def output_values(self):
        # print(f"===============\nExposure Speed: {self.camera.exposure_speed}\nShutter Speed: {self.camera.shutter_speed}")
        pass
