
from wallaby import digital

FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0
ROBOT_ID_CLONE = 0
IS_CLONE = digital(ROBOT_ID_CLONE)
IS_PRIME = not IS_CLONE

#Servo Ports
skyArm = 2
skyClaw = 1
electricalArm = 0

if IS_PRIME:
    # Servo Positions
    armVertical = 1260 + 170
    armLowSkyscraper = 645 + 170
    armLowGrab = 600 + 200 #570
    mayorArm = 950 + 200
    armHighSkyscraper = 1310 + 170
    armHighSkyscraperDeliver = 990 + 170
    armDown = 0 + 170

    clawOpen = 150
    clawDeliver = 150
    clawClosedWater = 1350
    clawClosedMayor = 1300

    electricArmDown = 2000
    electricArmUp = 800
    electricArmStart = 950

elif IS_CLONE:
    # Servo Positions
    armVertical = 1260
    armLowSkyscraper = 645
    armLowGrab = 600 #570
    mayorArm = 950
    armHighSkyscraper = 1310
    armHighSkyscraperDeliver = 990
    armDown = 0

    clawOpen = 150
    clawDeliver = 150
    clawClosedWater = 1350
    clawClosedMayor = 1300

    electricArmDown = 2000
    electricArmUp = 758

#Camera Channels
YELLOW = 0
ORANGE = 1

#Threshold Values
MC_LIMIT = 15
SKY_LIMIT = 50

#Gyro
turn_conversion = 5100  #5500



