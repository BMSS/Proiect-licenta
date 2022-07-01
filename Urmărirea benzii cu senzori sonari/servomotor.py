import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(33, GPIO.OUT)
pwm=GPIO.PWM(33, 50)
pwm.start(0)

class servo():
    
    def SetAngle(angle):
        duty=angle/18+2
        pwm.start(duty)
        #GPIO.output(33, True)
        pwm.ChangeDutyCycle(duty)
        #sleep(0.4)
        #GPIO.output(33, False)
        #return angle
        
def main():       
    #servo.SetAngle(90)
    #sleep(0.5)    
    servo.SetAngle(45)
    #20 maxim stanga
    print("Viraj maxim stanga")
    sleep(1)
    servo.SetAngle(90)
    #90 drept
    print("Centru")
    sleep(1)
    servo.SetAngle(180)
    #180 maxim dreapta
    print("Viraj maxim dreapta")
    #sleep(0.5)
    #servo.SetAngle(90) #inapoi la centru
    sleep(1)
    #servo.SetAngle_2(12)
    #pwm.stop()
    #GPIO.cleanup()
    
if __name__=="__main__":
    while True:
        main()