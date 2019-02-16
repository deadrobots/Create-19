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
    if c.IS_PRIME:
        print("I am prime")
    if c.IS_CLONE:
        print("I am clone")
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
    moveServo(c.skyClaw, c.clawClosedWater)
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
    msleep(500)
    moveServo(c.electricalArm, c.electricArmDown, 10)
    wait_for_button()


def findBurningBuildings():
    #Function determines which skyscraper and which MC are burning
    global burningMCLeft
    global burningSky
    moveServo(c.skyArm, c.armVertical)
    if c.IS_PRIME:
        g.rotate(50, 100)
    elif c.IS_CLONE:
        g.rotate(55, 100)
    msleep(500)
    burningMCLeft = p.findBurningMC()
    if burningMCLeft == True:
        print("doing code for left")
    else:
        print("doing code for right")
    msleep(500)
    if c.IS_PRIME:
        g.rotate(-45, 100)
    elif c.IS_CLONE:
        g.rotate(-55, 100)
    msleep(900)
    burningSky = p.findBurningSky()
    if burningSky == 0:
        print("doing code for left")
    elif burningSky == 1:
        print("doing code for middle")
    else:
        print("doing code for right")
    #Do Bump to signal LEGO bot (not coded yet)

def grabBotMayor():
    print("Grabbing the botMayor")
    m.drive_to_black_and_square_up(-75)
    msleep(500)
    g.create_drive_timed(150, 1.6)
    g.rotate(-90, 100)
    msleep(500)
    g.create_drive_timed(200, 3.3)
    msleep(100)
    m.drive_to_black_and_square_up(-75)
    if burningSky == 0 or burningSky == 2:
        msleep(500)
        #g.rotate(2.5, 50)
        msleep(500)
        g.create_drive_timed(50, 3.3)
        msleep(500)
        moveServo(c.skyArm, c.mayorArm, 5)
        msleep(100)
        moveServo(c.skyClaw, c.clawClosedMayor, 5)
        msleep(800)
        moveServo(c.skyArm, c.armVertical, 5)
        msleep(500)
        m.drive_to_black_and_square_up(-100)
        msleep(500)
        g.create_drive_timed(-175, 1)
        msleep(500)
        m.drive_to_black_and_square_up(-100)
        msleep(500)
        g.rotate(180, 125)
        moveServo(c.skyArm, c.armDown, 10)
        msleep(100)
        moveServo(c.skyClaw, c.clawOpen, 20)
        msleep(100)
        if burningSky == 0:
            moveServo(c.skyArm, c.armVertical, 10)
            msleep(500)
            g.rotate(180, 125)
            msleep(500)
            g.create_drive_timed(200, 2.3)
            msleep(100)
            m.drive_to_black_and_square_up(-75)
            msleep(500)
            g.rotate(-35, 100)
            msleep(500)
            g.create_drive_timed(50, 2.2)
            msleep(100)
            moveServo(c.skyArm, c.armLowGrab, 10)
            msleep(100)
            moveServo(c.skyClaw, c.clawClosedMayor, 10)
            msleep(100)
            moveServo(c.skyArm, c.armVertical, 10)
            msleep(250)
            g.create_drive_timed(-50, 2.2)
            msleep(500)
            g.rotate(35, 100)
            msleep(500)
            g.create_drive_timed(-175, 1)
            msleep(500)
            m.drive_to_black_and_square_up(-100)
            msleep(500)
            g.rotate(180, 125)
            moveServo(c.skyArm, c.armDown, 10)
            msleep(100)
            moveServo(c.skyClaw, c.clawOpen, 20)
            msleep(100)
        else:
            moveServo(c.skyArm, c.armVertical, 10)
            msleep(500)
            g.rotate(180, 125)
            msleep(500)
            g.create_drive_timed(200, 2.3)
            msleep(100)
            m.drive_to_black_and_square_up(-75)
            msleep(500)
            g.rotate(38, 100)
            msleep(500)
            g.create_drive_timed(50, 2.7)
            msleep(100)
            moveServo(c.skyArm, c.armLowGrab, 10)
            msleep(100)
            moveServo(c.skyClaw, c.clawClosedMayor, 10)
            msleep(100)
            moveServo(c.skyArm, c.armVertical, 10)
            msleep(250)
            g.create_drive_timed(-50, 2.7)
            msleep(500)
            g.rotate(-38, 100)
            msleep(500)
            g.create_drive_timed(-175, 1)
            msleep(500)
            m.drive_to_black_and_square_up(-100)
            msleep(500)
            g.rotate(180, 125)
            moveServo(c.skyArm, c.armDown, 10)
            msleep(100)
            moveServo(c.skyClaw, c.clawOpen, 20)
            msleep(100)
    else:
        moveServo(c.skyArm, c.armVertical, 10)
        msleep(100)
        m.drive_to_black_and_square_up(-75)
        msleep(500)
        g.rotate(-35, 100)
        msleep(500)
        g.create_drive_timed(50, 2.2)
        msleep(100)
        moveServo(c.skyArm, c.armLowGrab, 10)
        msleep(100)
        moveServo(c.skyClaw, c.clawClosedMayor, 10)
        msleep(100)
        moveServo(c.skyArm, c.armVertical, 10)
        msleep(250)
        g.create_drive_timed(-50, 2.2)
        msleep(500)
        g.rotate(35, 100)
        msleep(500)
        g.create_drive_timed(-175, 1)
        msleep(500)
        m.drive_to_black_and_square_up(-100)
        msleep(500)
        g.rotate(180, 125)
        moveServo(c.skyArm, c.armDown, 10)
        msleep(100)
        moveServo(c.skyClaw, c.clawOpen, 20)
        msleep(100)
        moveServo(c.skyArm, c.armVertical, 10)
        msleep(500)
        g.rotate(180, 125)
        msleep(500)
        g.create_drive_timed(200, 2.3)
        msleep(100)
        m.drive_to_black_and_square_up(-75)
        msleep(500)
        g.rotate(38, 100)
        msleep(500)
        g.create_drive_timed(50, 2.7)
        msleep(100)
        moveServo(c.skyArm, c.armLowGrab, 10)
        msleep(100)
        moveServo(c.skyClaw, c.clawClosedMayor, 10)
        msleep(100)
        moveServo(c.skyArm, c.armVertical, 10)
        msleep(250)
        g.create_drive_timed(-50, 2.7)
        msleep(500)
        g.rotate(-38, 100)
        msleep(500)
        g.create_drive_timed(-175, 1)
        msleep(500)
        m.drive_to_black_and_square_up(-100)
        msleep(500)
        g.rotate(180, 125)
        moveServo(c.skyArm, c.armDown, 10)
        msleep(100)
        moveServo(c.skyClaw, c.clawOpen, 20)
        msleep(100)
        DEBUG()

