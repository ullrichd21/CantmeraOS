from menu import Menu

from functools import partial

import config as config
import graphic


class Roll:
    def __init__(self):
        self.setup_complete = False
        self.held = False
        self.screen_status = False  # True if the screen has changed
        self.screen = None
        self.i = 0
        self.menus = [
            Menu("Roll Size").add_option("5", partial(config.update_value, "roll_size", 5))
                .add_option("15", partial(config.update_value, "roll_size", 15))
                .add_option("30", partial(config.update_value, "roll_size", 30)),
            Menu("B/W?").add_option("Yes", partial(config.update_value, "BW", True)).add_option("No", partial(
                config.update_value, "BW", False))
        ]

        self.update_screen()

    def handle_input(self, button):
        if button == "pressed":
            self.next()
        elif button == "held":
            self.do_action()

    def next(self):
        if self.menus[self.i].has_next_option():
            self.menus[self.i].next_option()
        self.update_screen()

    def do_action(self):
        self.menus[self.i].do_action()
        # self.i = (self.i + 1) % len(self.menus)
        if self.i == len(self.menus) - 1:
            config.update_value("active", True, save_now=True)
            self.setup_complete = True
            return
        else:
            self.i += 1
        self.update_screen()

    def get_screen_status(self):
        return self.screen_status

    def get_screen(self):
        self.screen_status = False
        return self.screen

    def update_screen(self):
        self.screen_status = True
        curr_menu = self.menus[self.i]
        opt = curr_menu.get_current_selection()
        img = graphic.generate_image(curr_menu.title, opt.title,
                                     highlighted=opt.selected, next=curr_menu.has_next_option())
        self.screen = img

    def get_setup_status(self):
        return self.setup_complete
