#!/usr/bin/python
import os, sys
import actions as act
import createPlusPlus
import constants as c
from wallaby import *
import utilities as u
import camera as p
import shutdown

def main():
    # motorz.test()
    with createPlusPlus.Create(full=True) as cpp:
        print("Running!")
        act.init(cpp)
        shutdown.die_after_time(main_two, 118)#118

def main_two():
    act.findBurningBuildings()
    act.grabWaterCube()
    act.dropWaterCube()
    camera_close()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()