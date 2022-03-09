from time import sleep
from picamera import PiCamera
from datetime import datetime

def iso(n_iso):
    camera.iso = n_iso

def shutter_speed(n_shutter_speed):
    camera.shutter_speed = n_shutter_speed

def main():
    camera = PiCamera(resolution=(4056, 3040))
    # Set ISO to the desired value
    camera.iso = 100
    # Wait for the automatic gain control to settle
    sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g

    while True:
        print("Press ENTER to take a photo. Type \"i\" to change the ISO or \"s\" to change the shutter speed")

        inp = input()

        if inp == "":
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            camera.capture(dt_string + "_capture.jpg")
        elif inp == "i":
            i = int(input("New ISO: "))
            iso(i)
        elif inp == "s":
            s = int(input("New Shutter Speed: "))
            shutter_speed(s)
if __name__ == "__main__":
    main()
# Finally, take several photos with the fixed settings
camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
