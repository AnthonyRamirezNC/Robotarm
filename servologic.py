import RPi.GPIO as GPIO
import time

#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

#Set Pin 31 as an output, and set Waist as pin 11 as PWM
GPIO.setup(29,GPIO.OUT)
Waistsrvo = GPIO.PWM(29,50) #Note 11 is pin, 50 is 50hz pulse

#Set Pin 32 as an output, and set Waist as pin 32 as PWM
GPIO.setup(31,GPIO.OUT)
LowerArmsrvo = GPIO.PWM(31,50)


#OTHER FUNCTIONS ARE WORK IN PROGRESS
#Set Pin 33 as an output, and set Waist as pin 33 as PWM
GPIO.setup(32,GPIO.OUT)
UpperArmsrvo = GPIO.PWM(32,50)

#Set Pin 36 as an output, and set Waist as pin 36 as PWM
GPIO.setup(33,GPIO.OUT)
Wristsrvo = GPIO.PWM(33,50)

#Set Pin 37 as an output, and set Waist as pin 37 as PWM
GPIO.setup(36,GPIO.OUT)
Wristrtnsrvo = GPIO.PWM(36,50)

#Set Pin 37 as an output, and set Waist as pin 37 as PWM
GPIO.setup(37,GPIO.OUT)
Clawsrvo = GPIO.PWM(37,50)


#loop to allow user to set servo angle. Try/Finally allows exit with execution of servo.stop and GPIO cleanup
def useangle(angle,mtrchoice):
    if mtrchoice == 'Waist':
        Waist(angle)
    elif mtrchoice == 'Lower Arm':
        Lower_Arm(angle)
    elif mtrchoice == 'Upper Arm':
        Upper_Arm(angle)
    elif mtrchoice == 'Wrist':
        Wrist(angle)
    elif mtrchoice == 'Wrist Rotation':
        Wrist_rtn(angle)
    else:
        print('select a servo')
#Waist control function    
def Waist(angle):
    Waistsrvo.start(0)
    Waistsrvo.ChangeDutyCycle(2+(angle/18))
    time.sleep(.5)
    Waistsrvo.ChangeDutyCycle(0)

#Lower Arm control function
def Lower_Arm(angle):
    LowerArmsrvo.start(0)
    LowerArmsrvo.ChangeDutyCycle(2+(angle/18))
    time.sleep(.5)
    LowerArmsrvo.ChangeDutyCycle(0)

#Upper arm control function
def Upper_Arm(angle):
    UpperArmsrvo.start(0)
    UpperArmsrvo.ChangeDutyCycle(2+(angle/18))
    time.sleep(.5)
    UpperArmsrvo.ChangeDutyCycle(0)

#Wrist control function
def Wrist(angle):
    Wristsrvo.start(0)
    Wristsrvo.ChangeDutyCycle(2+(angle/18))
    time.sleep(.5)
    Wristsrvo.ChangeDutyCycle(0)


#Wrist rotation control function    
def Wrist_rtn(angle):
    Wristrtnsrvo.start(0)
    Wristrtnsrvo.ChangeDutyCycle(2+(angle/18))
    time.sleep(.5)
    Wristrtnsrvo.ChangeDutyCycle(0)

    
def clsclaw():
    Clawsrvo.start(0)
    Clawsrvo.ChangeDutyCycle(2)
    time.sleep(.5)
    Clawsrvo.ChangeDutyCycle(0)
    
def opnclaw():
    Clawsrvo.start(0)
    Clawsrvo.ChangeDutyCycle(12)
    time.sleep(.5)
    Clawsrvo.ChangeDutyCycle(0)