"""This module uses the new Create API to control the Create.
To use it you must fist call 'connect' and when done call 'disconnect'."""


from wallaby import *
from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES


class Create:

    def __init__(self, drs_forward=True, full=True):
        self.full = full
        self.robot = self.Create(drs_forward)

    def __enter__(self):
        self.robot.connect(self.full)
        return self.robot

    def __exit__(self, *args):
        # self.robot.mode_safe()
        self.robot.drive(0, 0)
        self.robot.disconnect()
        print("exited safely")


    class Create:

        right_encoder_initial = None
        left_encoder_initial = None
        robot = None
        turn_diameter = 9.5
        port = '/dev/ttyUSB0'
        create_initialized = False

        def __init__(self, drs_forward):
            self.drs_forward = drs_forward

        def connect(self, full=True):
            """Connect to the create - must be called before anything else is used."""
            global robot
            global create_initialized
            create_initialized = True
            try:
                robot = Create2(self.port)
            except Exception:
                print('The Create is either not connected or is powered off.')
                exit(1)
            if full:
                self.mode_full()
            else:
                self.mode_safe()
            self._set_initial_counts()

        def mode_safe(self):
            self._verify()
            robot.oi_mode = MODES.SAFE

        def mode_full(self):
            self._verify()
            robot.oi_mode = MODES.FULL

        def drive_timed(self, left, right, time):
            """Drive normally"""
            left, right = self._get_direction(left, right)
            left *= 5
            right *= 5
            self._verify()  # Check if create is connected
            robot.drive_direct(left, right)
            msleep(time)
            robot.drive_direct(0, 0)

        def drive(self, left, right):
            """Drive normally without stopping"""
            left, right = self._get_direction(left, right)
            left *= 5
            right *= 5
            self._verify()  # Check if create is connected
            robot.drive_direct(left, right)

        def drive_distance(self, distance, base_speed, diff=25, refresh_rate=0):
            """Drive straight a distance"""
            self._verify()  # Check if create is connected
            # save initial encoder vals (they'll roll over, so we need to adjust for this eventually
            self._set_initial_counts()
            base_speed *= 5
            if self.drs_forward:
                distance *= -1
            if distance < 0:
                distance = abs(distance)
                base_speed *= -1
            if base_speed <  -475:
                base_speed = -475
            if base_speed > 475:
                base_speed = 475
            if base_speed < 0:
                diff *= -1
            # master is left wheel
            left_speed = base_speed
            while abs(self._convert_to_inches(self._left_encoder())) < distance - 0.75:
                r_encoder = abs(self._right_encoder())
                l_encoder = abs(self._left_encoder())
                if r_encoder > l_encoder:
                    left_speed = base_speed - diff
                if l_encoder > r_encoder:
                    left_speed = base_speed + diff
                robot.drive_direct(int(left_speed), int(base_speed))
                msleep(refresh_rate)
            robot.drive_direct(0, 0)

        def drive_conditional(self, condition, base_speed, state=True, diff=25, refresh_rate=0):
            """Drive straight a distance"""
            self._verify()  # Check if create is connected
            # save initial encoder vals (they'll roll over, so we need to adjust for this eventually
            self._set_initial_counts()
            base_speed *= 5
            if self.drs_forward:
                base_speed *= -1
            if base_speed <  -475:
                base_speed = -475
            if base_speed > 475:
                base_speed = 475
            if base_speed < 0:
                diff *= -1
            # master is left wheel
            left_speed = base_speed
            while condition() is state:
                r_encoder = abs(self._right_encoder())
                l_encoder = abs(self._left_encoder())
                if r_encoder > l_encoder:
                    left_speed = base_speed - diff
                if l_encoder > r_encoder:
                    left_speed = base_speed + diff
                robot.drive_direct(int(left_speed), int(base_speed))
                msleep(refresh_rate)
            robot.drive_direct(0, 0)

        def rotate(self, degrees, speed):
            """Rotate using both wheels"""
            self._verify()  # Check if create is connected
            self._set_initial_counts()
            speed *= 5
            if speed < 0:
                speed *= -1
            if degrees < 0:
                speed *= -1
            degrees = abs(degrees) - 5
            if degrees < 0:
                degrees = 0
            circ_percent = degrees / 360.0
            circ = 3.1415 * self.turn_diameter
            dist = circ_percent * circ
            robot.drive_direct(speed, -speed)
            while self._convert_to_inches((abs(self._left_encoder()) + abs(self._right_encoder())) / 2.0) < dist:
                pass
            robot.drive_direct(0, 0)

        def pivot_on_left(self, degrees, speed):
            """Pivot keeping the left wheel still"""
            self._verify()  # Check if create is connected
            self._set_initial_counts()
            if speed < 0:
                speed *= -1
            if degrees < 0:
                speed *= -1
            degrees = abs(degrees) - 5
            if degrees < 0:
                degrees = 0
            circ_percent = degrees / 360.0
            circ = 3.1415 * self.turn_diameter * 2
            dist = circ_percent * circ
            robot.drive_direct(speed, 0)
            while self._convert_to_inches(abs(self._right_encoder())) < dist:
                pass
            robot.drive_direct(0, 0)

        def pivot_on_right(self, degrees, speed):
            """Pivot keeping the right wheel still"""
            self._verify()  # Check if create is connected
            self._set_initial_counts()
            if speed < 0:
                speed *= -1
            if degrees < 0:
                speed *= -1
            degrees = abs(degrees) - 5
            if degrees < 0:
                degrees = 0
            circ_percent = degrees / 360.0
            circ = 3.1415 * self.turn_diameter * 2
            dist = circ_percent * circ
            robot.drive_direct(0, speed)
            while self._convert_to_inches(abs(self._left_encoder())) < dist:
                pass
            robot.drive_direct(0, 0)

        def disconnect(self):
            """Disconnect from the create"""
            self._verify()  # Check if create is connected
            robot.stop()
            print('create disconnected')

        def get_bump_right(self):
            """Returns condition of right create bumper"""
            self._verify()
            return robot.bumps_and_wheel_drops.bump_right

        def get_bump_left(self):
            """Returns condition of left create bumper"""
            self._verify()
            return robot.bumps_and_wheel_drops.bump_left

        def get_black_right(self):
            return robot.cliff_right_signal < 2200

        def get_black_left(self):
            return robot.cliff_left_signal < 2200

        def get_black_front_left(self):
            return robot.cliff_front_left_signal < 2200

        def get_black_front_right(self):
            return robot.cliff_front_right_signal < 2200

        def set_led(self, state):
            robot.set_leds(state)

        def _set_initial_counts(self):
            """Set the initial encoder counts."""
            self._verify()  # Check if create is connected
            global right_encoder_initial
            global left_encoder_initial
            right_encoder_initial = robot.right_encoder_counts
            left_encoder_initial = robot.left_encoder_counts

        def _left_encoder(self):
            """Returns the left encoder's ticks. Make sure to have called '_set_initial_counts' before use."""
            self._verify()  # Check if create is connected
            return (int(robot.left_encoder_counts) - int(left_encoder_initial))

        def _right_encoder(self):
            """Returns the right encoder's ticks. Make sure to have called '_set_initial_counts' before use."""
            self._verify()  # Check if create is connected
            return (int(robot.right_encoder_counts) - int(right_encoder_initial))

        def _convert_to_inches(self, ticks):
            """Convert encoder ticks to inches"""
            dist = ((3.1415 * 72.0 / 508.8) * ticks) / 25.4
            return dist

        def _verify(self):
            """Checks if the create is connected. Exits if not connected."""
            if not create_initialized:
                print('Please call \'connect\' at the start of your program!')
                exit(1)

        def _get_direction(self, left, right):
            if left and right and self.drs_forward:
                return (-right, -left)
            else:
                return (left, right)

