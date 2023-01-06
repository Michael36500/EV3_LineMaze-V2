#!/usr/bin/env pybricks-micropython
import time
import pybricks.tools as pt
from pybricks.ev3devices import ColorSensor, Motor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# motory
levy_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
pravy_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
# drivebase
robot = DriveBase(levy_motor, pravy_motor, 54, 87)
# senzor
color = ColorSensor(Port.S4)
#vojta vávra


def sleduj_caru():
    global cilova_hodnota_sledovani_cary, konstanta_p, zakladni_rychlost_pro_PID, cl_navigacni
    # P formula
    cl_navigacni = color.reflection()
    error_vuci_chtenemu = cl_navigacni - cilova_hodnota_sledovani_cary
    jak_moc_se_otocit = konstanta_p * error_vuci_chtenemu
    # vykonej
    robot.drive(zakladni_rychlost_pro_PID, jak_moc_se_otocit)  # type: ignore


cilova_hodnota_sledovani_cary = 15
konstanta_p = 3
zakladni_rychlost_pro_PID = 20
    
while True:
    sleduj_caru()