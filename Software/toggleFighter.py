###########################
#   Imports
###########################
import sys, tty, termios, time
import RPi.GPIO as GPIO

###########################
#   Global Variables
###########################
print('Hello, contestant... prepare for battle...\n')
GPIO.setmode(GPIO.BCM)
LED1 = 5
LED2 = 6
weaponPin = 18
mot1in1 = 22
mot1in2 = 23
mot2in1 = 24
mot2in2 = 25
LEDstatus = False
weaponStatus = True

# Setting up the pins for motor control and usage
GPIO.setup(weaponPin, GPIO.OUT)
GPIO.setup(mot1in1, GPIO.OUT)
GPIO.setup(mot1in2, GPIO.OUT)
GPIO.setup(mot2in1, GPIO.OUT)
GPIO.setup(mot2in2, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

###########################
#   Functions
###########################

###########################
def toggleWeapon():
    global weaponStatus
    weaponStatus = not weaponStatus
    GPIO.output(weaponPin, (weaponStatus))
    print('togW')
    

###########################
def toggleLights():
    global LEDstatus
    LEDstatus = not LEDstatus
    GPIO.output(LED1, LEDstatus)
    GPIO.output(LED2, LEDstatus)
    print('togL')    

###########################
def blinkThreeTimes():
    toggleLights()
    time.sleep(0.2)
    toggleLights()
    time.sleep(0.2)
    toggleLights()
    time.sleep(0.2)
    toggleLights()
    time.sleep(0.2)
    toggleLights()
    time.sleep(0.2)
    toggleLights()

###########################
#   Main Code
###########################
#       - initializes
#       - tests
#       - runs main loop
###########################

# Instructions for when the user has an interface
print('Don\'t forget how to fight:')
print("w/s: move forward/backward")
print("a/d: pivot left/right")
print("p: break (complete stop)")
print("m: toggle weapon on or off")
print("l: toggle lights on or off")
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


# Motors ready
GPIO.output(weaponPin, weaponStatus)
GPIO.output(mot1in1, False)
GPIO.output(mot1in2, False)
GPIO.output(mot2in1, False)
GPIO.output(mot2in2, False)

lastKeyPressed = "~"
blinkThreeTimes()
while True:
    #print('poll for stuff')
    keyPressed = getch()
    print('Curr Key: ' + keyPressed + ', Prev Key: ' + keyPressed)
    if keyPressed != lastKeyPressed:
        # press w to move forward, press s to move backward, tap p to stop.
        # if you do not press anything it will continue at max speed in the direction last travelled (fwd/bwd), and steering will be straightened automatically
        # if stopped it will not start again until a direction is pressed
        if keyPressed == "w":
            GPIO.output(mot1in1, True)
            GPIO.output(mot1in2, False)
            GPIO.output(mot2in1, True)
            GPIO.output(mot2in2, False)
            print('Motion: Forward. Key: ' + keyPressed)
        if keyPressed == "s":
            GPIO.output(mot1in1, False)
            GPIO.output(mot1in2, True)
            GPIO.output(mot2in1, False)
            GPIO.output(mot2in2, True)
            print('Motion: Reverse. Key: ' + keyPressed)
        if keyPressed == "p":
            GPIO.output(mot1in1, False)
            GPIO.output(mot1in2, False)
            GPIO.output(mot2in1, False)
            GPIO.output(mot2in2, False)
            print('Motion: Stop.') 
        if keyPressed == "a":
            GPIO.output(mot1in1, False)
            GPIO.output(mot1in2, True)
            GPIO.output(mot2in1, True)
            GPIO.output(mot2in2, False)
            print('Steering: Left.  Key: ' + keyPressed)
        if keyPressed == "d":
            GPIO.output(mot1in1, True)
            GPIO.output(mot1in2, False)
            GPIO.output(mot2in1, False)
            GPIO.output(mot2in2, True)
            print('Steering: Right. Key: ' + keyPressed)
    if keyPressed == "m":
        toggleWeapon()
        print('Key: ' + keyPressed)
    if keyPressed == "l":
        toggleLights()
        print('Key: ' + keyPressed)    
    if keyPressed == "x":
        print('Key: ' + keyPressed)
        break
    lastKeyPressed = keyPressed

###########################
####### #     # ### ####### 
#        #   #   #     #    
#         # #    #     #    
#####      #     #     #    
#         # #    #     #    
#        #   #   #     #    
####### #     # ###    #
###########################
#   Main Code
#       - sets everything off (PWM, GPIO pins, etc.)
###########################
print('Cleanup...')
blinkThreeTimes()
GPIO.output(LED1, False)
GPIO.output(LED2, False)
GPIO.output(mot1in1, False)
GPIO.output(mot1in2, False)
GPIO.output(mot2in1, False)
GPIO.output(mot2in2, False)
GPIO.cleanup()
print('END GAME')
