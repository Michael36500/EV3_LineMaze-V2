#!/usr/bin/env pybricks-micropython
import time
from pybricks.ev3devices import Motor, UltrasonicSensor # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction, Color


# nastavení robota
ev3 = EV3Brick()
pravy_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
pravy_motor_navic = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
levy_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
levy_motor_navic = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
# a senzůrů
# left_u = UltrasonicSensor(Port.S4) ABY SE NERUŠILI https://forums.firstinspires.org/forum/general-discussions/first-programs/first-lego-league/the-challenge/products-equipment/ev3-specific/15114-do-multiple-ultrasonic-sensors-facing-same-way-interfere
ultras = UltrasonicSensor(Port.S4)

def min_lft_rgh():
    # doprava
    levy_motor.track_target(-360*1000)
    levy_motor_navic.track_target(-360*1000)
    pravy_motor.track_target(360*1000)
    pravy_motor_navic.track_target(360*1000)
    
    lft = ultras.distance()

    # doprava
    levy_motor.track_target(360*1000)
    levy_motor_navic.track_target(360*1000)
    pravy_motor.track_target(-360*1000)
    pravy_motor_navic.track_target(-360*1000)
    
    rgh = ultras.distance()

    if lft > rgh: return "left"
    if lft < rgh: return "right"
    else: return "stejne"

    

# nastaví čekací hodnotu
vyladeno = 0.35


# čekám na zmáčknutí tlačítka
ev3.light.on(Color.ORANGE)
while True:
    if ev3.buttons.pressed() != []: # type: ignore
        ev3.light.on(Color.RED)
        break
# čekám
# time.sleep(4.9)

# # otáčím se o 90
# levy_motor.track_target(360*1000)
# levy_motor_navic.track_target(360*1000)
# pravy_motor.track_target(-360*1000)
# pravy_motor_navic.track_target(-360*1000)
# # čekám čekací hodnotu
# time.sleep(vyladeno)

# jedu rovně
levy_motor.track_target(360*1000)
levy_motor_navic.track_target(360*1000)
pravy_motor.track_target(360*1000)
pravy_motor_navic.track_target(360*1000)


while True:
    dist = ultras.distance()
    print(dist)

    thresh = 300

    if dist < 100:
        print("jsem v protivníkovi")
        levy_motor.track_target(360*1000)
        levy_motor_navic.track_target(360*1000)
        pravy_motor.track_target(360*1000)
        pravy_motor_navic.track_target(360*1000)


    elif dist > thresh:
        # otáčej se na místě, hledej
        # doprava
        levy_motor.track_target(360*1000)
        levy_motor_navic.track_target(360*1000)
        pravy_motor.track_target(-360*1000)
        pravy_motor_navic.track_target(-360*1000)
    else:
        # hledáš protivníka podle lft a rgh
        min_lft_rgh()
        print ("fuck y'a all")
        pass