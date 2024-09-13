#Algorithms
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DIR_F = 20  # Direction Front Motor
STEP_F = 21  # Step Front Motor
RESET_F = 2  # Reset Front Motor
DIR_R = 16  # Direction Right Motor
STEP_R = 19  # Step Right Motor
RESET_R = 13  # Reset Right Motor
DIR_L = 3
STEP_L = 17
RESET_L = 12
DIR_BACK = 10
STEP_BACK = 22
RESET_BACK = 27
DIR_T = 5
STEP_T = 11
RESET_T = 9
DIR_BOT = 7
STEP_BOT = 8
RESET_BOT = 25

# THESE SHOULD ALL BE GOOD

cw = 0  # Clockwise Rotation
ccw = 1  # Counterclockwise Rotation
SPR = 200*8  # Steps per Revolution ((360 / 1.8)*2 [using extra set of coils])
Revolutions = .25

MODE = (14, 15, 18)  # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 1, 1)}
GPIO.output(MODE, RESOLUTION['1/8'])

rot_amount = int(SPR * Revolutions)
delay = .0001
delay2 = delay/2
wait = 0.001  #time to wait after waking up before step move
wait2 = 0.0
wait3 = 0.0

GPIO.setup(DIR_F, GPIO.OUT)
GPIO.setup(STEP_F, GPIO.OUT)
GPIO.setup(RESET_F, GPIO.OUT)

GPIO.setup(DIR_R, GPIO.OUT)
GPIO.setup(STEP_R, GPIO.OUT)
GPIO.setup(RESET_R, GPIO.OUT)

GPIO.setup(DIR_L, GPIO.OUT)
GPIO.setup(STEP_L, GPIO.OUT)
GPIO.setup(RESET_L, GPIO.OUT)

GPIO.setup(DIR_BACK, GPIO.OUT)
GPIO.setup(STEP_BACK, GPIO.OUT)
GPIO.setup(RESET_BACK, GPIO.OUT)

GPIO.setup(DIR_T, GPIO.OUT)
GPIO.setup(STEP_T, GPIO.OUT)
GPIO.setup(RESET_T, GPIO.OUT)

GPIO.setup(DIR_BOT, GPIO.OUT)
GPIO.setup(STEP_BOT, GPIO.OUT)
GPIO.setup(RESET_BOT, GPIO.OUT)

#class HWmoves():
#   def __int__():

def Front_cw():
    GPIO.output(RESET_F, GPIO.LOW)
    GPIO.output(DIR_F, cw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_F, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_F, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_F, GPIO.HIGH)
    sleep(wait3)

def Front_ccw():
    GPIO.output(RESET_F, GPIO.LOW)
    GPIO.output(DIR_F, ccw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_F, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_F, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_F, GPIO.HIGH)
    sleep(wait3)

def Right_cw():
    GPIO.output(RESET_R, GPIO.LOW)
    GPIO.output(DIR_R, cw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_R, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_R, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_R, GPIO.HIGH)
    sleep(wait3)

def Right_ccw():
    GPIO.output(RESET_R, GPIO.LOW)
    GPIO.output(DIR_R, ccw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_R, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_R, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_R, GPIO.HIGH)
    sleep(wait3)

def Left_cw():
    GPIO.output(RESET_L, GPIO.LOW)
    GPIO.output(DIR_L, cw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_L, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_L, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_L, GPIO.HIGH)
    sleep(wait3)

def Left_ccw():
    GPIO.output(RESET_L, GPIO.LOW)
    GPIO.output(DIR_L, ccw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_L, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_L, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_L, GPIO.HIGH)
    sleep(wait3)

def Back_cw():
    GPIO.output(RESET_BACK, GPIO.LOW)
    GPIO.output(DIR_BACK, cw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_BACK, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_BACK, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_BACK, GPIO.HIGH)
    sleep(wait3)

def Back_ccw():
    GPIO.output(RESET_BACK, GPIO.LOW)
    GPIO.output(DIR_BACK, ccw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_BACK, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_BACK, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_BACK, GPIO.HIGH)
    sleep(wait3)


def Top_cw():
    GPIO.output(RESET_T, GPIO.LOW)
    GPIO.output(DIR_T, cw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_T, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_T, GPIO.LOW)
        sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_T, GPIO.HIGH)
    sleep(wait3)

def Top_ccw():
    GPIO.output(RESET_T, GPIO.LOW)
    GPIO.output(DIR_T, ccw)
    sleep(wait)
    for x in range(rot_amount):
        GPIO.output(STEP_T, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP_T, GPIO.LOW)
        sleep(delay2)
    GPIO.output(RESET_T, GPIO.HIGH)
    sleep(wait3)

def Bottom_cw():
    GPIO.output(RESET_BOT, GPIO.LOW)
    GPIO.output(DIR_BOT, cw)
    sleep(wait)
    for x in range(rot_amount):
         GPIO.output(STEP_BOT, GPIO.HIGH)
         sleep(delay)
         GPIO.output(STEP_BOT, GPIO.LOW)
         sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_BOT, GPIO.HIGH)
    sleep(wait3)

def Bottom_ccw():
    GPIO.output(RESET_BOT, GPIO.LOW)
    GPIO.output(DIR_BOT, ccw)
    sleep(wait)
    for x in range(rot_amount):
         GPIO.output(STEP_BOT, GPIO.HIGH)
         sleep(delay)
         GPIO.output(STEP_BOT, GPIO.LOW)
         sleep(delay2)
    sleep(wait2)
    GPIO.output(RESET_BOT, GPIO.HIGH)
    sleep(wait3)




"""
Back_cw()
Back_cw()
Back_ccw()
Back_ccw()
Back_cw()
Back_cw()
Back_cw()
Back_ccw()
Back_ccw()
Back_cw()
Back_ccw()
Back_ccw()

Left_cw()
Left_cw()
Left_ccw()
Left_ccw()


Top_cw()
Top_ccw()
Top_ccw()
Top_cw()
Back_ccw()
Back_ccw()

Left_cw()
Left_cw()
Top_ccw()
Top_cw()
Top_cw()
Back_ccw()
Back_ccw()

Left_cw()
Left_cw()
Top_cw()
Top_ccw()
Top_ccw()
Top_ccw()
"""
"""
Front_cw()
Right_cw()
Back_cw()
Left_cw()
Top_cw()
Bottom_cw()
"""
GPIO.output(RESET_BACK, GPIO.HIGH)
GPIO.output(RESET_BOT, GPIO.HIGH)
GPIO.output(RESET_T, GPIO.HIGH)
GPIO.output(RESET_F, GPIO.HIGH)
GPIO.output(RESET_R, GPIO.HIGH)
GPIO.output(RESET_L, GPIO.HIGH)
#GPIO.output(RESET_F, GPIO.HIGH)

"""
Bottom_cw()
Bottom_ccw()
Bottom_ccw()"""