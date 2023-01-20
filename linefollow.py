#!/usr/bin/env pybricks-micropython
import time
import pybricks.tools as pt
from pybricks.ev3devices import ColorSensor, Motor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# motory
levy_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
pravy_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
# drivebase
robot = DriveBase(levy_motor, pravy_motor, 54, 96)
robot.settings(75, 502, 80, 662)
# senzor
color = ColorSensor(Port.S4)
levy_col = ColorSensor(Port.S2)
pravy_col = ColorSensor(Port.S1)
#vojta vávra


# def P():
#     global cilova_hodnota_sledovani_cary, konstanta_p, zakladni_rychlost_pro_PID, cl_navigacni
#     # P formula
#     cl_navigacni = color.reflection()
#     error_vuci_chtenemu = cl_navigacni - cilova_hodnota_sledovani_cary
    # jak_moc_se_otocit = konstanta_p * error_vuci_chtenemu
#     # vykonej

def sleduj_caru():
    global cilova_hodnota_sledovani_cary, zakladni_rychlost_pro_PID, cl_navigacni, error
    global konstanta_p, konstanta_i, konstanta_d

    # settings
    old_error = error
    cl_navigacni = color.reflection()

    # formuly
    error = cl_navigacni - cilova_hodnota_sledovani_cary
    integral = konstanta_i + error
    derivative = error - old_error
    
    # pohyb
    turn = konstanta_p * error + konstanta_i * integral + konstanta_d * derivative
    robot.drive(zakladni_rychlost_pro_PID, turn)  # type: ignore
def make_right():
    print("right")
    robot.straight(55)
    robot.turn(-90)

def make_left():
    print("left")
    robot.straight(55)
    robot.turn( 90)

def check():
    # levý senzor
    if levy_col.reflection() < cilova_hodnota_sledovani_cary - 20:
        make_left()
    # doprava
    elif pravy_col.reflection() < cilova_hodnota_sledovani_cary - 20:
        make_right()


cilova_hodnota_sledovani_cary = 50
konstanta_p = 0.7
konstanta_i = 0.2
konstanta_d = 0.1
zakladni_rychlost_pro_PID = 120
error = 0
    
while True:
    sleduj_caru()
    check() # poznámkuj tohle na 1. jízdu