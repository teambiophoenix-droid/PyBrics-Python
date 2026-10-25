from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()

#SquareRobot
#Left_Drive_Wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#Right_Drive_Wheel = Motor(Port.F, Direction.CLOCKWISE)
#Left_Attachment_Motor = Motor(Port.A, Direction.CLOCKWISE)
#Right_Attachment_Motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
#drive_base = DriveBase(Left_Drive_Wheel, Right_Drive_Wheel, 62.4, 151.0)

#TankRobot
Left_Drive_Wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Right_Drive_Wheel = Motor(Port.E, Direction.CLOCKWISE)
Left_Attachment_Motor = Motor(Port.B, Direction.CLOCKWISE)
Right_Attachment_Motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(Left_Drive_Wheel, Right_Drive_Wheel, 62.4, 145.0)

def Mission12():
    drive_base.reset(0, 0)
    
    drive_base.straight(300)
    print("After forward: Distance =", drive_base.distance(), "mm")
    #print("After forward: Turn =", drive_base.angle(), "deg")

    wait(10)

    drive_base.turn(90)
    #print("After right turn: Distance =", drive_base.distance(), "mm")
    print("After left turn: Turn =", drive_base.angle(), "deg")

    wait(10)

    #drive_base.turn(-90)
    #print("After final turn: Distance =", drive_base.distance(), "mm")
    #print("After final turn: Turn =", drive_base.angle(), "deg")

    #wait(10)

    #drive_base.straight(-250)
    #print("After backward: Distance =", drive_base.distance(), "mm")
    #print("After backward: Turn =", drive_base.angle(), "deg")




    #Right_Attachment_Motor.run_angle(200, 247)
    #drive_base.straight(55)
    #Right_Attachment_Motor.run_angle(200, -250)
    #drive_base.straight(-225) 
    #Right_Attachment_Motor.run_angle(200, 250)
    #drive_base.turn(-27)
    #drive_base.straight(400)
    #drive_base.turn(120)
    #Left_Attachment_Motor.run_angle(550, 600)
    #drive_base.straight(150)
    #Left_Attachment_Motor.run_angle(300,-130)
    #drive_base.straight(-150)

# The main program starts here.
prime_hub.imu.reset_heading(0)
drive_base.use_gyro(True)
drive_base.settings(straight_speed=500)
drive_base.settings(turn_rate=300)
drive_base.settings(straight_acceleration=300)
drive_base.settings(turn_acceleration=150)
Left_Drive_Wheel.control.target_tolerances(25, 0)
Right_Drive_Wheel.control.target_tolerances(25, 0)
Left_Drive_Wheel.control.limits(acceleration=300)
Right_Drive_Wheel.control.limits(acceleration=300)

Mission12()
