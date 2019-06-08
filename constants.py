
from wallaby import digital

FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0
ROBOT_ID_CLONE = 0
IS_CLONE = digital(ROBOT_ID_CLONE)
IS_PRIME = not IS_CLONE
STARTLIGHT = 0

EThresh = 2000  #2500

ET = 2

#Servo Ports

sky_claw = 1
electric_arm_base = 2
sky_arm = 3
meople_claw = 0
meople_arm = 2
ambulance_claw = 0

#Sensor ports
left_tophat = 5
right_tophat = 4
pipe_switch = 9

#motor
electric_line_motor = 3
ambulance_arm = 0

if IS_PRIME:
    # Servo Positions
    arm_offset = -180
    arm_vertical = 1430 + arm_offset
    arm_low_sky = 815 + arm_offset
    arm_low_grab = 850 + arm_offset
    mayor_arm = 1150 + arm_offset
    arm_high_sky = 1480 + arm_offset
    arm_high_sky_deliver = 1210 + arm_offset
    arm_down = 0
    arm_start = 375 + arm_offset
    arm_button = 0
    arm_moving =90

    claw_open = 150
    clawDeliver = 150
    claw_closed_water = 1250
    claw_closed_mayor = 1300

    #meople arm
    meople_arm_up = 1390
    meople_arm_down = 245

    #meople claw
    meople_claw_open = 854
    meople_claw_closed = 678

    # Gyro
    turn_conversion = 5100  # 5500


elif IS_CLONE:
    # Servo Positions
    arm_vertical = 1445
    arm_low_sky = 830
    arm_low_grab = 850
    mayor_arm = 1135
    arm_high_sky = 1485
    arm_high_sky_deliver = 1175
    arm_down = 255
    arm_start = 375
    arm_button = 185
    arm_moving = 200

    claw_open = 150
    clawDeliver = 150
    claw_closed_water = 1160
    claw_closed_mayor = 1190

    #Electric base
    electric_base_down = 0
    electric_base_up = 1450
    electric_base_right = 1460
    electric_base_left = 1210
    electric_base_left_score = 1330
    electric_base_start_left = 1299
    electric_base_swing = 1800

    #Electric arm
    electric_arm_start = 815
    electric_arm_right = 0
    electric_arm_slight_left = 1180
    electric_arm_left = 2047

    #Meople arm
    meople_arm_up = 1560
    meople_arm_meople_grab = 360 #plz do not change this i enjoy this
    meople_arm_down = 290

    #Meople claw
    meople_claw_wide = 1320
    meople_claw_open = 1580
    meople_claw_closed = 1750


    #Gyro
    turn_conversion = 5100  #5500

#Camera Channels
YELLOW = 0
ORANGE = 1

#Threshold Values
MC_LIMIT = 15
SKY_LIMIT = 50





