#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *
import utilities as u
import camera as p
import shutdown
import movement as m
import gyro as g


def main():
    act.elec()
    print("Running!!!")
    act.init()
    act.grab_bot_mayor()
    #shut_down_in(118)
    act.head_to_elec_lines()
    act.connect_elec_lines()
    act.get_water_cube()
    act.drop_water_cube()
    u.DEBUG()


class tee :
    def __init__(self, _fd1, _fd2) :
        self.fd1 = _fd1
        self.fd2 = _fd2

    def __del__(self) :
        if self.fd1 != sys.stdout and self.fd1 != sys.stderr :
            self.fd1.close()
        if self.fd2 != sys.stdout and self.fd2 != sys.stderr :
            self.fd2.close()

    def write(self, text) :
        self.fd1.write(text)
        self.fd2.write(text)

    def flush(self) :
        self.fd1.flush()
        self.fd2.flush()

if __name__ == "__main__":
    ### sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    stdoutsav = os.fdopen(sys.stdout.fileno(), "w", 0)
    outputlog = open("/tmp/wallaby-stdout.log", "a")
    sys.stdout = tee(stdoutsav, outputlog)

    stderrsav = os.fdopen(sys.stderr.fileno(), "w", 0)
    errorlog = open("/tmp/wallaby-stderr.log", "a")
    sys.stderr = tee(stderrsav, errorlog)

    main()