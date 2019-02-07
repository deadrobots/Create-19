from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import gyro as g

colorOrder = []

burningMCLeft = True
burningSky = 0

def init():
    print("Starting init")
    enable_servos()
    print("Enabling my servos")
    p.cameraInit()
    p.camera_update()
    print("Camera Init")
    msleep(500)
    moveServo(c.skyArm, c.armHighSkyscraper)
    msleep(500)
    moveServo(c.skyClaw, c.clawOpen)
    msleep(500)
    moveServo(c.skyClaw, c.clawClosed)
    msleep(500)
    create_connect()
    print("Connecting create")
    g.rotate(-50, 150)
    msleep(500)
    g.rotate(50, 150)
    msleep(500)
    moveServo(c.skyArm, c.armDown)
    msleep(500)
    moveServo(c.skyClaw, c.clawOpen)
    wait_for_button()


def findBurningBuildings():
    #Function determines which skyscraper and which MC are burning
    global burningMCLeft
    global burningSky
    g.rotate(50, 200)
    msleep(500)
    burningMCLeft = p.findBurningMC()
    if burningMCLeft == True:
        print("doing code for left")
    else:
        print("doing code for right")
    msleep(500)
    g.rotate(-45, 200)
    msleep(500)
    burningSky = p.findBurningSky()
    if burningSky == 0:
        print("doing code for left")
    elif burningSky == 1:
        print("doing code for middle")
    else:
        print("doing code for right")
    #Do Bump to signal LEGO bot (not coded yet)

def grabWaterCube():
    #Create turns and grabs large water cube
    moveServo(c.skyArm, c.armVertical)
    msleep(300)
    g.rotate(160, 150)
    msleep(300)
    moveServo(c.skyArm, c.armDown)
    #driveTilBlackLCliffAndSquareUp(100)
    g.create_drive_timed(100, 2)
    msleep(1000)
    g.rotate(12, 150)
    msleep(1000)
    g.create_drive_timed(100, 1)
    moveServo(c.skyClaw, c.clawClosed)
    moveServo(c.skyArm, c.armLowSkyscraper)
    DEBUG()
    msleep(500)
    #g.create_drive_timed(100, 1.5)
    msleep(500)
    cpp.rotate(20, 100)
    msleep(500)
    g.create_drive_timed(50, 1)
    msleep(500)
    moveServo(c.skyClaw, c.clawClosed)
    print("Grab water cube")
    DEBUG()
    msleep(1000)
    cpp.rotate(-8, 50)
    msleep(500)
    cpp.drive_distance(-18.5, 50)
    msleep(500)

def dropWaterCube():
    #Create deposits large water cube on burning building
    cpp.rotate(-94, 50)
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(50)
    msleep(3000)
    #Uses previous test to determine which building is on fire
    print(burningSky)
    #Drives towards burning building
    if burningSky == 0:
        print("Left")
        cpp.rotate(60, 20)
        cpp.drive_distance(12, 50)
        cpp.rotate(-60, 20)
    elif burningSky == 1:
        print("Middle")
        cpp.drive_distance(8, 50)
    else:
        print("Right")
        cpp.rotate(-60, 20)
        cpp.drive_distance(12, 50)
        cpp.rotate(60, 20)

#Proposed strategy, but might change
def grabFirstSkyCube():
    pass
def grabSecondSkyCube():
    pass
def connectElectricalLines():
    pass