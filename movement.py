from wallaby import *
from math import pi
from utilities import *
import constants as c
import gyro as g



def get_bump_left(self):
    """Returns condition of left create bumper"""
    self._verify()
    return get_create_lbump


def get_bump_right(self):
    """Returns condition of right create bumper"""
    self._verify()
    return get_create_rbump


def get_black_right():
    #print("Black Right Cliff")
    return get_create_rcliff_amt() < 2200


def get_black_left():
    #print("Black Left Cliff")
    #print("Black Left Cliff")
    return get_create_lcliff_amt() < 2200

def get_left_front():
    return get_create_lfcliff_amt() < 2200


def get_right_front():
    return get_create_rfcliff_amt() < 2200


def black_left_or_right():
    return get_black_left() or get_black_right()


def drive_to_black_and_square_up(speed):
    g.drive_condition(black_left_or_right, speed, False)
    create_drive_direct(0, 0)
    msleep(500)
    lspeed = -speed
    rspeed = -speed
    while lspeed != 0 or rspeed != 0:
        if get_black_left():
            lspeed = 0
        if get_black_right():
            rspeed = 0
        create_drive_direct(lspeed, rspeed)
    msleep(100)

def drive_timed(left, right, time): #DRS forward is opposite of create forward
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)


def drive_condition(condition, speed):
    print("Driving for condition")
    speed = -speed
    create_drive_direct(speed, speed)
    while condition:
         pass
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


def driveTilBlackLCliffAndSquareUp(speed):
    if speed > 0:
        drive_condition(not black_left_or_right, speed)
        while not get_black_left() or not get_black_right():
            if get_black_left():
                g.turn_with_gyro(-speed, 0)
                print ("left")
            elif get_black_right():
                g.turn_with_gyro(0, -speed)
                print ("right")
            else:
                print ("None")
    else:
        drive_condition(black_left_or_right, speed)
        while not get_black_left() or not get_black_right():
            if get_black_left():
                g.turn_with_gyro(-speed, 0)
                print ("left")
            elif get_black_right():
                g.turn_with_gyro(0, -speed)
                print ("right")
            else:
                print ("None")
    print ("done!")
    create_drive_direct(0, 0)


def timedLineFollowLeftFront(speed, time):
    sec = seconds()
    while(seconds() - sec<time):
        if get_left_front():
            create_drive_direct(speed/10, speed)
        else:
            create_drive_direct(speed, speed/10)
        msleep(10)
    create_stop()


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

#####################################################





