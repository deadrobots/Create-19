from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import gyro as g
import movement as m

colorOrder = []

burningMCLeft = True
burningSky = 0

def turnCalibration():
    g.rotate(180, 100)
    msleep(500)
    DEBUG()

def init():
    #SETUP
    #Arm pointing away from MCs
    #Edges of create line up with the black tape intersection
    #Align square up surface with left side of middle bump
    #   This should ensure that the robot is pointing directly towards the middle bump (DRS forward)
    print("Starting init")
    enable_servos()
    print("Enabling my servos")
    p.cameraInit()
    p.camera_update()
    print("Camera Init")
    msleep(500)
    moveServo(c.skyArm, c.armVertical)
    msleep(500)
    moveServo(c.skyClaw, c.clawOpen)
    msleep(500)
    moveServo(c.skyClaw, c.clawClosed)
    msleep(500)
    create_connect()
    create_full()
    #turnCalibration()
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
    moveServo(c.skyArm, c.armVertical)
    g.rotate(50, 100)
    msleep(500)
    burningMCLeft = p.findBurningMC()
    if burningMCLeft == True:
        print("doing code for left")
    else:
        print("doing code for right")
    msleep(500)
    g.rotate(-45, 100)
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
    g.rotate(175, 150)
    msleep(500)
    moveServo(c.skyArm, c.armDown)
    #driveTilBlackLCliffAndSquareUp(100)
    m.drive_to_black_and_square_up(75)
    msleep(500)
    g.create_drive_timed(-100, 1)
    msleep(500)
    g.rotate(13, 150)
    msleep(500)
    g.create_drive_timed(100, 2)
    moveServo(c.skyClaw, c.clawClosed)
    moveServo(c.skyArm, c.armVertical)
    msleep(300)
    g.create_drive_timed(-100, 1.5)
    msleep(300)


def dropWaterCube():
    #Create deposits large water cube on burning building
    g.rotate(-13, 150)
    msleep(300)
    g.create_drive_timed(-200, 1.8)
    msleep(300)
    g.rotate(90, 150)
    msleep(3000)
    g.create_drive_timed(-200, 3)
    msleep(300)
    m.drive_to_black_and_square_up(75)
    g.create_pivot_on_right_wheel(50, 7)
    if burningSky == 0:
        print("Left")
        g.rotate(40, 100)
        moveServo(c.skyArm, c.armLowSkyscraper, 5)
    elif burningSky == 1:
        print("Middle")
        moveServo(c.skyArm, c.armHighSkyscraperDeliver, 5)
        moveServo(c.skyClaw, c.clawOpen, 5)
    else:

        print("Right")
        g.rotate(-40, 100)
        moveServo(c.skyArm, c.armLowSkyscraper, 5)
    #After this is successful, fill function below that picks up the Mayor and Botguy and places them in the startbox
    #You shouldn't have to move the robot at all because the arm is long enough to reach the start box

#Proposed strategy
def grabFirstSkyCube():
    pass
def grabSecondSkyCube():
    pass
def connectElectricalLines():
    pass