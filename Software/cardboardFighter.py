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
weaponSpeed = 0
maxDutyCycle = 90

# Setting up the pins for motor control and usage
GPIO.setup(weaponPin, GPIO.OUT)
weapon = GPIO.PWM(weaponPin, maxDutyCycle) # pin to set PWM = 18, and  frequency = maxDutyCycleHz

GPIO.setup(mot1in1, GPIO.OUT)
motor1_pwm1 = GPIO.PWM(mot1in1, maxDutyCycle) # pin to set PWM = 22, and  frequency = maxDutyCycleHz

GPIO.setup(mot1in2, GPIO.OUT)
motor1_pwm2 = GPIO.PWM(mot1in2, maxDutyCycle) # pin to set PWM = 23, and  frequency = maxDutyCycleHz

GPIO.setup(mot2in1, GPIO.OUT)
motor2_pwm1 = GPIO.PWM(mot2in1, maxDutyCycle) # pin to set PWM = 24, and  frequency = maxDutyCycleHz

GPIO.setup(mot2in2, GPIO.OUT)
motor2_pwm2 = GPIO.PWM(mot2in2, maxDutyCycle) # pin to set PWM = 25, and  frequency = maxDutyCycleHz

GPIO.setup(LED1, GPIO.OUT)
GPIO.output(LED1, LEDstatus)
GPIO.setup(LED2, GPIO.OUT)
GPIO.output(LED2, LEDstatus)

###########################
#   Functions
###########################

###########################
def toggleWeapon():
    global weaponSpeed
    weaponSpeed = abs(weaponSpeed-maxDutyCycle)  # toggles between 0 and maxWeaponSpeed = maxDutyCycle - can moderate this to change the angle or speed
    weapon.ChangeDutyCycle(weaponSpeed)
    print('I have a plan... attack')

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
weapon.start(0)
motor1_pwm1.start(0)
motor1_pwm2.start(0)
motor2_pwm1.start(0)
motor2_pwm2.start(0)
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
            motor1_pwm2.ChangeDutyCycle(0)
            motor2_pwm2.ChangeDutyCycle(0)
            GPIO.output(mot1in1, True)
            GPIO.output(mot1in2, False)
            GPIO.output(mot2in1, True)
            GPIO.output(mot2in2, False)
            motor1_pwm1.ChangeDutyCycle(maxDutyCycle)
            motor2_pwm1.ChangeDutyCycle(maxDutyCycle)
            print('Motion: Forward. Key: ' + keyPressed)
        if keyPressed == "s":
            motor1_pwm1.ChangeDutyCycle(0)
            motor2_pwm1.ChangeDutyCycle(0)
            GPIO.output(mot1in1, False)
            GPIO.output(mot1in2, True)
            GPIO.output(mot2in1, False)
            GPIO.output(mot2in2, True)
            motor1_pwm2.ChangeDutyCycle(maxDutyCycle)
            motor2_pwm2.ChangeDutyCycle(maxDutyCycle)
            print('Motion: Reverse. Key: ' + keyPressed)
        if keyPressed == "p":
            motor1_pwm1.ChangeDutyCycle(0)
            motor1_pwm2.ChangeDutyCycle(0)
            motor2_pwm1.ChangeDutyCycle(0)
            motor2_pwm2.ChangeDutyCycle(0)
            GPIO.output(mot1in1, True)
            GPIO.output(mot1in2, False)
            GPIO.output(mot2in1, True)
            GPIO.output(mot2in2, False)
            print('Motion: Stop.') 
        if keyPressed == "a":
            motor1_pwm1.ChangeDutyCycle(0)
            motor2_pwm1.ChangeDutyCycle(0)
            motor1_pwm2.ChangeDutyCycle(0)
            motor2_pwm2.ChangeDutyCycle(0)
            GPIO.output(mot1in1, False)
            GPIO.output(mot1in2, True)
            GPIO.output(mot2in1, True)
            GPIO.output(mot2in2, False)
            motor2_pwm1.ChangeDutyCycle(maxDutyCycle)
            motor1_pwm2.ChangeDutyCycle(maxDutyCycle)
            print('Steering: Left.  Key: ' + keyPressed)
        if keyPressed == "d":
            motor1_pwm1.ChangeDutyCycle(0)
            motor2_pwm1.ChangeDutyCycle(0)
            motor1_pwm2.ChangeDutyCycle(0)
            motor2_pwm2.ChangeDutyCycle(0)
            GPIO.output(mot1in1, True)
            GPIO.output(mot1in2, False)
            GPIO.output(mot2in1, False)
            GPIO.output(mot2in2, True)
            motor1_pwm1.ChangeDutyCycle(maxDutyCycle)
            motor2_pwm2.ChangeDutyCycle(maxDutyCycle)
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
weapon.ChangeDutyCycle(0)
motor1_pwm1.ChangeDutyCycle(0)
motor1_pwm2.ChangeDutyCycle(0)
motor2_pwm1.ChangeDutyCycle(0)
motor2_pwm2.ChangeDutyCycle(0)
weapon.stop(0)
motor1_pwm1.stop(0)
motor1_pwm2.stop(0)
motor2_pwm1.stop(0)
motor2_pwm2.stop(0)
GPIO.output(LED1, False)
GPIO.output(LED2, False)
GPIO.output(mot1in1, False)
GPIO.output(mot1in2, False)
GPIO.output(mot2in1, False)
GPIO.output(mot2in2, False)
GPIO.cleanup()
print('END GAME')

