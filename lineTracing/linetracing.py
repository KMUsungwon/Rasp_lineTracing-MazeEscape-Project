import RPi.GPIO as GPIO # import GPIO librery
import time
from ultraModule import getDistance

GPIO.setmode(GPIO.BOARD)

MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

GPIO.output(MotorLeft_A, GPIO.LOW)
GPIO.output(MotorLeft_B, GPIO.HIGH)
GPIO.output(MotorLeft_PWM, GPIO.HIGH)

GPIO.output(MotorRight_A, GPIO.LOW)
GPIO.output(MotorRight_B, GPIO.HIGH)
GPIO.output(MotorRight_PWM, GPIO.HIGH)

LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)

# sensor init
leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 40
rightmostled = 32

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)


# core code
def go(leftSpeed, rightSpeed):
    LeftPwm.ChangeDutyCycle(leftSpeed*1.6)
    RightPwm.ChangeDutyCycle(rightSpeed*1.6)
#     sleep(0.0001)


def stop():
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


result = {'01111':(20, 0), '00111':(20, 4),
          '00011':(20, 6.5), '10111':(20, 8),
          '10011':(20, 12), '11110':(0, 20),
          '11100':(4, 20), '11000':(6.5, 20),
          '11101':(8, 20), '11001':(15, 20),
          '11011':(20, 20), '10001':(20, 20),
          '00000':(20, 20), '11111':(0,15)}

try:
    LeftPwm.start(0)
    RightPwm.start(0)
    while True:
        print('0000000000')
        sensor = [
            str(GPIO.input(leftmostled)),
            str(GPIO.input(leftlessled)),
            str(GPIO.input(centerled)),
            str(GPIO.input(rightlessled)),
            str(GPIO.input(rightmostled))
        ]

        print(sensor)

        inputStream = "".join(sensor)

        distance = getDistance()
        if distance > 15:
            print('gogogogogogo')
            print(inputStream)
            go(result[inputStream][1], result[inputStream][0])
        else:
            print(distance)
            stop()
            time.sleep(1)
#         stop()
#         sleep(2)

except KeyboardInterrupt:
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()
except KeyError:
    print('else Thing')