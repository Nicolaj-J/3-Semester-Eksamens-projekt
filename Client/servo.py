import RPi.GPIO as GPIO
import pigpio
import time
import capture

servo1 = 13
servo2 = 12

pwm1 = pigpio.pi()
pwm1.set_mode(servo1, pigpio.OUTPUT)
pwm1.set_PWM_frequency(servo1, 50)

pwm2 = pigpio.pi()
pwm2.set_mode(servo1, pigpio.OUTPUT)
pwm2.set_PWM_frequency(servo2, 50)


def up_down_cap():
    for i in range(2500, 2000, -150):
        print("Servo moving vertical", i)
        pwm1.set_servo_pulsewidth(servo1, i)
        capture.capture()
        
def left_right_cap():
    for i in range(750, 2500, 250):
        print("-" * 15)
        print("Servo moving horizontal", i)
        pwm2.set_servo_pulsewidth(servo2, i)
        up_down_cap()
        print("-" * 15)
        time.sleep(0.5)

def stop():
    print("stoping")
    p.stop()
    GPIO.cleanup()
    print("GPIO CLEANED UP")
    
