
from wallaby import digital

FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0
ROBOT_ID_CLONE = 0
IS_CLONE = digital(ROBOT_ID_CLONE)
IS_PRIME = not IS_CLONE

#Servo Ports
skyArm = 2
skyClaw = 3
electricalArm = 0

if IS_PRIME:
    #Servo Positions
    armVertical = 1350
    armLowSkyscraper = 2000
    armHighSkyscraper = 1795
    armHighSkyscraperDeliver = 1870
    armDown = 0

    clawOpen = 2048
    clawClosedWater = 1000

elif IS_CLONE:
    # Servo Positions
    armVertical = 1260
    armLowSkyscraper = 645
    mayorArm = 910
    armHighSkyscraper = 1310
    armHighSkyscraperDeliver = 990
    armDown = 0

    clawOpen = 2048
    clawDeliver = 1700
    clawClosedWater = 710

    clawClosedMayor = clawClosedWater - 250

    electricArmDown = 2000

#Camera Channels
YELLOW = 0
ORANGE = 1

#Threshold Values
MC_LIMIT = 15
SKY_LIMIT = 50

#Gyro
bias = 0
turn_conversion = 5100  #5500
