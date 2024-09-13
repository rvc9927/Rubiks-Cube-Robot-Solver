from time import sleep
import RPi.GPIO as GPIO


DIR1 = 20   # Direction GPIO Pin1
STEP1 = 21  # Step GPIO Pin1
RESET1 = 2 # Reset Motor 1
DIR2 = 16   # Direction GPIO Pin2
STEP2 = 19  # Step GPIO Pin1
RESET2 = 13 # Reset Motor 2
CW = 0     # Clockwise Rotation
CCW = 1    # Counterclockwise Rotation
SPR = 400   # Steps per Revolution ((360 / 1.5)*2 [using extra set of coils])
Revolutions = .25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.setup(RESET1, GPIO.OUT)
GPIO.setup(RESET2, GPIO.OUT)


MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['1/32'])

rot_amount = int(SPR * Revolutions)
delay = .0208 / 64

GPIO.output(RESET1, GPIO.HIGH)
for x in range(rot_amount):
    GPIO.output(STEP1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    sleep(delay)
GPIO.output(RESET1, GPIO.LOW)

sleep(1)

GPIO.output(RESET2, GPIO.HIGH)
GPIO.output(DIR2, CW)
for x in range(rot_amount):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
GPIO.output(RESET2, GPIO.LOW)

sleep(1)

GPIO.output(RESET1, GPIO.HIGH)
GPIO.output(DIR1, CCW)
for x in range(rot_amount):
    GPIO.output(STEP1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    sleep(delay)
GPIO.output(RESET1, GPIO.LOW)

sleep(1)

GPIO.output(RESET2, GPIO.HIGH)
GPIO.output(DIR2, CCW)
for x in range(rot_amount):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
GPIO.output(RESET2, GPIO.LOW)


