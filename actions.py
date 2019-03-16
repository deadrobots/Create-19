from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import gyro as g
import movement as m
import electricLineMotor as em

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
    msleep(500)
    print("Testing Servos")
    msleep(500)
    msleep(500)
    move_servo(c.sky_arm, c.arm_vertical)
    msleep(500)
    move_servo(c.sky_claw, c.claw_open)
    msleep(500)
    move_servo(c.sky_claw, c.claw_closed_water)
    msleep(500)
    u.move_servo(c.electric_arm_base, c.electric_base_right)
    u.move_servo(c.electric_arm, c.electric_arm_right)
    u.move_servo(c.electric_arm, c.electric_arm_start_box)
    u.move_servo(c.electric_arm_base, c.electric_base_down)
    print("Connecting to Create")
    create_connect()
    create_full()
    #turnCalibration()
    print("Drive and Sensor Testing")
    g.rotate(-50, 150)
    msleep(500)
    p.find_burning_sky()
    g.rotate(50, 150)
    msleep(500)
    g.drive_condition(m.get_black_left, -250, False)
    print("Setting servos for the run")
    move_servo(c.sky_arm, c.arm_start)
    msleep(500)
    move_servo(c.sky_claw, c.claw_open)
    msleep(500)
    wait_for_button_camera()
    c.START_TIME = seconds()
    if u.burning_MC == False:
        u.move_servo(c.sky_arm, 200)
        u.move_servo(c.sky_arm, c.arm_button, 5)
        msleep(100)
        u.move_servo(c.sky_arm, c.arm_vertical)
    else:
        u.move_servo(c.sky_arm, c.arm_vertical)
    msleep(1000)
    g.calibrate_gyro()
    msleep(2000)


def find_burning_buildings(): #Determines which sky scraper and medical center is burning
    #Function determines which skyscraper and which MC are burning
    global burningMCLeft
    global burningSky
    g.rotate(50, 150)
    msleep(250)
    burningMCLeft = p.find_burning_MC() #Eventually will need to pass this info onto lego
    if burningMCLeft == True:
        print("doing code for left")
    else:
        print("doing code for right")
    g.rotate(-50, 100)
    msleep(300)
    burningSky = p.find_burning_sky()
    if burningSky == 0:
        print("doing code for left")
    elif burningSky == 1:
        print("doing code for middle")
    else:
        print("doing code for right")
    #Do Bump to signal LEGO bot (not coded yet)


def go_to_tallest_building(): #exactly what it sounds like
    print ("Going to the tallest building")
    move_servo(c.sky_arm, c.arm_vertical)
    print("help me i'm pivoting")
    m.pivot_till_black(100)
    print("did i pivot?")
    wait_for_button()
    g.create_drive_timed(100, 1)
    wait_for_button()
    g.rotate(8, 125)
    wait_for_button()
    g.create_drive_timed(100, 1)
    wait_for_button()
    g.rotate(-8, 125)
    print("did we do this right? Are we looking directly at the building????????????????????")
    wait_for_button()
    m.drive_to_black_and_square_up(100)
    wait_for_button()
    #g.create_drive_timed(50, 3.2)
    msleep(500)
    move_servo(c.sky_arm, c.mayor_arm, 5)
    msleep(100)
    move_servo(c.sky_claw, c.claw_closed_mayor, 20)
    msleep(800)
    move_servo(c.sky_arm, c.arm_vertical, 5)
    msleep(500)
    m.drive_to_black_and_square_up(-100)
    g.rotate(180, 125)
    m.drive_to_black_and_square_up(100)
    g.rotate(-5, 125)
    move_servo(c.sky_arm, c.arm_down, 10)
    msleep(100)
    move_servo(c.sky_claw, c.claw_open, 20)
    msleep(100)
    g.rotate(5, 125)


def grab_bot_mayor():
    global burningSky
    global burningMCLeft
    p.count()
    burningMCLeft = p.find_burning_MC()
    move_servo(c.sky_arm, c.arm_vertical)
    g.rotate(-50, 100)
    msleep(400)
    burningSky = p.find_burning_sky()
    if burningSky == 0:
        print("doing code for left")
    elif burningSky == 1:
        print("doing code for middle")
    else:
        print("doing code for right")
    print ("Going to 1/2 building")
    g.create_drive_timed(200, .7)
    m.pivot_till_black(200)
    m.drive_to_black_and_square_up(200)
    g.create_drive_timed(200, 0.5)
    m.drive_to_black_and_square_up(200)
    if burningSky!=0:
        grab_first()
        if burningSky!=1:
            grab_second()
        else:
            grab_third()
    else:
        grab_second()
        grab_third()


