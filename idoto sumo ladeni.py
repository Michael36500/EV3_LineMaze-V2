#!/usr/bin/env pybricks-micropython
import time
from pybricks.ev3devices import Motor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction, Button, Color


# nastavení robota
ev3 = EV3Brick()

levy_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
pravy_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

# left_u = UltrasonicSensor(Port.S1)
# right_u = UltrasonicSensor(Port.S4)


speed = 5000
vyladeno = 0.3

def sumo(wait_cas):
    while True:
        if ev3.buttons.pressed() != []: # type: ignore
            ev3.light.on(Color.RED)
            break

    levy_motor.track_target(100000)
    pravy_motor.track_target(-100000)

    time.sleep(wait_cas)

    levy_motor.track_target(360*1000)
    pravy_motor.track_target(360*1000)

    time.sleep(1)

    pravy_motor.stop()
    levy_motor.stop()


while True:
    if ev3.buttons.pressed() == [Button.LEFT]: # type: ignore
        ev3.screen.print(vyladeno)
        vyladeno = round(vyladeno + 0.01, 3)
        time.sleep(0.25)

    if ev3.buttons.pressed() == [Button.RIGHT]: # type: ignore
        ev3.screen.print(vyladeno)
        vyladeno = round(vyladeno - 0.01, 3)
        time.sleep(0.25)
        

    if ev3.buttons.pressed() == [Button.UP]: # type: ignore
        ev3.screen.print(vyladeno)
        vyladeno = round(vyladeno + 0.001, 3)
        time.sleep(0.25)

    if ev3.buttons.pressed() == [Button.DOWN]: # type: ignore
        ev3.screen.print(vyladeno)
        vyladeno = round(vyladeno - 0.001, 3)
        time.sleep(0.25)


    if ev3.buttons.pressed() == [Button.CENTER]: # type: ignore
        ev3.screen.print(vyladeno)
        print(vyladeno)
        sumo(vyladeno)
