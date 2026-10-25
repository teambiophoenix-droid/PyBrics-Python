
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase

prime_hub = PrimeHub()

Left_Drive_Wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Right_Drive_Wheel = Motor(Port.F, Direction.CLOCKWISE)

Left_Attachment_Motor = Motor(Port.A, Direction.CLOCKWISE)
Right_Attachment_Motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)

drive_base = DriveBase(
    Left_Drive_Wheel,
    Right_Drive_Wheel,
    62.4,
    160.0
)

# Built-in DriveBase control settings
drive_base.use_gyro(True)
drive_base.settings(
    straight_speed=1000,
    straight_acceleration=1000,
    turn_rate=100,
    turn_acceleration=150
)


def print_status(label):
    print("\n", label)
    print("Distance:", drive_base.distance(), "mm")
    print("DriveBase angle:", drive_base.angle(), "deg")


def Mission12():
    drive_base.reset(0, 0)

    print("Starting Mission 12")

    # Move forward
    drive_base.straight(2000)
    #drive_base.straight(-500)
    #drive_base.straight(250)
    print_status("After forward 250 mm")

    # Turn right
    #drive_base.turn(90)
    #drive_base.straight(250)
    #drive_base.straight(-250)
    print_status("After right turn 90 degrees")

    # Turn left
    #drive_base.turn(-90)
    #drive_base.turn(90)
    #drive_base.turn(90)
    
    print_status("After another 3 90 turns")

    # Move backward
    #drive_base.straight(-250)
    print_status("After backward 250 mm")

    print("\nMISSION 12 COMPLETE")
    print("Final distance:", drive_base.distance(), "mm")
    print("Final angle:", drive_base.angle(), "deg")


Mission12()
