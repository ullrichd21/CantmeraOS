import json
import os

values = {
    'roll_size': -1,
    'BW': False,
    'photos_taken': 0,
    'active': False
}


def check_config_exists():
    return os.path.exists("./config.json")


def create_default_config():
    conf = {
        'roll_size': -1,
        'BW': False,
        'photos_taken': 0,
        'active': False
    }

    with open("./config.json", "w") as out:
        json.dump(conf, out)


def parse_config():
    with open("./config.json", "r") as conf:
        dic = json.load(conf)

        global values
        values = dic


def update_value(var, val, increment=False):
    global values

    if increment:
        values[var] += val
    else:
        values[var] = val

    save_config()


def save_config():
    global values

    with open("./config.json", "w") as out:
        json.dump(values, out)


def print_config():
    global values
    print(values)
