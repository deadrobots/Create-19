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
    #SETUP
    #Arm pointing away from MCs
    #Edges of create line up with the black tape
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
    msleep(300)
    moveServo(c.skyArm, c.armDown)
    #driveTilBlackLCliffAndSquareUp(100)
    g.create_drive_timed(100, 2)
    msleep(1000)
    g.rotate(12.5, 150)
    msleep(1000)
    g.create_drive_timed(100, 1.5)
    moveServo(c.skyClaw, c.clawClosed)
    moveServo(c.skyArm, c.armVertical)
    msleep(1000)
    g.create_drive_timed(-100, 1.5)
    msleep(500)


def dropWaterCube():
    #Create deposits large water cube on burning building
    g.rotate(-12.5, 150)
    msleep(500)
    g.create_drive_timed(-200, 2)
    msleep(500)
    g.rotate(90, 150)
    msleep(500)
    wait_for_button()
    g.create_drive_timed(-200, 2)
    msleep(1000)
    #Next Step:
    #Edit this code below so that the create pauses as a certain location where it can reach all three skyscrapers
    #From here, based on which building is burning, place block there
    #Code below is framework
    if burningSky == 0:
        print("Left")
        g.rotate(60, 100)
        g.create_drive_timed(-100, 3)
        g.rotate(-60, 100)
    elif burningSky == 1:
        print("Middle")
        g.create_drive_timed(-100, 2.5)
    else:
        print("Right")
        g.rotate(-60, 100)
        g.create_drive_timed(-100, 3)
        g.rotate(60, 100)
    #After this is successful, fill function below that picks up the Mayor and Botguy and places them in the startbox
    #You shouldn't have to move the robot at all because the arm is long enough to reach the start box

#Proposed strategy
def grabFirstSkyCube():
    pass
def grabSecondSkyCube():
    pass
def connectElectricalLines():
    pass