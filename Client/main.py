import servo
import drive
import RPi.GPIO as GPIO
import pigpio
import time
from threading import Thread

pi = pigpio.pi()

class State:
    def __init__(self):
        self.running = False
    def off(self):
        self.running = False
    def on(self):
        self.running = True

s = State()

def interupt(gpio, level, tick): 
    print("Buttun pressed")
    if s.running == True: 
        print("Button press ignored, script running")
    else: 
        print("Running script")
        s.on()

def run():
    while True:
        if s.running == True:
            print("Running cature!")
            servo.left_right_cap()
            print("Capture finished!")
            time.sleep(5)
            s.off()
            drive.upload_files()
        else:
            print("wating for button")
            print("Running is: ", s.running)
            time.sleep(2)
            

cb1 = pi.callback(22, pigpio.RISING_EDGE, interupt)
thread = Thread(target = run)
thread.start()

while True: 
    #print("wating")
    #print("Running is: ", State.running)
    time.sleep(1)