def grab_second():
    move_servo(c.sky_arm, c.arm_high_sky_deliver, 15)#
    g.create_drive_timed(200, 0.925)#
    move_servo(c.sky_claw, c.claw_closed_mayor, 20)#
    move_servo(c.sky_arm, c.arm_high_sky)
    g.create_drive_timed(-200, 0.1)  #
    #######################################################
    g.rotate(180, 150)
    m.drive_to_black_and_square_up(200)
    if burningSky == 0:
        g.rotate(10, 150)
    else:
        g.rotate(-10, 150)
    move_servo(c.sky_arm, c.arm_down, 15)
    move_servo(c.sky_claw, c.claw_open +500, 10)
    move_servo(c.sky_arm, c.arm_low_sky, 10)
    move_servo(c.sky_claw, c.claw_open)
    move_servo(c.sky_arm, c.arm_high_sky, 15)
    if burningSky == 0:
        g.rotate(-10, 150)
    else:
        g.rotate(10, 150)
    g.rotate(180, 150)
    m.drive_to_black_and_square_up(200)


def grab_first():
    g.create_drive_timed(200, 0.6)
    g.rotate(40, 150)
    move_servo(c.sky_claw, c.claw_open+300, 20)
    g.create_drive_timed(200, .6)
    move_servo(c.sky_arm, c.arm_low_grab +50, 10)  #
    move_servo(c.sky_claw, c.claw_closed_mayor, 15)  #
    move_servo(c.sky_arm, c.arm_high_sky, 20)
    g.create_drive_timed(-200, .325)
    g.rotate(-40, 150)
    ######################################################
    g.rotate(180, 150)
    m.drive_to_black_and_square_up(200)
    g.rotate(10, 150)
    move_servo(c.sky_arm, c.arm_down, 15)
    move_servo(c.sky_claw, c.claw_open + 500, 15)
    move_servo(c.sky_arm, c.arm_low_sky, 20)
    move_servo(c.sky_claw, c.claw_open, 20)
    move_servo(c.sky_arm, c.arm_high_sky, 20)
    g.rotate(170, 150)
    m.drive_to_black_and_square_up(200)


def grab_third():
    g.create_drive_timed(200, 0.6)
    g.rotate(-45, 150)
    move_servo(c.sky_claw, c.claw_open + 300, 20)
    g.create_drive_timed(200, .35)
    move_servo(c.sky_arm, c.arm_low_grab +50, 10)  #
    g.create_drive_timed(200, 0.3)
    move_servo(c.sky_claw, c.claw_closed_mayor, 15)  #
    move_servo(c.sky_arm, c.arm_high_sky, 15)
    g.create_drive_timed(-200, 0.55)
    g.rotate(45, 150)
    #####################################################
    g.rotate(180, 150)
    m.drive_to_black_and_square_up(200)
    g.rotate(-10, 150)
    move_servo(c.sky_arm, c.arm_down, 15)
    move_servo(c.sky_claw, c.claw_open + 500)
    move_servo(c.sky_arm, c.arm_low_sky, 20)
    move_servo(c.sky_claw, c.claw_open, 20)
    move_servo(c.sky_arm, c.arm_high_sky, 20)
    g.rotate(10, 150)
    g.rotate(180, 150)
    m.drive_to_black_and_square_up(200)


def head_to_elec_lines(): # Goes to electric lines and attatches them
    print("Heading to electric lines")
    move_servo(c.sky_arm, c.arm_vertical, 10)
    if c.IS_PRIME:
        g.create_drive_timed(-240, .25)
    else:
        g.create_drive_timed(-60,2)
    g.rotate(-90, 100)
    u.move_servo(c.electric_arm_base, c.electric_base_up)
    u.move_servo(c.electric_arm, c.electric_arm_start)
    g.create_drive_timed(500, 3.5) #Square up on wall
    msleep(100)
    g.create_drive_timed(-200, .5)
    g.rotate(-90, 150)
    g.drive_condition(get_bump_or_black, -500, False)
    method = u.bump_or_black_test()
    print(method)
    if method == 1:
        print("Bumped")
        g.create_drive_timed(200, .7)
    elif method == 2:
        print("Tophats")
    elif method == 3:
        print("Create sensors")
    else:
        print("None (shouldn't happen)")
        g.create_drive_timed(-200, 1)
    m.drive_to_black_and_square_up(125)
    g.create_drive_timed(-120, .25)
    g.rotate(90, 125)
    g.create_drive_timed(125, 2.3) #Square up on wall
    if not u.get_pipe_switch():
        g.create_drive_timed(-250, .5)
        g.create_drive_timed(500, 1)
        msleep(300)


