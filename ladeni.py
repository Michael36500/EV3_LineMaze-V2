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
robot = DriveBase(levy_motor, pravy_motor, 54, 87)


# forward
# robot.straight(300)

# 360
robot.turn(360)
exit()