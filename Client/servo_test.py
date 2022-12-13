import RPi.GPIO as GPIO
import pigpio
import time

servo = 13

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency(servo, 50)

print("0 deg")
pwm.set_servo_pulsewidth(servo, 2500)
