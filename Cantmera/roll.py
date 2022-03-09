class Roll:
    def __init__(self):

        self.held = False

        self.screen = Screen()
        self.i = 0
        self.menus = [
            Menu("Roll Size").add_option("5", lambda: print("Selected 5!"))
                     .add_option("15", lambda: print("Selected 15!"))
                     .add_option("30", lambda: print("Selected 30!")),
            Menu("B/W?").add_option("Yes", lambda: print("Selected Yes!")).add_option("No", lambda: print("Selected No!"))
        ]

        self.button = Button(5, bounce_time=0.1)
        self.button.when_held = self.set_held
        self.button.when_released = self.compute_input

        self.update_screen()
        pause()

    def set_held(self):
        self.held = True

    def compute_input(self):
        # print(self.button.active_time)
        if self.held != True:
            self.next()
        else:
            self.do_action()

        self.held = False

    def next(self):
        if self.menus[self.i].has_next_option():
            self.menus[self.i].next_option()
        self.update_screen()

    def do_action(self):
        print("Hello!")
        self.i = (self.i + 1) % len(self.menus)
        self.update_screen()

    def update_screen(self):
        curr_menu = self.menus[self.i]
        opt = curr_menu.get_current_selection()
        img = graphic.generate_image(curr_menu.title, opt.title,
                                     highlighted=opt.selected, next=curr_menu.has_next_option())
        self.screen.display(img)