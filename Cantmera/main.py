import datetime as dt

from gpiozero import Button

import config
import twitter
from roll import Roll
from screen import Screen
from shutter import Shutter

held = False
setup = False
last_input = ""
time_idle = dt.datetime.now()


def main():
    global setup, held, time_idle

    button = Button(5, bounce_time=0.1)
    button.when_held = set_held
    button.when_released = compute_input

    # Check if new roll
    if config.check_config_exists():
        print("Config Exists!")
        config.parse_config()
    else:
        print("No Config Found! Creating Config...")
        config.create_default_config()

    config.print_config()
    screen = Screen()
    shutter = None
    roll = None

    if not config.values["active"]:
        setup = True
    else:
        shutter = Shutter()

    while True:
        if setup:
            if roll is None:
                roll = Roll()
            roll.handle_input(give_input())

            if roll.get_setup_status():
                if shutter is None:
                    shutter = Shutter()
                setup = False

            if roll.get_screen_status():
                img = roll.get_screen()
                print(img)
                screen.display(img)

        else:
            shutter.handle_input(give_input())

            if shutter.get_roll_status():
                screen.display(twitter.get_tweet_screen())
                success = twitter.tweet_all_photos()
                if success:
                    config.create_default_config()
                    setup = True

            if shutter.get_screen_status():
                screen.display(shutter.get_screen())

        if (dt.datetime.now() - time_idle).seconds > 10:
            if config.get_unsaved_changes():
                print("IDLE")
                time_idle = dt.datetime.now()
                config.save_config()
    # if not new roll, load config and start shutterOS


def set_held():
    global held
    held = True


def give_input():
    global last_input
    val = last_input
    last_input = ""
    return val


def compute_input():
    global held, last_input, time_idle

    if not held:
        last_input = "pressed"
    else:
        last_input = "held"

    held = False
    time_idle = dt.datetime.now()


if __name__ == "__main__":
    main()
