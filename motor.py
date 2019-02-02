from wallaby import clear_motor_position_counter
from wallaby import freeze
from wallaby import get_motor_position_counter
from wallaby import msleep
from wallaby import seconds
from wallaby import analog
from wallaby import motor_power as motor
from wallaby import motor_power
from wallaby import digital


CLAW = 0

def rotate_spinner(rotations, speed):
    full_rotation = 1400.0
    start = get_motor_position_counter(CLAW)
    motor_power(CLAW, speed)

    tries_remaining = 3
    previous = 0
    counter = 0

    while abs(get_motor_position_counter(CLAW) - start) < abs(full_rotation * rotations) and tries_remaining > 0:
        if counter >= 10:
            counter = 0
            if tries_remaining > 0:
                motor_power(CLAW, int(-speed))
                msleep(300)
                motor_power(CLAW, speed)
            tries_remaining -= 1
        elif abs(get_motor_position_counter(CLAW)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(CLAW))
        msleep(10)
    print "rotated {} out of {}".format(get_motor_position_counter(CLAW) - start, abs(full_rotation * rotations))
    freeze(CLAW)


def rotate_until_stalled(speed):
    counter = 0
    motor_power(CLAW, speed)
    previous = abs(get_motor_position_counter(CLAW))
    while counter < 10:
        if abs(get_motor_position_counter(CLAW)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(CLAW))
        msleep(10)
    freeze(CLAW)


def wait_for_someone_to_rotate():
    print("please spin me back")
    clear_motor_position_counter(CLAW)
    while abs(get_motor_position_counter(CLAW)) < 350:
        pass
    print("good job")


def claw_to_position(position, power):
    counter = 0
    power = abs(power)
    previous = abs(get_motor_position_counter(CLAW))
    while get_motor_position_counter(CLAW) < position and counter < 10:
        motor_power(CLAW, power)
        if abs(get_motor_position_counter(CLAW)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(CLAW))
        # print('+ {}/{}'.format(get_motor_position_counter(CLAW), position))
    while get_motor_position_counter(CLAW) > position and counter < 10:
        # print('- {}/{}'.format(get_motor_position_counter(CLAW), position))
        if abs(get_motor_position_counter(CLAW)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(CLAW))
        motor_power(CLAW, -power)
    freeze(CLAW)


def set_claw_open():
    clear_motor_position_counter(CLAW)


def claw_move(power):
    motor_power(CLAW, power)


def test():
    rotate_until_stalled(20)
    rotate_until_stalled(-20)
    set_claw_open()
    #claw_to_position(600, 20)
    while True:
        print(get_motor_position_counter(CLAW))
    exit(0)
