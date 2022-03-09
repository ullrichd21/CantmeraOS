import json
import os


def get_file_from_path(path):
    if os.path.exists(path):
        return open(path)
    return None


def get_network_details(path):
    file = get_file_from_path(path)
    lines = file.readlines()
    return lines


def connect_to_network(name, password, interface):
    try:
        os.system(f"nmcli d wifi connect {name} password {password} iface {interface}")
    except:
        raise Exception(f"Couldn't connect to network {name} with {interface}")
    else:
        return True


def change_network():
    interface = "Some default" #This needs to be changed.
    # Find drive.
    path = "./test.txt"  # This needs to be changed to the default path of USB drives...

    network = get_network_details(path)

    connect_to_network(network[0], network[1], interface)
