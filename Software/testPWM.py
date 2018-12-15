import sys, tty, termios, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# just one pwm
mot2in2 = 20
GPIO.setup(mot2in2, GPIO.OUT)
motor2_pwm2 = GPIO.PWM(mot2in2, 100) # pin to set PWM = 25, and  frequency = 100Hz

print('START MOTOR \#' + str(mot2in2) + ': Duty Cycle = 90')
motor2_pwm2.start(90)
print('5 second rule')
time.sleep(5)
print('Initiate shutdown')
motor2_pwm2.ChangeDutyCycle(0)
motor2_pwm2.stop()
GPIO.cleanup()
print('Done')

