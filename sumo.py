#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import UltrasonicSensor, Motor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase


# nastavení robota
ev3 = EV3Brick()

levy_motor = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
pravy_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

ultra_sonic = UltrasonicSensor(Port.S4)

# robot = DriveBase(levy_motor, pravy_motor, 54, 87)

# robot.straight(300)
# robot.turn(360)

# robot.settings(300, 1500, 500, 1500)
# print(robot.settings())

# robot.stop()

levy_motor.dc(80)


maxi = 2550

while True:
    dist = ultra_sonic.distance()
    if dist < maxi:
        maxi = dist
    print(dist, maxi)
    if dist > maxi + 5 and dist < 300:
        levy_motor.hold()
        pravy_motor.hold()
        break

# robot.drive(150, 0)
levy_motor.track_target(360*100)
pravy_motor.track_target(360*100)