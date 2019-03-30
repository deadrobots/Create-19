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
    global first
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
    em.clear_ticks_button()
    u.move_servo(c.electric_arm_base, c.electric_base_down)
    print("Connecting to Create")
    create_connect()
    create_full()
    #turnCalibration()
    print("Drive and Sensor Testing")
    g.rotate(-50, 150)
    msleep(500)
    p.find_burning_sky()
    done = seconds() + 3
    first = False
    print("Waiting for you to press the switch and check which building is burning")
    while not u.get_pipe_switch():
        pass
    g.rotate(50, 150)
    msleep(500)
    g.drive_condition(m.get_black_left, -250, False)
    print("Setting servos for the run")
    move_servo(c.sky_arm, c.arm_start)
    msleep(500)
    move_servo(c.sky_claw, c.claw_open)
    msleep(500)
    wait_4_light()
    c.START_TIME = seconds()
    shut_down_in(119.5)
    if u.compute_burning_MC() == False: #burning MC is on right
        print("Pushing switch")
        msleep(300)
        u.move_servo(c.sky_arm, c.arm_moving)
        u.move_servo(c.sky_arm, c.arm_button, 5)
        msleep(100)
        u.move_servo(c.sky_arm, c.arm_vertical)
    else: #burning MC is on left
        print("Not pushing switch")
        u.move_servo(c.sky_arm, c.arm_vertical)
        msleep(1000)
    msleep(500)
    g.calibrate_gyro()
    u.move_servo(c.electric_arm_base, c.electric_base_left)


def grab_bot_mayor():
    global burningSky
    global burningMCLeft
    p.count()
    burningMCLeft = p.find_burning_MC()
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
    g.create_drive_timed(400, .35)
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
    em.electric_line_motor(30, 0)
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
    move_servo(c.sky_arm, c.arm_vertical, 20)
    if c.IS_PRIME:
        g.create_drive_timed(-240, .25)
    else:
        g.create_drive_timed(-240,.5)
    g.rotate(-90, 100)
    u.move_servo(c.electric_arm_base, c.electric_base_up, 20)
    u.move_servo(c.electric_arm, c.electric_arm_start)
    em.electric_line_motor(30, -600)
    g.create_drive_timed(500, 3.5) #Square up on wall
    msleep(100)
    if not u.get_pipe_switch():
        g.create_drive_timed(-200, .65)
        g.rotate(-90, 300)
        g.drive_condition(get_bump_or_black, -500, False)
        method = u.bump_or_black_test()
        print(method)
        if method == 1:
            print("Bumped")
            g.drive_condition(on_black_left_tophat, 200, False)
        elif method == 2:
            print("Tophats")
        elif method == 3:
            print("Create sensors")
            g.drive_condition(u.bumped and on_black_left_tophat, -200, False)
        else:
            print("None (shouldn't happen)")
            g.create_drive_timed(-200, 1)
        m.drive_to_black_and_square_up(125)
        g.create_drive_timed(-120, .25)
        g.rotate(90, 125)
        g.create_drive_timed(125, 2.5) #Square up on wall
        if not u.get_pipe_switch():
            g.create_drive_timed(-250, .5)
            g.create_drive_timed(500, 1)
            msleep(300)
    else:
        msleep(11000)

def connect_elec_lines():
    #Controls a servo and motor to connect both of the elctric lines
    clear_motor_position_counter(c.electric_line_motor) #Clears motor counter
    if c.IS_PRIME:
        em.electric_line_motor(50, -900) #Moves motor to a certain position
    else:
        em.electric_line_motor(50, -800)
    u.move_servo(c.electric_arm_base, c.electric_base_swing, 20)
    em.clear_ticks(-25) #Runs motor until it hits PVC then zeros motor counter
    u.move_servo(c.electric_arm_base, c.electric_base_right, 4)
    em.clear_ticks(-25)
    em.electric_line_motor(25, 470)
    # msleep(200)
    # em.clear_ticks(-50)
    msleep(200)
    em.electric_line_motor(30, 170)
    msleep(100)
    g.create_drive_timed(-100, 1) #Drive functions use Wallaby gyro
    u.move_servo(c.electric_arm_base, c.electric_base_start_left) #Servo functions use a loop to control servo speed
    em.electric_line_motor(50, -85)
    g.create_drive_timed(100, 1.2)
    msleep(100)
    em.clear_ticks(25)
    if c.IS_PRIME:
        em.electric_line_motor(30, -500)
    else:
        em.electric_line_motor(30, -480)
    g.rotate(3, 50)
    msleep(500)
    g.rotate(-3, 50)
    em.electric_line_motor(50, -30)


def get_water_cube(): # Drives to cube of water
    if c.IS_PRIME:
        g.create_drive_timed(-400, 4)
    else:
        g.create_drive_timed(-450, 3.4)
    g.rotate(-90, 250)
    g.create_drive_timed(500, 2.1)
    g.create_drive_timed(250, .2)
    g.rotate(-85, 300)
    g.create_drive_timed(-250, .5)
    m.drive_to_black_and_square_up(100)
    g.rotate(2, 125)
    g.create_drive_timed(200, .75)
    g.create_drive_timed(100, .6)
    move_servo(c.sky_arm, c.arm_down, 10)
    msleep(100) # do not remove
    move_servo(c.sky_claw, c.claw_closed_water, 10)
    msleep(100) # do not remoove
    move_servo(c.sky_arm, c.arm_vertical, 10)


def drop_water_cube():
    #Create deposits large water cube on burning building
    g.rotate(70, 400)
    g.create_drive_timed(400, .5)
    g.drive_condition(m.on_black_left_tophat, -200, False)
    g.create_drive_timed(100, 1)
    g.rotate(-90, 100)
    g.create_drive_timed(-400, 1.3)
    g.create_drive_timed(-200, .2)
    g.rotate(-90, 250)
    g.create_drive_timed(200, 1.3)
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
            g.rotate(-42, 100)
            g.create_drive_timed(200, .25)
            g.create_drive_timed(50, 1.2)
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


    
