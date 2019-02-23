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

def turn_calibration():
    g.rotate(180, 100)
    msleep(500)
    DEBUG()

def init(): #Test to make sure all the moving parts and sensors work the way they should
    if c.IS_PRIME:
        print("I are prime")
    if c.IS_CLONE:
        print("I are clone")
    #SETUP
    #Arm pointing towards the medical centers
    #Edges of create line up with the black tape intersection
    #Align square up surface with left side of middle bump
    #This should ensure that the robot is pointing directly towards the middle bump (DRS forward)
    print("Starting init")
    print("Enabling my servos")
    enable_servos()
    print("Camera Init")
    p.camera_init()
    p.camera_update()
    camera_test = p.find_burning_sky()
    msleep(500)
    print("Testing Servos")
    msleep(500)
    msleep(500)
    move_servo(c.skyArm, c.armVertical)
    msleep(500)
    move_servo(c.skyClaw, c.clawOpen)
    msleep(500)
    move_servo(c.skyClaw, c.clawClosedWater)
    msleep(500)
    move_servo(c.electricalArm, c.electricArmUp)
    msleep(500)
    print("Connecting to Create")
    create_connect()
    create_full()
    #turnCalibration()
    print("Drive and Sensor Testing")
    g.rotate(-50, 150)
    msleep(500)
    g.rotate(50, 150)
    msleep(500)
    g.drive_condition(m.get_black_left, -250, False)
    print("Setting servos for the run")
    move_servo(c.skyArm, c.armDown)
    msleep(500)
    move_servo(c.skyClaw, c.clawOpen)
    msleep(500)
    move_servo(c.electricalArm, c.electricArmDown, 10)
    disable_servo(c.electricalArm)
    wait_for_button()
    c.START_TIME = seconds()
    msleep(500)
    g.calibrate_gyro()


def find_burning_biuldings(): #Determines which sky scraper and medical center is burning
    #Function determines which skyscraper and which MC are burning
    global burningMCLeft
    global burningSky
    move_servo(c.skyArm, c.armVertical)
    g.rotate(55, 100)
    msleep(500)
    burningMCLeft = p.find_burning_MC() #Eventually will need to pass this info onto lego
    if burningMCLeft == True:
        print("doing code for left")
    else:
        print("doing code for right")
    msleep(500)
    g.rotate(-55, 100)
    msleep(900)
    burningSky = p.find_burning_sky()
    if burningSky == 0:
        print("doing code for left")
    elif burningSky == 1:
        print("doing code for middle")
    else:
        print("doing code for right")
    #Do Bump to signal LEGO bot (not coded yet)


def grab_bot_mayor(): #Grabs the Botguy and the mayor off the two non burning skyscrapers
    print("Grabbing the botMayor")
    m.drive_to_black_and_square_up(-100)
    g.create_drive_timed(150, 1.6)
    g.rotate(-90, 100)
    g.create_drive_timed(200, 3.3)
    m.drive_to_black_and_square_up(-100)
    if burningSky == 0 or burningSky == 2: #center building
        #g.rotate(2.5, 50)
        if c.IS_CLONE:
            g.create_drive_timed(50, 3.2)
        else:
            g.create_drive_timed(50, 3.1)
        msleep(500)
        move_servo(c.skyArm, c.mayorArm, 5)
        msleep(100)
        move_servo(c.skyClaw, c.clawClosedMayor, 20)
        msleep(800)
        move_servo(c.skyArm, c.armVertical, 5)
        msleep(500)
        m.drive_to_black_and_square_up(-100)
        #g.create_drive_timed(-175, 1)
        g.rotate(180, 125)
        m.drive_to_black_and_square_up(100)
        g.rotate(-5, 125)
        move_servo(c.skyArm, c.armDown, 10)
        msleep(100)
        move_servo(c.skyClaw, c.clawOpen, 20)
        msleep(100)
        g.rotate(5, 125)
        if burningSky == 0: # Go to right building
            move_servo(c.skyArm, c.armVertical, 10)
            msleep(100)
            m.drive_to_black_and_square_up(-75)
            g.rotate(145, 100)
            g.create_drive_timed(50, 4.9) #2.7
            msleep(100)
            move_servo(c.skyArm, c.armLowGrab, 10)
            msleep(100)
            move_servo(c.skyClaw, c.clawClosedMayor, 20)
            msleep(100)
            move_servo(c.skyArm, c.armVertical, 10)
            msleep(250)
            g.create_drive_timed(-50, 3.5)
            g.rotate(-155, 100)
            m.drive_to_black_and_square_up(100)
            g.rotate(5, 125)
            move_servo(c.skyArm, c.armDown + 75, 10)
            msleep(100)
            move_servo(c.skyClaw, c.clawOpen, 20)
            msleep(100)
            g.rotate(-5, 125)
        else: # Go to left building
            move_servo(c.skyArm, c.armVertical, 10)
            if c.IS_PRIME:
                g.rotate(-148, 125)
            else:
                g.rotate(-143, 125)
            g.create_drive_timed(50, 5.2)
            move_servo(c.skyArm, c.armLowGrab, 10)
            msleep(100)
            move_servo(c.skyClaw, c.clawClosedMayor, 20)
            msleep(100)
            move_servo(c.skyArm, c.armVertical, 10)
            msleep(250)
            g.create_drive_timed(-50, 2.7)
            g.rotate(143, 100)
            m.drive_to_black_and_square_up(100)
            move_servo(c.skyArm, c.armDown + 75, 10)
            msleep(100)
            move_servo(c.skyClaw, c.clawOpen, 20)
            msleep(100)
    else: # Go to outside buildings
        move_servo(c.skyArm, c.armVertical, 10)
        msleep(100)
        m.drive_to_black_and_square_up(-75)
        g.rotate(-30, 100)  #-35
        g.create_drive_timed(50, 2.2)
        msleep(100)
        move_servo(c.skyArm, c.armLowGrab, 10)
        msleep(100)
        move_servo(c.skyClaw, c.clawClosedMayor, 20)
        msleep(100)
        move_servo(c.skyArm, c.armVertical, 10)
        msleep(250)
        g.create_drive_timed(-50, 2.2)
        g.rotate(-145, 100)
        m.drive_to_black_and_square_up(100)
        move_servo(c.skyArm, c.armDown, 10)
        msleep(100)
        move_servo(c.skyClaw, c.clawOpen, 20)
        msleep(100)
        move_servo(c.skyArm, c.armVertical, 10)
        msleep(500)
        g.rotate(-146, 125)
        g.create_drive_timed(100, 2.4)
        g.create_drive_timed(50, .5)
        msleep(100)
        move_servo(c.skyArm, c.armLowGrab, 10)
        msleep(100)
        move_servo(c.skyClaw, c.clawClosedMayor, 20)
        msleep(100)
        move_servo(c.skyArm, c.armVertical, 10)
        msleep(250)
        g.create_drive_timed(-50, 2.7)
        g.rotate(142, 100)
        m.drive_to_black_and_square_up(100)
        g.rotate(-10, 125)
        move_servo(c.skyArm, c.armDown + 75, 10)
        msleep(100)
        move_servo(c.skyClaw, c.clawOpen, 20)
        msleep(100)
        g.rotate(10, 125)


