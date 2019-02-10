import constants as c
from wallaby import *


cpp = None

def init_utilities(icpp):
    global cpp
    cpp = icpp


def wait_for_button_blink():
    print "Press Button..."
    state = False
    while not right_button():
        if state:
            state = False
            cpp.set_led(state)
        else:
            state = True
            cpp.set_led(state)
        msleep(500)
    msleep(1)
    print "Pressed"
    msleep(1000)


def wait_for_button(force=False):
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Button..."
        while not right_button():
            pass
        msleep(1)
        print "Pressed"
        msleep(1000)


def wait_for_selection(force=False):
    seeding1= False
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Left Button for Seeding...\nPress Right Button for Head-to-Head"
        while not right_button():
            if left_button():
                seeding1 = True
                print "Pressed Left"
                msleep(1000)
                return seeding1
            pass
        msleep(1)
        print "Pressed Right"
        msleep(1000)
        return seeding1


def wait_4_light(ignore=False):
    if ignore:
        wait_for_button_blink()
        return
    while not calibrate(c.STARTLIGHT):
        pass
    _wait_4(c.STARTLIGHT)


def calibrate(port):
    print("Press LEFT button with light on")
    while not left_button():
        pass
    while left_button():
        pass
    lightOn = analog(port)
    print("On value =", lightOn)
    if lightOn > 1500:
        print("Bad calibration")
        return False
    msleep(1000)
    print("Press RIGHT button with light off")
    while not right_button():
        pass
    while right_button():
        pass
    lightOff = analog(port)
    print("Off value =", lightOff)
    if lightOff < 1500:
        print("Bad calibration")
        return False

    if (lightOff - lightOn) < 1000:
        print("Bad calibration")
        return False
    c.startLightThresh = (lightOff + lightOn) / 2
    print("Good calibration! ", c.startLightThresh)
    print('{} {} {}'.format(lightOff, lightOn, c.startLightThresh))
    return True


def _wait_4(port):
    print("waiting for light!! ")
    while analog(port) > c.startLightThresh:
        pass


def DEBUG(PrintTime=True):
    ao()
    msleep(100)
    if PrintTime:
        print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    disable_servos()
    exit(0)


def EXIT():
    ao()
    msleep(100)
    print 'Program finished!\nSeconds: ', seconds() - c.START_TIME
    exit(0)


def DEBUG_with_wait():
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    msleep(5000)
    DEBUG(False)


def moveServo(servo, endPos, speed=10):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if now > 2047:
        print("Servo setting too large ", servo)
    if now < 0:
        print("Servo setting too small ", servo)
    if now > endPos:
        speed = -speed
    for i in range(now, endPos, speed):
        set_servo_position(servo, i)
        msleep(10)
    set_servo_position(servo, endPos)
    msleep(10)


def getLinefollowvalues():
    create_connect()
    while 1:
        print ("The right front line follow sensor sees: ")
        print get_create_rfcliff_amt()



