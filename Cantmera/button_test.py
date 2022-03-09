from gpiozero import Button
from picamera import PiCamera
from signal import pause
from datetime import datetime


def take_photo():
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    # Camera warm-up time
    camera.capture(f'{formatted_time}.jpg')


camera = PiCamera()
camera.start_preview()

button = Button(5)

button.when_pressed = take_photo

pause()
