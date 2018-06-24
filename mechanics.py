
import RPi.GPIO as GPIO
import time
import thread

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

gpioSelect = {"UP":5, "DOWN":5, "LEFT":3, "RIGHT":3}
dutyPercentageSelect = {"UP":2.5, "DOWN":12.5, "LEFT":12.5, "RIGHT":2.5}

def move(direction, amount):
    print "Moving ", direction, ", ", amount, "degrees"

    try:
        gpioPin = gpioSelect[direction]
        dutyPercentage = dutyPercentageSelect[direction]
        milliseconds = amount / 2
        if milliseconds % 20 == 0:
            milliseconds += 5
    except KeyError:
        print "Invalid direction parameter given"
    
    try:
       thread.start_new_thread( startMotor, (gpioPin, dutyPercentage, milliseconds, ) )

    except Exception as e:
        print(e)

def startMotor(gpioPin, dutyPercentage, milliseconds):
    p = GPIO.PWM(gpioPin,50)
    p.start(dutyPercentage)
    time.sleep(float(milliseconds)/float(1000))
    p.stop()
    time.sleep(1)

def moveToMiddle():
    p = GPIO.PWM(3,50)
    p2 = GPIO.PWM(5,50)
    p.start(7.5)
    p2.start(7.5)
    time.sleep(0.150)
    p.stop()
    p2.stop()