def head_to_elec_lines(): # Goes to electric lines and attatches them
    print("Heading to electric lines")
    move_servo(c.skyArm, c.armVertical, 10)
    if c.IS_PRIME:
        g.create_drive_timed(-60, 1)
    else:
        g.create_drive_timed(-60,2)
    g.rotate(85, 100)
    msleep(100)
    g.create_drive_timed(200, 4)
    g.rotate(10, -100)
    g.drive_condition(on_black_front, 200, False)
    g.rotate(10 , 100)
    g.create_drive_timed(200, 3)
    # g.create_drive_timed(100, 4) #Mechenical square up on pipe
    msleep(100)


def hook_up_elec_lines():
    g.create_drive_timed(-100, 1)
    g.rotate(89, 125)
    enable_servo(c.electricalArm)
    move_servo(c.electricalArm, c.electricArmStart, 10)
    g.create_drive_timed(100, 2.75)
    move_servo(c.electricalArm, c.electricArmStart - 100, 3)
    g.create_drive_timed(-50, 1.5)
    msleep(100)
    move_servo(c.electricalArm, c.electricArmDown, 50)
    m.drive_to_black_and_square_up(-100)
    msleep(250)
    g.rotate(5, 100)
    g.create_drive_timed(-50, 3.5)
    move_servo(c.electricalArm, c.electricArmStart, 10)
    msleep(100)
    move_servo(c.electricalArm, c.electricArmStart - 100, 3)
    g.create_drive_timed(-125, 2.5)
    msleep(250)
    g.create_drive_timed(125, 1)
    move_servo(c.electricalArm, c.electricArmDown, 50)
    disable_servo(c.electricalArm)


def get_water_cube(): # Drives to cube of water
    g.create_drive_timed(125, .5)
    msleep(100)
    g.rotate(-90, 100)
    g.create_drive_timed(100, 2)
    g.create_drive_timed(-200, 8)
    g.rotate(-90, 100)
    g.create_drive_timed(200, 3)
    g.create_pivot_on_right_wheel(-100, 90)
    g.create_drive_timed(-125, 1)
    m.drive_to_black_and_square_up(100)
    g.rotate(10, 100)
    g.create_drive_timed(100, 1.7)
    move_servo(c.skyArm, c.armDown, 10)
    move_servo(c.skyClaw, c.clawClosedWater, 10)
    move_servo(c.skyArm, c.armVertical, 10)


def dropWaterCube():
    #Create deposits large water cube on burning building
    g.rotate(80, 100)
    g.create_drive_timed(200, 1)
    g.drive_condition(m.on_black_front, -200, False)
    g.create_drive_timed(100, 1)
    g.rotate(-90, 100)
    g.create_drive_timed(-200, 3.2)
    g.rotate(-90, 100)
    g.create_drive_timed(200, 1)
    m.drive_to_black_and_square_up(-100)
    wait_for_button()
    if burningSky == 0:
        print("Left")
        if c.IS_CLONE:
            g.rotate(40, 100)
        else:
            g.rotate(35, 100)
        msleep(500)
        g.create_drive_timed(100, 1.8) #Will
        move_servo(c.skyArm, c.armLowSkyscraper, 5)
        msleep(100)
        move_servo(c.skyClaw, c.clawOpen, 10)
    elif burningSky == 1:
        print("middle")
        if c.IS_CLONE:
            msleep(500)
            g.rotate(2.5, 50)
            msleep(500)
            g.create_drive_timed(50, 3.3)
            msleep(500)
        msleep(250)
        move_servo(c.skyArm, c.armHighSkyscraperDeliver, 5)
        msleep(100)
        move_servo(c.skyClaw, c.clawDeliver, 5)
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
        move_servo(c.skyArm, c.armLowSkyscraper, 5)
        msleep(100)
        move_servo(c.skyClaw, c.clawDeliver, 10)



    
