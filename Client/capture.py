from picamera import PiCamera
from time import sleep

camera = PiCamera()

class Capture_info:
    fol = "/home/pi/Desktop/Code/pic/"
    ext = "0001"
    ftype = ".jpg"

def capture():
    path = Capture_info.fol + Capture_info.ext + Capture_info.ftype
    print(path)
    print(Capture_info.ext)
    camera.capture(path)
    ext = int(Capture_info.ext) +1
    print(len(str(ext)))
    Capture_info.ext = "0" * (4 - len(str(ext)))+ str(ext)
    sleep(0.2)
    

#camera.stop_preview()

