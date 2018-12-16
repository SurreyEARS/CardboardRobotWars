import sys, tty, termios, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# just one pwm
weaponPin = 18
GPIO.setup(weaponPin, GPIO.OUT)
weapon = GPIO.PWM(weaponPin, 100) # pin to set PWM = 18, and  frequency = 100Hz

mot1in1 = 22
GPIO.setup(mot1in1, GPIO.OUT)
motor1_pwm1 = GPIO.PWM(mot1in1, 100) # pin to set PWM = 22, and  frequency = 100Hz

mot1in2 = 23
GPIO.setup(mot1in2, GPIO.OUT)
motor1_pwm2 = GPIO.PWM(mot1in2, 100) # pin to set PWM = 23, and  frequency = 100Hz

mot2in1 = 24
GPIO.setup(mot2in1, GPIO.OUT)
motor2_pwm1 = GPIO.PWM(mot2in1, 100) # pin to set PWM = 24, and  frequency = 100Hz

mot2in2 = 25
GPIO.setup(mot2in2, GPIO.OUT)
motor2_pwm2 = GPIO.PWM(mot2in2, 100) # pin to set PWM = 25, and  frequency = 100Hz

print('START BCM PIN\#: ' + ', ' + str(weaponPin) + ', ' + str(mot1in1) + ', ' + str(mot1in2) + ', ' + str(mot2in2) + ', ' + str(mot2in2) + ': Duty Cycle = 90')
motor1_pwm1.start(90)
motor1_pwm2.start(90)
motor2_pwm1.start(90)
motor2_pwm2.start(90)
weapon.start(100)
# wait
print('5 second rule')
time.sleep(5)

#stop pwms
motor1_pwm1.ChangeDutyCycle(0)
motor1_pwm1.stop()
motor1_pwm2.ChangeDutyCycle(0)
motor1_pwm2.stop()
motor2_pwm1.ChangeDutyCycle(0)
motor2_pwm1.stop()
motor2_pwm2.ChangeDutyCycle(0)
motor2_pwm2.stop()
weapon.ChangeDutyCycle(0)
weapon.stop()

#cleanup
print('Initiate shutdown')
GPIO.cleanup()
print('Done')

