import RPi.GPIO as GPIO

class MotorIf(object):

    def __init__(self, fwdPin, revPin, pwmPin):
        GPIO.setup(fwdPin,GPIO.OUT)
        GPIO.setup(revPin,GPIO.OUT)
        GPIO.setup(pwmPin,GPIO.OUT)
        self.fwdPin = fwdPin
        self.revPin = revPin
        self.pwmPin = pwmPin
        self.running = False
        self.pwm = GPIO.PWM(pwmPin,100)
        print 'Created MotorIf '
        super(MotorIf,self).__init__()
        
    def set_speed(self, speed):
        self.speed = speed
        if speed == 0:
            GPIO.output(self.revPin,GPIO.LOW)
            GPIO.output(self.fwdPin,GPIO.LOW)
            self.pwm.stop()
            self.running = False
            print 'Stopping motors'
        else :
            if not self.running:
                self.pwm.start(speed)
                self.running = True
            else:
                self.pwm.ChangeDutyCycle(speed)

    def set_direction(self, dir):
        if dir == 'FORWARD':
            GPIO.output(self.revPin,GPIO.LOW)
            GPIO.output(self.fwdPin,GPIO.HIGH)
        elif dir == 'BACKWARD':
            GPIO.output(self.revPin,GPIO.HIGH)
            GPIO.output(self.fwdPin,GPIO.LOW)
        
    def stop(self):
        self.set_speed(0)

