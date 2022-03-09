from signal import pause

from menu import Menu
from screen import Screen
from gpiozero import Button
import config as config
import os
import json
import graphic
from shutter import Shutter
from roll import Roll

def main():
    #Check if new roll
    if config.check_config_exists():
        print("Config Exists!")
        config.parse_config()
    else:
        print("No Config Found! Creating Config...")
        config.create_default_config()

    config.print_config()

    if not config.values["active"]:
        roll = Roll()
    else:
        print("Roll Active!")
        # config.print_config()
        shutter = Shutter()

    #if not new roll, load config and start shutterOS


if __name__ == "__main__":
    main()
