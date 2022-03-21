import json
import os

values = {
    'roll_size': -1,
    'BW': False,
    'photos_taken': 0,
    'active': False
}

unsaved_changes = False


def check_config_exists():
    return os.path.exists("/home/pi/config.json")


def create_default_config():
    global values

    conf = {
        'roll_size': -1,
        'BW': False,
        'photos_taken': 0,
        'active': False
    }

    values = conf

    with open("/home/pi/config.json", "w") as out:
        json.dump(conf, out)

    save_config()


def parse_config():
    with open("/home/pi/config.json", "r") as conf:
        dic = json.load(conf)

        global values
        values = dic

    photo_num = values["photos_taken"]
    photos_found = check_photo_num()

    if photo_num != photos_found:
        update_value("photos_taken", photos_found)


def check_photo_num():
    return len(os.listdir("/home/pi/photos/"))


def update_value(var, val, increment=False, save_now=False):
    global values, unsaved_changes

    if increment:
        values[var] += val
    else:
        values[var] = val

    if save_now:
        unsaved_changes = False
        save_config()
    else:
        unsaved_changes = True

    if not increment:
        print(f"{var} was updated to {val}")
    else:
        print(f"{var} was incremented to {values[var]}")


def get_unsaved_changes():
    return unsaved_changes


def get_value(var):
    global values
    return values[var]


def save_config():
    global values

    with open("./config.json", "w") as out:
        json.dump(values, out)


def print_config():
    global values
    print(values)
