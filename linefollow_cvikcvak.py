#!/usr/bin/env pybricks-micropython
import math
import time
import pybricks.tools as pt
from pybricks.ev3devices import ColorSensor, Motor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase

# robot
ev3 = EV3Brick()
levy_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
pravy_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
senz_motor = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)

robot = DriveBase(levy_motor, pravy_motor, 54, 87)

# senzor
color = ColorSensor(Port.S1)

def read_left():
    out = []
    senz_motor.dc(60)
    while True:
        out.append(color.reflection())
        if senz_motor.angle() > 50:
            break
    return out

def read_right():
    out = []
    senz_motor.dc(-60)
    while True:
        out.append(color.reflection())
        if senz_motor.angle() < -50:
            break
    return out

def calibrate():
    senz_motor.dc(70)
    pt.wait(500)
    senz_motor.reset_angle(90)
    senz_motor.run_target(300, 0)

def find_min_indx(pole):
    # print(pole)
    mini = min(pole)
    return pole.index(mini)

def normalize_pole(pole):
    delka = 20
    out = [0] * (delka - 1)
    ln = len(pole)
    ln = math.floor(ln / delka) + 1

    for x in range(delka - 1):
        muth = sum(pole[ln * x :ln*(x+1)])
        out[x] = muth

    return out

def drive(smer):
    smer -= 10
    hodnota_p = 2.5
    base_speed = 25
    levy_motor.dc(base_speed - smer *hodnota_p)
    pravy_motor.dc(base_speed + smer *hodnota_p)

calibrate()
senz_motor.reset_angle(0)


# hodnota_p = -10

while True:
    pole = read_left()
    pole = normalize_pole(pole)
    indx = find_min_indx(pole)
    print(indx)
    drive(indx)

    pole = read_right()
    pole = normalize_pole(pole)
    indx = find_min_indx(pole)
    indx = 20 - indx
    print(indx)
    drive(indx)