#!/usr/bin/env pybricks-micropython
import time
from pybricks.ev3devices import Motor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction, Color


# nastavení robota
ev3 = EV3Brick()
pravy_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
pravy_motor_navic = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
levy_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
levy_motor_navic = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)


vyladeno = 0.260
while True:
    if ev3.buttons.pressed() != []: # type: ignore
        ev3.light.on(Color.RED)
        break
# time.sleep(4.9)


levy_motor.track_target(360*1000)
levy_motor_navic.track_target(360*1000)
pravy_motor.track_target(-360*1000)
pravy_motor_navic.track_target(-360*1000)

time.sleep(vyladeno)

levy_motor.track_target(360*1000)
levy_motor_navic.track_target(360*1000)
pravy_motor.track_target(360*1000)
pravy_motor_navic.track_target(360*1000)
# while True:
#     time.sleep(1)
#     levy_motor.brake()
#     pravy_motor.brake()
#     time.sleep(0.1)
    # levy_motor.track_target(360)
    # pravy_motor.track_target(360)
    # time.sleep(0.3)
    # # time.sleep(1)




time.sleep(1)

while True:
    if ev3.buttons.pressed() != []: # type: ignore
        break