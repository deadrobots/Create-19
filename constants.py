
from wallaby import digital

FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0
ROBOT_ID_CLONE = 0
IS_CLONE = digital(ROBOT_ID_CLONE)
IS_PRIME = not IS_CLONE

#Servo Ports
sky_arm = 0
sky_claw = 1
electric_arm_base = 2
electric_arm = 3

#Sensor ports
left_tophat = 5
right_tophat = 4
pipe_switch = 9

#motor
electric_line_motor = 3

if IS_PRIME:
    # Servo Positions
    arm_vertical = 1260 + 170
    arm_low_sky = 645 + 170
    arm_low_grab = 600 + 200 #570
    mayor_arm = 950 + 200
    arm_high_sky = 1310 + 170
    arm_high_sky_deliver = 990 + 170
    arm_down = 0 + 170
    arm_start = 375
    arm_button = 140

    claw_open = 150
    clawDeliver = 150
    claw_closed_water = 1250
    claw_closed_mayor = 1280

    #Electric base
    electric_base_down = 470 -470
    electric_base_up = 1920-470
    electric_base_right = 2047-470
    electric_base_left = 1680-470
    electric_base_left_score = 1800-470
    electric_base_start_left = 1870-470
    electric_base_swing = 1910

    #Electric arm
    electric_arm_start = 920
    electric_arm_right = 20
    electric_arm_start_box = 1230
    electric_arm_slight_left = 1350
    electric_arm_left = 2047

    # Gyro
    turn_conversion = 5100  # 5500


elif IS_CLONE:
    # Servo Positions
    arm_vertical = 1260
    arm_low_sky = 645
    arm_low_grab = 600 #570
    mayor_arm = 950
    arm_high_sky = 1310
    arm_high_sky_deliver = 990
    arm_down = 0

    claw_open = 150
    clawDeliver = 150
    claw_closed_water = 1350
    claw_closed_mayor = 1300

    #Electric base
    electric_base_down = 540
    electric_base_up = 1815
    electric_base_right = 1940
    electric_base_left = 1890
    electric_base_left_score = 1740

    #Electric arm
    electric_arm_start = 815
    electric_arm_right = 0
    electric_arm_slight_left = 1180
    electric_arm_left = 2047

    #Gyro
    turn_conversion = 5100  #5500

#Camera Channels
YELLOW = 0
ORANGE = 1

#Threshold Values
MC_LIMIT = 15
SKY_LIMIT = 50





