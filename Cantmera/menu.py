from option import Option


class Menu:

    def __init__(self, title):
        self.title = title
        self.options = []
        self.selection = 0

    def next_option(self):
        # for o in self.options:
        #     print(o.title)
        # print(self.options)
        print(f"sel: {self.selection} | new: {(self.selection + 1) % len(self.options)}")
        self.selection = (self.selection + 1) % len(self.options)
        # print(self.selection)

    def get_current_selection(self):
        return self.options[self.selection]

    def add_option(self, option, action):
        self.options.append(Option(option, action))
        return self

    def get_remaining_options(self):
        return self.selection - len(self.options)

    def has_next_option(self):
        # if self.selection < len(self.options) - 1:
        #     print(f"{self.selection}, {len(self.options)}")
        #     return True
        # return False
        if len(self.options) > 1:
            return True
        return False

    def do_action(self):
        return self.options[self.selection].action