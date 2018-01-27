from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()
# camera.start_preview()
sleep(5)
camera.capture('picture.jpg')
# camera.stop_preview()