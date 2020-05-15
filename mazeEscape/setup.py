import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# 모터 핀 설정
motor_pin = {
    "left": [12, 11, 35],
    "right": [15, 13, 37],
}

# 모터 방향 설정

forward0 = True
forward1 = False

backward0 = not forward0
backward1 = not forward1


# 모터 연결

for each in list(motor_pin):
    for i in each:
        GPIO.setup(i, GPIO.OUT)

# 모터 방향 설정

GPIO.output(motor_pin["left"][0], GPIO.LOW)
GPIO.output(motor_pin["left"][1], GPIO.HIGH)
GPIO.output(motor_pin["left"][2], GPIO.HIGH)

GPIO.output(motor_pin["right"][0], GPIO.HIGH)
GPIO.output(motor_pin["right"][1], GPIO.LOW)
GPIO.output(motor_pin["right"][2], GPIO.HIGH)

# 모터 속도 초기화

LeftPwm = GPIO.PWM(motor_pin["left"][2], 100)
RightPwm = GPIO.PWM(motor_pin["right"][2], 100)

# 적외선 센서 핀 설정 left1 left2 center right1 right2
senser_pin = [16, 18, 22, 40, 32]

for each in senser_pin:
    GPIO.setup(each, GPIO.IN)

# 모터 설정 함수

def motorSet(x, direction):
    '''
    모터를 설정하는 함수이다
    :param x: True or False 모터의 방향 설정
    :param direction: 왼쪽, 오른쪽 모터에 대한 인자값
    :return: None
    '''
    if direction == "left":
        if x:
            GPIO.output(motor_pin["left"][0], GPIO.HIGH)
            GPIO.output(motor_pin["left"][1], GPIO.LOW)
        elif not x:
            GPIO.output(motor_pin["left"][0], GPIO.LOW)
            GPIO.output(motor_pin["left"][1], GPIO.HIGH)
    else:
        if x:
            GPIO.output(motor_pin["right"][0], GPIO.LOW)
            GPIO.output(motor_pin["right"][1], GPIO.HIGH)
        else:
            GPIO.output(motor_pin["right"][0], GPIO.HIGH)
            GPIO.output(motor_pin["right"][1], GPIO.LOW)