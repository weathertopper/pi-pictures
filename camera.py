from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('~/temp-pics/picture.jpg')
camera.stop_preview()