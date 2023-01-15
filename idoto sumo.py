#!/usr/bin/env pybricks-micropython
import time
from pybricks.ev3devices import Motor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction, Color


# nastavení robota
ev3 = EV3Brick()

levy_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
pravy_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

# left_u = UltrasonicSensor(Port.S1)
# right_u = UltrasonicSensor(Port.S4)

angle = 200
speed = 5000
vyladeno = 0.306
while True:
    if ev3.buttons.pressed() != []: # type: ignore
        ev3.light.on(Color.RED)
        break
time.sleep(4.8)


levy_motor.track_target(angle)
pravy_motor.track_target(-angle)

time.sleep(vyladeno)

levy_motor.track_target(360*1000)
pravy_motor.track_target(360*1000)

time.sleep(1)

while True:
    if ev3.buttons.pressed() != []: # type: ignore
        break