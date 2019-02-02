from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import createPlusPlus as cpp


colorOrder = []

cpp = None
burningMCLeft = True
burningSky = 0

def init(icpp):
    global cpp
    cpp = icpp
    init_movement(cpp)
    cpp.connect()
    p.cameraInit()
    p.camera_update()
    cpp.rotate(-20, 40)
    msleep(2000)
    cpp.rotate(20, 40)
    wait_for_button()

def findBurningBuildings():
    cpp.drive_distance(50, 100)
    #Function determines which skyscraper and which MC are burning
    global burningMCLeft
    global burningSky
    burningMCLeft = p.findBurningMC()
    if burningMCLeft == True:
        print("doing code for left")
    else:
        print("doing code for right")
    msleep(500)
    cpp.rotate(-50, 50)
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
    cpp.rotate(145, 50)
    driveTilBlackLCliffAndSquareUp(50)
    msleep(500)
    cpp.drive_distance(4, 50)
    cpp.rotate(8, 50)
    print("Grab water cube")
    msleep(1000)
    cpp.rotate(-8, 50)
    msleep(500)
    cpp.drive_distance(-18.5, 50)
    msleep(500)

def dropWaterCube():
    #Create deposits large water cube on burning building
    cpp.rotate(-94, 50)
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(50)
    msleep(3000)
    #Uses previous test to determine which building is on fire
    print(burningSky)
    #Drives towards burning building
    if burningSky == 0:
        print("Left")
        cpp.rotate(60, 20)
        cpp.drive_distance(12, 50)
        cpp.rotate(-60, 20)
    elif burningSky == 1:
        print("Middle")
        cpp.drive_distance(8, 50)
    else:
        print("Right")
        cpp.rotate(-60, 20)
        cpp.drive_distance(12, 50)
        cpp.rotate(60, 20)

#Proposed strategy, but might change
def grabFirstSkyCube():
    pass
def grabSecondSkyCube():
    pass
def connectElectricalLines():
    pass