def grabWaterCube():
    #Create turns and grabs large water cube
    moveServo(c.skyArm, c.armVertical)
    msleep(300)
    if c.IS_PRIME:
        g.rotate(175, 150)
    msleep(500)
    if c.IS_PRIME:
        moveServo(c.skyArm, c.armDown)
    msleep(800)
    #driveTilBlackLCliffAndSquareUp(100)
    if c.IS_PRIME:
        m.drive_to_black_and_square_up(75)
    else:
        m.drive_to_black_and_square_up(150)
    msleep(500)
    if c.IS_PRIME:
        g.create_drive_timed(-100, 1)
    elif c.IS_CLONE:
        g.create_drive_timed(100, 1.5) #Will
    msleep(500)
    if c.IS_PRIME:
        g.rotate(13, 150)
        msleep(500)
        g.create_drive_timed(100, 2)
        msleep(100)
    if c.IS_CLONE:
        msleep(100)
        g.rotate(18, 150)
        moveServo(c.skyArm, c.armDown, 10)
    msleep(750)
    moveServo(c.skyClaw, c.clawClosedWater)
    msleep(1000)
    moveServo(c.skyArm, c.armVertical)
    msleep(300)
    if c.IS_PRIME:
        g.create_drive_timed(-100, 1.5)
    msleep(300)


def dropWaterCube():
    #Create deposits large water cube on burning building
    g.rotate(-10, 150)
    msleep(300)
    if c.IS_PRIME:
        g.create_drive_timed(-100, .7)
    else:
        m.drive_to_black_and_square_up(-150)
    msleep(500)
    if c.IS_PRIME:
        m.drive_to_black_and_square_up(-100)
    msleep(500)
    if c.IS_PRIME:
        g.create_drive_timed(100, 1.5)
    else:
        g.create_drive_timed(-200, 2.1)
    msleep(500)
    if c.IS_PRIME:
        g.rotate(90, 150)
        g.create_drive_timed(-200, 3)
        msleep(300)
        m.drive_to_black_and_square_up(75)
    else:
        g.rotate(-90, 150)
        g.create_drive_timed(200, 3.3)
        m.drive_to_black_and_square_up(-75)
    if burningSky == 0:
        print("Left")
        if c.IS_CLONE:
            g.rotate(40, 100)
        else:
            g.rotate(35, 100)
        msleep(500)
        g.create_drive_timed(100, 1.8) #Will
        moveServo(c.skyArm, c.armLowSkyscraper, 5)
        msleep(100)
        moveServo(c.skyClaw, c.clawOpen, 10)
    elif burningSky == 1:
        print("middle")
        if c.IS_CLONE:
            msleep(500)
            g.rotate(2.5, 50)
            msleep(500)
            g.create_drive_timed(50, 3.3)
            msleep(500)
        msleep(250)
        moveServo(c.skyArm, c.armHighSkyscraperDeliver, 5)
        msleep(100)
        moveServo(c.skyClaw, c.clawDeliver, 5)
    else:
        print("Right")
        if c.IS_PRIME:
            g.rotate(-23, 100)
            msleep(500)
            g.create_drive_timed(-50, .5)
        elif c.IS_CLONE:
            g.rotate(-35, 100)
            msleep(500)
            g.create_drive_timed(50, 1.3)
        msleep(100)
        moveServo(c.skyArm, c.armLowSkyscraper, 5)
        msleep(100)
        moveServo(c.skyClaw, c.clawDeliver, 10)

    #After this is successful, fill function below that picks up the Mayor and Botguy and places them in the startbox
    #You shouldn't have to move the robot at all because the arm is long enough to reach the start box

#Proposed strategy
def grabFirstSkyCube():
    pass
def grabSecondSkyCube():
    pass
def connectElectricalLines():
    pass