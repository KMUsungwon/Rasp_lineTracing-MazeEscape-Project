######################################################################
### Date: 2017/10/5
### file name: TurnModule.py
### Purpose: 턴을 위한 모듈이다.
######################################################################

from setup import *
GPIO.setwarnings(False)

def pointTurn(speed, direction):
    '''
    구동체를 제자리에서 턴 하기 위한 함수
    :param speed: 모터 구동 스피드
    :param direction: 방향 "left" or "right"
    :return: None
    '''
    if direction == "right":
        motorSet(backward0, "left")
        GPIO.output(motor_pin["left"][2], GPIO.HIGH)
        motorSet(forward0, "right")
        GPIO.output(motor_pin["right"][2], GPIO.HIGH)
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(speed)
    else:
        motorSet(forward0, "left")
        GPIO.output(motor_pin["left"][2], GPIO.HIGH)
        motorSet(backward0, "right")
        GPIO.output(motor_pin["right"][2], GPIO.HIGH)
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(speed)
