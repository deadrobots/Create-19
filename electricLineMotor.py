import utilities as u
from wallaby import *
import constants as c


def clear_ticks_button():
    print ("Waiting for motor to be placed in zero position")
    u.wait_for_button()
    clear_motor_position_counter(c.electric_line_motor)


def clear_ticks(speed):
    count = 0
    motor_power(c.electric_line_motor, speed)
    while count < 10:
        x = get_motor_position_counter(c.electric_line_motor)
        msleep(5)
        if get_motor_position_counter(c.electric_line_motor) == x:
            count = count + 1
    motor(c.electric_line_motor, 0)
    clear_motor_position_counter(c.electric_line_motor)



def electric_line_motor(speed, endPos, n = 10):
    count = 0
    if get_motor_position_counter(c.electric_line_motor) > endPos:
        speed = -speed
        motor_power(c.electric_line_motor, speed)
        while get_motor_position_counter(c.electric_line_motor) > endPos:
            x = get_motor_position_counter(c.electric_line_motor)
            msleep(5)
            if count == n:
                break
            elif x == get_motor_position_counter(c.electric_line_motor):
                count = count + 1
            else:
                count = 0
    else:
        motor_power(c.electric_line_motor, speed)
        while get_motor_position_counter(c.electric_line_motor) <  endPos:
            x = get_motor_position_counter(c.electric_line_motor)
            msleep(5)
            if count == n:
                break
            elif x == get_motor_position_counter(c.electric_line_motor):
                count = count + 1
            else:
                count = 0
    #motor(c.electric_line_motor, 0)
    freeze(c.electric_line_motor)



