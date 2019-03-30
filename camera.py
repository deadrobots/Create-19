from wallaby import *
import constants as c
import actions as a
import utilities as u

remember = False
first = True
camera_reads = [False * 10]

def camera_init():
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


def color_proximity(color):
    #Tests to see if the center of the colored block is within a certain proximity to the center of the orange card
    if abs(get_object_center_x(color, 0)- get_object_center_x(c.YELLOW,0)) < c.COLOR_PROXIMITY: # and get_object_center_y(color,0) < get_object_center_y(c.ORANGE,0):
        return True
    return False


def color_value(color):
    #Prints data (x,y,area) of the selected color channel
    print("objects=" + str(get_object_count(color))),
    print(", x=" + str(get_object_center_x(color, 0))),
    print(", y=" + str(get_object_center_y(color, 0))),
    print(", area=" + str(get_object_area(color, 0)))


def count():
    i = 0
    while (i < 10):
        camera_update()
        i += 1
        msleep(50)


def see_color(color):
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


def find_burning_MC():
    global remember
    count()
    startTime = seconds()
    remember = True
    while (seconds() - startTime < .5):
        camera_update()
        found = False
        if get_object_count(c.YELLOW)>0:
            i = 0
            while i < get_object_count(c.YELLOW):
                if get_object_area(c.YELLOW, i) > c.MC_LIMIT:
                    print("I see yellow")
                    found = True
                    break
                i = i+1
        if found:
            print("X = ", get_object_center_x(c.YELLOW, i))
            print("Y = ", get_object_center_y(c.YELLOW, i))
            print("Area = ", get_object_area(c.YELLOW, i))
            if get_object_center_x(c.YELLOW, 0) < 80:
                print("Burning MC is on the left")
                remember = True
                return remember
            elif get_object_center_x(c.YELLOW, 0) > 80:
                print("Burning MC is on the right")
                remember = False
                return remember
        else:
            print("I see approximately no yellow")
            return remember


def find_burning_sky():
    global first
    if first:
        count()
        first = False
    count()
    startTime = seconds()
    while (seconds() - startTime < .5):
        camera_update()
        found = False
        if get_object_count(c.YELLOW) > 0:
            i = 0
            while i < get_object_count(c.YELLOW):
                if get_object_center_y(c.YELLOW, i) >= 30 and get_object_area(c.YELLOW, i) > c.SKY_LIMIT:
                    print("I see yellow in the correct area, object = ", i)
                    found = True
                    break
                i = i + 1
            if found:
                print("X = ", get_object_center_x(c.YELLOW, i))
                print("Y = ", get_object_center_y(c.YELLOW, i))
                print("Area = ", get_object_area(c.YELLOW, i))
                if get_object_center_x(c.YELLOW, i) <= 80:
                    print("Burning skyscraper is in the middle")
                    return 1
                elif get_object_center_x(c.YELLOW, i) > 80:
                    print("Burning skyscraper is on the right")
                    return 2
            else:
                print("No burning skyscraper found - assume left")
                return 0
        else:
            print("No object found - guess left")
            return 0


def find_burning_MC_improved():
    global camera_reads
    count()
    startTime = seconds()
    if len(camera_reads) == 10:
        camera_reads.pop(0)
    while (seconds() - startTime < .5):
        camera_update()
        found = False
        if get_object_count(c.YELLOW)>0:
            i = 0
            while i < get_object_count(c.YELLOW):
                if get_object_area(c.YELLOW, i) > c.MC_LIMIT:
                    print("I see yellow")
                    found = True
                    break
                i = i+1
        if found:
            print("X = ", get_object_center_x(c.YELLOW, i))
            print("Y = ", get_object_center_y(c.YELLOW, i))
            print("Area = ", get_object_area(c.YELLOW, i))
            if get_object_center_x(c.YELLOW, 0) < 80:
                print("Burning MC is on the left")
                camera_reads.append(True)
            elif get_object_center_x(c.YELLOW, 0) > 80:
                print("Burning MC is on the right")
                camera_reads.append(False)
        else:
            print("I see approximately no yellow")
            return remember
