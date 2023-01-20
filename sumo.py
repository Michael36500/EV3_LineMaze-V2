#!/usr/bin/env pybricks-micropython
import time
import pybricks.tools as pt
from pybricks.ev3devices import UltrasonicSensor, Motor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase


# nastavení robota
ev3 = EV3Brick()

levy_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
pravy_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

left_u = UltrasonicSensor(Port.S1)
right_u = UltrasonicSensor(Port.S4)

# robot = DriveBase(levy_motor, pravy_motor, 54, 87)
# robot.settings(300, 1500, 500, 1500)
# robot.stop()
# ev
while True:   # type: ignore
    if ev3.buttons.pressed() != []: # type: ignore
        break

time.sleep(5)

levy_motor.dc(80)

maxi = 2550


while True:
    leva = left_u.distance()
    prava = right_u.distance()

    if prava < maxi:
        maxi = prava



    # if prava > maxi + 5 and prava < 300:
    if prava < 250:
        # time.sleep(0.05\)
        break

    # if leva < prava:
    #     levy_motor.hold()
    #     pravy_motor.hold()
    #     break
        

pravy_motor.dc(120)
levy_motor.dc(120)

time.sleep(100000)

# while True:
#     leva = left_u.distance()
#     prava = right_u.distance()

#     if leva > 50 or prava > 50:
#         pravy_motor.dc(100//2)
#         levy_motor.dc(100//2)

#     if leva < 300 and leva > 10 or prava < 300:
#         spd = 80 // 2
#         toc = (prava - leva) // 10

#         pravy_motor.dc(spd + toc)
#         levy_motor.dc(spd - toc)