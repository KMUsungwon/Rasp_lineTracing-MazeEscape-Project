from time import sleep

def setMotor(x, direction):
    if direction == "right":
        if x:
            GPIO.output(MotorRight_A, GPIO.LOW)
            GPIO.output(MotorRight_B, GPIO.HIGH)
        else:
            GPIO.output(MotorRight_A, GPIO.HIGH)
            GPIO.output(MotorRight_B, GPIO.LOW)
    else:
        if x:
            GPIO.output(MotorLeft_A, GPIO.HIGH)
            GPIO.output(MotorLeft_B, GPIO.LOW)
        else:
            GPIO.output(MotorLeft_A, GPIO.LOW)
            GPIO.output(MotorLeft_B, GPIO.HIGH)

def SwingTurn(speed, running_time, direction):
    if direction == "right":
        setMotor(False, "right")
        GPIO.output(MotorLeft_PWM,GPIO.HIGH)
        GPIO.output(MotorRight_PWM,GPIO.LOW)
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(0)
    else:
        GPIO.output(MotorLeft_PWM, GPIO.LOW)
        setMotor(True, "left")
        GPIO.output(MotorRight_PWM, GPIO.HIGH)
        LeftPwm.ChangeDutyCycle(0)
        RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)