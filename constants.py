
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
electric_arm = 3

#Sensor ports
left_tophat = 5
right_tophat = 4
pipe_switch = 9

if IS_PRIME:
    # Servo Positions
    arm_vertical = 1260 + 170
    arm_low_sky = 645 + 170
    arm_low_grab = 600 + 200 #570
    mayor_arm = 950 + 200
    arm_high_sky = 1310 + 170
    arm_high_sky_deliver = 990 + 170
    arm_down = 0 + 170

    claw_open = 150
    clawDeliver = 150
    claw_closed_water = 1250
    claw_closed_mayor = 1280

    electric_arm_down = 1680 #2000
    electric_arm_up = 800
    electric_arm_start = 630 #950

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

    electric_arm_down = 2000
    electric_arm_up = 758

#Camera Channels
YELLOW = 0
ORANGE = 1

#Threshold Values
MC_LIMIT = 15
SKY_LIMIT = 50

#Gyro
turn_conversion = 5100  #5500



