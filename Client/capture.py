from picamera import PiCamera
from time import sleep

camera = PiCamera()

class capture_info:
    fol = "/home/pi/Desktop/Code/pic/"
#camera.start_preview()
    ext = "0001"
    ftype = ".jpg"

def capture():
    path = capture_info.fol + capture_info.ext + capture_info.ftype
    print(path)
    print(capture_info.ext)
    camera.capture(path)
    ext = int(capture_info.ext) +1
    print(len(str(ext)))
    capture_info.ext = "0" * (4 - len(str(ext)))+ str(ext)
    sleep(0.5)
    

#camera.stop_preview()

