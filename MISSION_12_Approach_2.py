from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
prime_hub = PrimeHub()
Left_Drive_Wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Right_Drive_Wheel = Motor(Port.F, Direction.CLOCKWISE)
Left_Attachment_Motor = Motor(Port.A, Direction.CLOCKWISE)
Right_Attachment_Motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(Left_Drive_Wheel, Right_Drive_Wheel, 62, 180.0)

# The main program starts here.
prime_hub.imu.reset_heading(0)
drive_base.use_gyro(True)
drive_base.settings(straight_speed=300)
drive_base.settings(turn_rate=300)
drive_base.settings(straight_acceleration=300)
drive_base.settings(turn_acceleration=150)


def Mission_7_12_13():
    drive_base.reset(0, 0)
    #Bring down the left arm
    Left_Attachment_Motor.run_angle(800,-220)
    #move towards Mission 7
    drive_base.straight(700)
    #lift the MyCelium
    Left_Attachment_Motor.run_angle(800,160)
    Left_Attachment_Motor.run_angle(800,-130)
    #print("After forward: Distance =", drive_base.distance(), "mm")
    
    #Turn Towards Misson_12_13
    drive_base.turn(46)
    print("After right turn: Turn =", drive_base.angle(), "deg")
    drive_base.straight(100)
    #Perform the drop M13 and Lift M12
    Right_Attachment_Motor.run_angle(500,200)
    Right_Attachment_Motor.run_angle(800,-100)
    drive_base.straight(-100)

def Mission_6_11():    
    drive_base.reset(0, 0)
    drive_base.turn(40)
    #print("After right turn: Turn =", drive_base.angle(), "deg")
    
    #Moving backwards towards M6
    drive_base.straight(-365)
    Left_Attachment_Motor.run_angle(800,130)
    
    #Facing M6
    drive_base.turn(-46)
    
    #Move towards M6
    drive_base.settings(straight_speed=100)
    
    # Pushing the Ant without breaking it
    drive_base.straight(150)
    drive_base.settings(straight_speed=500)
    drive_base.straight(-100)
    Right_Attachment_Motor.run_angle(500,200)
    
    # Turn to perform M11_Window_To_Past
    drive_base.turn(78)
    drive_base.straight(300)

    #Heading Home Blue
    drive_base.turn(23)
    drive_base.straight(480)

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

Mission_7_12_13()
Mission_6_11()