def elec():
    em.clear_ticks_button()
    c.START_TIME = seconds()
    g.calibrate_gyro()
    if c.IS_CLONE:
        print("Clone")
    else:
      print("Prime")
    enable_servos()
    create_connect()
    msleep(250)
    u.move_servo(c.electric_arm_base, c.electric_base_right, 4)
    g.create_drive_timed(100, 1.3)
    em.clear_ticks(-20)
    msleep(100)
    em.electric_line_motor(30, 470)
    u.DEBUG()
    u.move_servo(c.electric_arm_base, c.electric_base_left_score)
    msleep(300)
    u.move_servo(c.electric_arm, c.electric_arm_slight_left, 5)
    u.move_servo(c.electric_arm, c.electric_arm_right, 4)
    msleep(100)

    msleep(200)
    u.move_servo(c.electric_arm, c.electric_arm_start)
    msleep(100)
    g.create_drive_timed(-100, 1)

    DEBUG()


def connect_elec_lines():
    # c.START_TIME = seconds()
    # g.calibrate_gyro()
    # if c.IS_CLONE:
    #     print("Clone")
    # else:
    #   print("Prime")
    # enable_servos()
    # create_connect()
    msleep(250)
    u.move_servo(c.electric_arm, c.electric_arm_right, 4)
    msleep(100)
    if c.IS_CLONE:
        u.move_servo(c.electric_arm_base, c.electric_base_right, 4)
        msleep(100)
        u.move_servo(c.electric_arm, c.electric_arm_start)
    else:
        u.move_servo(c.electric_arm_base, c.electric_base_right, 4)
        msleep(200)
        u.move_servo(c.electric_arm, c.electric_arm_start)
        msleep(100)
    g.create_drive_timed(-100, 1)
    u.move_servo(c.electric_arm, c.electric_arm_slight_left)
    if c.IS_PRIME:
        u.move_servo(c.electric_arm_base, c.electric_base_start_left)
    g.create_drive_timed(100, 1.3)
    if c.IS_CLONE:
        u.move_servo(c.electric_arm_base, c.electric_base_left)
    u.move_servo(c.electric_arm, c.electric_arm_left)
    msleep(100)
    u.move_servo(c.electric_arm_base, c.electric_base_left_score)
    msleep(300)
    u.move_servo(c.electric_arm, c.electric_arm_slight_left, 5)
    DEBUG()


def get_water_cube(): # Drives to cube of water
    g.create_drive_timed(-500, 3)
    g.rotate(-90, 150)
    g.create_drive_timed(400, 2.5)
    g.create_pivot_on_right_wheel(-150, 90)
    g.create_drive_timed(-250, .5)
    m.drive_to_black_and_square_up(100)
    g.rotate(10, 125)
    g.create_drive_timed(200, .75)
    g.create_drive_timed(100, .4)
    move_servo(c.sky_arm, c.arm_down, 10)
    move_servo(c.sky_claw, c.claw_closed_water, 10)
    move_servo(c.sky_arm, c.arm_vertical, 10)


def drop_water_cube():
    #Create deposits large water cube on burning building
    g.rotate(80, 100)
    g.create_drive_timed(200, 1)
    g.drive_condition(m.on_black_left_tophat, -200, False)
    g.create_drive_timed(100, 1)
    g.rotate(-90, 100)
    g.create_drive_timed(-200, 2.8)
    g.rotate(-90, 100)
    g.create_drive_timed(200, 1)
    m.drive_to_black_and_square_up(-100)
    if burningSky == 0:
        print("Left")
        if c.IS_CLONE:
            g.rotate(40, 100)
        else:
            g.rotate(35, 100)
        g.create_drive_timed(100, 1.4)
        move_servo(c.sky_arm, c.arm_low_sky, 10)
    elif burningSky == 1:
        print("middle")
        g.create_drive_timed(100, 1.5)
        g.create_drive_timed(50, .3)
        g.rotate(-4, 100)
        move_servo(c.sky_arm, c.arm_high_sky_deliver, 10)
    else:
        print("Right")
        if c.IS_PRIME:
            g.rotate(-34, 100)
            g.create_drive_timed(100, 1) #(50,2.5)
            g.create_drive_timed(50, 1.2)
        elif c.IS_CLONE:
            g.rotate(-35, 100)
            g.create_drive_timed(200, .25)
            g.create_drive_timed(50, .3)
        msleep(100)
        move_servo(c.sky_arm, c.arm_low_sky, 10)


def push_cube_test():
    create_connect()
    u.wait_for_button()
    u.move_servo(c.sky_arm, c.arm_vertical)
    u.move_servo(c.sky_claw, c.claw_closed_water)
    g.rotate(-20, 250)
    msleep(100)
    g.rotate(20,250)
    msleep(100)
    u.move_servo(c.sky_arm, c.arm_high_sky_deliver)
    u.DEBUG()


    
