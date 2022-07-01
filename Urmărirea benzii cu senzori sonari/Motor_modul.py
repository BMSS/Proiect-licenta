import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

en = 11
in1 = 13
in2 = 15
temp1=1

class Motor():
    def __init__ (self,EnaA,In1,In2):
        self.EnaA = EnaA
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.EnaA,GPIO.OUT);GPIO.setup(self.In1,GPIO.OUT);GPIO.setup(self.In2,GPIO.OUT);
        self.pwmA = GPIO.PWM(self.EnaA,100);
        self.pwmA.start(0);
        self.Mspeed=0;
    def move(self, pwr):
        self.pwmA.ChangeDutyCycle(pwr)
        GPIO.output(self.In2, GPIO.HIGH);
        GPIO.output(self.In1,GPIO.LOW)
        #sleep(t)
    def moveb(self,pwm):
        self.pwmA.ChangeDutyCycle(pwm) #putere motor 25%
        GPIO.output(self.In2,GPIO.LOW);
        GPIO.output(self.In1,GPIO.HIGH)
        #sleep(t)
    def stop(self):
        self.pwmA.ChangeDutyCycle(0)
        GPIO.output(self.In1,GPIO.LOW);
        GPIO.output(self.In2,GPIO.LOW)
        #sleep(t)

def main():
    motor.move(0.5,2)
    motor.stop(2)
    motor.moveB(0.5,2)
    motor.stop(2)

if __name__ == '__main__':
    motor=Motor(11,13,15)
    main()