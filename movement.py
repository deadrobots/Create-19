
from wallaby import *
from math import pi
from utilities import *
import constants as c
import createPlusPlus as cpp

cpp = None


def init_movement(icpp):
    global cpp
    cpp = icpp


def drive_timed(left, right, time): #DRS forward is opposite of create forward
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)


def spin_cw(power, time):
    create_drive_direct(power, -power)
    msleep(time)
    create_drive_direct(0, 0)


def spin_ccw(power, time):
    create_drive_direct(-power, power)
    msleep(time)
    create_drive_direct(0, 0)


def rotate(power, time):
    if power > 0:
        spin_ccw(power, time)
    else:
        spin_cw(abs(power), time)

def rotateTillBlack(power):
    if power > 0:
        create_drive_direct(-power, power)
    else:
        create_drive_direct(power, -power)
    while (get_create_rfcliff_amt() > 2000):
        pass
    create_stop()

def drive_forever(left, right):
    create_drive_direct(-right, -left)


def stop():
    create_stop()


INCH_TO_MIL = 25.4

def drive_distance2(distance, speed):
    if distance < 0:
        speed = -speed
    dist_mil = INCH_TO_MIL * distance
    time = (int)((dist_mil / speed) * 1000)
    drive_timed(speed, speed, time)


def rotate_degrees(degrees, speed):
    if degrees < 0:
        speed = -speed
        degrees = abs(degrees)
    degrees = degrees * 1.13
    set_create_total_angle(0)
    drive_forever(-speed, speed)
    while abs(get_create_total_angle()) < degrees:
        pass
    stop()

def black_left_or_right():
    return cpp.get_black_left() or cpp.get_black_right()

def driveTilBlackLCliffAndSquareUp(speed):
    if speed > 0:
        cpp.drive_conditional(black_left_or_right, speed, False)
        while not cpp.get_black_left() or not cpp.get_black_right():
            if cpp.get_black_left():
                cpp.drive(-speed, 0)
                print ("left")
            elif cpp.get_black_right():
                cpp.drive(0, -speed)
                print ("right")
            else:
                print ("None")
    else:
        cpp.drive_conditional(black_left_or_right, speed, False)
        while not cpp.get_black_left() or not cpp.get_black_right():
            if cpp.get_black_left():
                cpp.drive(-speed, 0)
                print ("left")
            elif cpp.get_black_right():
                cpp.drive(0, -speed)
                print ("right")
            else:
                print ("None")
    print ("done!")
    cpp.drive(0, 0)


def driveTilFrontTophatBlack(lspeed, rspeed):
    lspeed = -lspeed
    rspeed = -rspeed
    create_drive_direct(rspeed, lspeed)
    while (analog(c.FRONT_TOPHAT) < 2000):
        pass
    create_stop()

def timedLineFollowLeftFront(speed, time):
    sec = seconds()
    while(seconds() - sec<time):
        if cpp.get_black_left():
            cpp.drive(speed/2, speed)
        else:
            cpp.drive(speed, speed/2)
    cpp.drive(0, 0)

def timedLineFollowFrontTophat(time):
    sec = seconds()
    while(seconds() - sec<time):
        if analog(c.FRONT_TOPHAT) < 1500:
            create_drive_direct(-100, -50)
        else:
            create_drive_direct(-50, -100)
    create_stop()

def timedLineFollowRightFront(speed, time):
    sec = seconds()
    while(seconds() - sec<time):
        if get_create_rfcliff_amt() < 2000:
            create_drive_direct(speed, (int)(speed/1.8))
        else:
            create_drive_direct((int)(speed/1.8), speed)
        msleep(10)
    create_stop()

def lineFollowLeftFrontTilRightFrontBlack(speed):
    while cpp.get_black_front_right():
        if not cpp.get_black_front_left():
            cpp.drive(speed, speed / 2)
        else:
            cpp.drive(speed / 2, speed)
    cpp.drive(0, 0)


def lineFollowRightFrontTilLeftFrontBlack(speed):
    while cpp.get_black_front_left():
        if not cpp.get_black_front_right():
            cpp.drive(speed / 2, speed)
        else:
            cpp.drive(speed, speed / 2)
    cpp.drive(0, 0)

def turnTilRightFrontBlack(left, right):
    create_drive_direct(left, right)
    while (get_create_rfcliff_amt() > 2000):
        pass
    create_stop()
