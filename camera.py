from wallaby import *
import constants as c
import actions as a
import utilities as u

def cameraInit():
    #Initializes/Opens up camera
    print("Running!")
    if camera_open_black() == 0:
        print("camera does not open")
        exit(0)
    else:
        print("camera open")
    if camera_update() == 0:
        print("no update")
    else:
        print("update")
    count()


def colorProximity(color):
    #Tests to see if the center of the colored block is within a certain proximity to the center of the orange card
    if abs(get_object_center_x(color, 0)- get_object_center_x(c.YELLOW,0)) < c.COLOR_PROXIMITY: # and get_object_center_y(color,0) < get_object_center_y(c.ORANGE,0):
        return True
    return False


def colorValue(color):
    #Prints data (x,y,area) of the selected color channel
    print("objects=" + str(get_object_count(color))),
    print(", x=" + str(get_object_center_x(color, 0))),
    print(", y=" + str(get_object_center_y(color, 0))),
    print(", area=" + str(get_object_area(color, 0)))


def count():
    i = 0
    while (i < 5):
        camera_update()
        i += 1
        msleep(60)

def seeColor(color):
    count()
    startTime = seconds()
    while (seconds() - startTime < .5):
        camera_update()
        msleep(50)
        if get_object_count(color) > 0:
            print("I see the color")
            return True
        else:
            print("I don't see the color")
            return False


def findBurningMC():
    count()
    startTime = seconds()
    while (seconds() - startTime < .5):
        camera_update()
        msleep(50)
        if get_object_count(c.YELLOW) > 0 and get_object_area(0, c.YELLOW) > c.MC_LIMIT:
            print("I see yellow")
            if get_object_center_x(c.YELLOW, 0) < 80:
                #print("Burning MC is on the left")
                return True
            elif get_object_center_x(c.YELLOW, 0) > 80:
                #print("Burning MC is on the right")
                return False
        else:
            print("I see approximately no yellow")


def findBurningSky():
    count()
    startTime = seconds()
    while (seconds() - startTime < .5):
        camera_update()
        msleep(50)
        if get_object_count(c.YELLOW) > 0 and get_object_area(0, c.YELLOW) > c.SKY_LIMIT:
            print("I see yellow")
            if get_object_center_x(c.YELLOW, 0) < 80:
                print("Burning skyscraper is in the middle")
                return 1
            elif get_object_center_x(c.YELLOW, 0) > 80:
                print("Burning skyscraper is on the right")
                return 2
        else:
            print("Burning skyscraper is on the left")
            return 0



