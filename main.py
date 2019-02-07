#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *
import utilities as u
import camera as p
import shutdown

def main():
    print("Running CameraTest!")
    act.init()
    shut_down_in(118)
    act.findBurningBuildings()
    act.grabWaterCube()
    act.dropWaterCube()
    camera_close()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()