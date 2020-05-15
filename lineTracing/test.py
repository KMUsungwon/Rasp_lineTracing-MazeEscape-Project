import RPi.GPIO as GPIO # import GPIO librery
import time
import ultraModule
import turn

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

GPIO.output(MotorLeft_A, GPIO.HIGH)
GPIO.output(MotorLeft_B, GPIO.LOW)
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
    LeftPwm.start(leftSpeed*1.6)
    RightPwm.start(rightSpeed*1.6)


result = {'01111':(20, 0), '00111':(20, 5),
          '00011':(20, 7.5), '10111':(20, 9),
          '10011':(20, 14), '11110':(0, 20),
          '11100':(5, 20), '11000':(7.5, 20),
          '11101':(9, 20), '11001':(16, 20),
          '11011':(20, 20), '10001':(20, 20),
          '00000':(20, 20), '11111':(16,14),
          '00001':(20,20)}

try:
    LeftPwm.start(0)
    RightPwm.start(0)
    while True:
        print('00000000000')
        distance = ultraModule.getDistance()
        print('111111111111')
        sensor = [
            str(GPIO.input(leftmostled)),
            str(GPIO.input(leftlessled)),
            str(GPIO.input(centerled)),
            str(GPIO.input(rightlessled)),
            str(GPIO.input(rightmostled))
        ]

        print(sensor)

        inputStream = "".join(sensor)
        if distance > 20:
            print('gogogogogogo')
            print(inputStream)
            go(result[inputStream][1], result[inputStream][0])

        else :
            print(distance)
            LeftPwm.ChangeDutyCycle(0)
            RightPwm.ChangeDutyCycle(0)
            time.sleep(1)
            LeftPwm.ChangeDutyCycle(50)
            RightPwm.ChangeDutyCycle(0)
            time.sleep(0.6)
            LeftPwm.ChangeDutyCycle(0)
            RightPwm.ChangeDutyCycle(0)
            time.sleep(1)
            go(20,20)
            time.sleep(1.2)
            LeftPwm.ChangeDutyCycle(0)
            RightPwm.ChangeDutyCycle(0)
            time.sleep(0.3)
            print('zzzzzzzzzzzzzzzzz')
            LeftPwm.ChangeDutyCycle(0)
            RightPwm.ChangeDutyCycle(50)
            time.sleep(0.9)
            LeftPwm.ChangeDutyCycle(0)
            RightPwm.ChangeDutyCycle(0)
            time.sleep(0.3)

#         stop()
#         sleep(2)

except KeyboardInterrupt:
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()