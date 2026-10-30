#These import statements bring tools from the Pybricks library into our program, so we can use them.
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# These are called initialization statements, helps to create and configure the robot’s objects
prime_hub = PrimeHub()
Left_Drive_Wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Right_Drive_Wheel = Motor(Port.E, Direction.CLOCKWISE)
Left_Attachment_Motor = Motor(Port.B)
Right_Attachment_Motor = Motor(Port.F)
drive_base = DriveBase(Left_Drive_Wheel, Right_Drive_Wheel, 62.4, 160.0)

SPEED = 300           
SPEED_ACCEL = 300 
TURN_SPEED = 300           
TURN_ACCEL = 150 


drive_base.settings(
    straight_speed=SPEED,
    straight_acceleration=SPEED_ACCEL,
    turn_rate=TURN_SPEED,
    turn_acceleration=TURN_ACCEL,
)

# ============================================================
#  COMMANDS  --  these are our coding blocks
# ============================================================
#   CODE you type                  WHAT IT DOES
#   -------------                  -------------------
#   forward(200)                   move forward 20 cm  (distance in mm; 200 = 20 cm)
#   backward(200)                  move backward 20 cm
#
#   forward(200, 500)              forward FAST  (2nd number = speed in mm/s)
#   forward(200, 120)              forward SLOW  (lower number = slower)
#   forward(200, MAX_SPEED)        forward at FULL speed
#   backward(200, MAX_SPEED)       backward at FULL speed
#
#   left(90)                       turn left 90 degrees
#   right(90)                      turn right 90 degrees
#
#   curve(200, 90)                 forward curve RIGHT
#   curve(200, -90)                forward curve LEFT
#   curve(-200, 90)                backward curve RIGHT
#   curve(-200, -90)               backward curve LEFT
#
#   leftAttachment(300, 180)       run motor leftAttachment for 180 degree
#                                  (speed 300 , 180 deg) (use -180 for other way)
#   rightAttchment(300, 180)       run motor rightAttachment for 180 degree  (use -180 for other way)
#                                  (radius 300 mm, 180 deg) (use -180 for other way)
#   pause(1)                       wait 1 second
#
#   ---- DOING TWO THINGS AT ONCE ----
#   leftAttachment_parallel(300, 180)  start left motor and KEEP GOING (do the next line too)
#   rightAttachment_parallel(300, 180) start right motor and KEEP GOING
# ============================================================

def Forward(distance_mm, speed=SPEED, accel=SPEED_ACCEL):
    drive_base.settings(straight_speed=speed,
                        straight_acceleration=accel)
    drive_base.straight(distance_mm)

def Backward(distance_mm, speed=SPEED, accel=SPEED_ACCEL):
    drive_base.settings(straight_speed=speed,
                        straight_acceleration=accel)
    drive_base.straight(-distance_mm)

def Right(degrees):
    wait(100)
    drive_base.turn(degrees)

def Left(degrees):
    wait(100)
    drive_base.turn(-degrees)

def Left_Attachment(speed, rotation):
    Left_Attachment_Motor.run_angle(speed, rotation)

def Right_Attchment(speed, rotation):
    Right_Attachment_Motor.run_angle(speed, rotation)

def Left_Attachment_parallel(speed, rotation):
    Left_Attachment_Motor.run_angle(speed, rotation, wait=False)

def Right_Attchment_parallel(speed, rotation):
    Right_Attachment_Motor.run_angle(speed, rotation, wait=False)

def Pause(seconds):
    wait(seconds * 1000)

def curve(radius_mm, degrees, speed=SPEED):
    drive_base.settings(straight_speed=speed)
    drive_base.curve(radius_mm, degrees)

def Mission12_13_7():
    Forward(500)
    Forward(500,50,50)
    Left(90)
    Left(90)
    Right(90)
    Backward(500)
    Left_Attachment(300, 360)
    Pause(1)
    Right_Attchment(300, 360)

def Mission11_6():
    Forward(500)
    Forward(500,50,50)
    
# The main program starts here.
drive_base.use_gyro(True)
drive_base.reset(0, 0)

Left_Drive_Wheel.control.target_tolerances(25, 0)
Right_Drive_Wheel.control.target_tolerances(25, 0)
Left_Drive_Wheel.control.limits(acceleration=300)
Right_Drive_Wheel.control.limits(acceleration=300)

Mission12_13_7()
#Mission11_6()