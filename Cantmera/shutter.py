from signal import pause

from screen import Screen
from gpiozero import Button
import config as config
import graphic


class Shutter:
    def __init__(self):
        self.screen = Screen()

        self.button = Button(5, bounce_time=0.1)
        self.button.when_pressed = self.take_photo

        self.update_screen()
        pause()



    def take_photo(self):
        print("Photo!")
        config.update_value("photos_taken", 1, increment = True)
        self.update_screen()

    def update_screen(self):
        img = graphic.generate_image("Shutter", f"{str(config.values['photos_taken'])}/{str(config.values['roll_size'])}",
                                     highlighted=False, next=False)
        # print(f"{type(img)}: {str(img)}")
        self.screen.display(img)

