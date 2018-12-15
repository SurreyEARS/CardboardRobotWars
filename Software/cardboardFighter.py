import sys, tty, termios, time
import RPi.GPIO as GPIO
# Setup
print('Hello, contestant... prepare for battle...\n')
GPIO.setmode(GPIO.BCM)


#mot1in1 = 17
#mot1in2 = 18
#GPIO.setup(mot1in1, GPIO.OUT)
#GPIO.setup(mot1in2,GPIO.OUT)
#motor1_pwm1 = GPIO.PWM(mot1in1, 100) # pin to set PWM = 17, and  frequency = 100Hz
#motor1_pwm2 = GPIO.PWM(mot1in2, 100) # pin to set PWM = 18, and  frequency = 100Hz
#motor1_pwm1.start(0)
#motor1_pwm2.start(0)

#mot2in1 = 24
mot2in2 = 25
#GPIO.setup(mot2in1, GPIO.OUT)
GPIO.setup(mot2in2,GPIO.OUT)
#motor2_pwm1 = GPIO.PWM(mot2in1, 100) # pin to set PWM = 24, and  frequency = 100Hz
motor2_pwm2 = GPIO.PWM(mot2in2, 100) # pin to set PWM = 25, and  frequency = 100Hz
#motor2_pwm1.start(0)
motor2_pwm2.start(0)

# Action Functions
def moveForward():
    print('mvf')
def moveBack():
    print('mvb')
def turnLeft():
    print('mvl')
def turnRight():
    print('mvr')
def toggleLights():
    print('togL')
def attack():
    print('I have a plan... attack')

# Instructions for when the user has an interface
print('Don\'t forget how to fight:')
print("w/s: acceleration")
print("a/d: steering")
print("l: lights")
print("x: exit\n")

# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Running Loop
while True:
    print('poll for stuff')

    keyPressed = getch()

    if keyPressed == "a":
        print('Key: ' + keyPressed)
    if keyPressed == "s":
        print('Key: ' + keyPressed)
    if keyPressed == "d":
        print('Key: ' + keyPressed)
    if keyPressed == "w":
        print('Key: ' + keyPressed)
    if keyPressed == "m":
        print('Key: ' + keyPressed)
    if keyPressed == "l":
        print('Key: ' + keyPressed)
    if keyPressed == "x":
        print('Key: ' + keyPressed)
        break

#Endgame
print('Cleanup...')
GPIO.cleanup()
print('END GAME')

