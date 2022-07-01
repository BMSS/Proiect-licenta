import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
TRIG =16
ECHO = 18
TRIG1= 22
ECHO1= 24
TRIG2 = 3
ECHO2 = 5
temp1=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.output(TRIG, False)
GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)

class mod_son():
    def sonarc():
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        pulse_start=time.time()
        pulse_end=time.time()
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()  
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        x = (pulse_duration * 34300)/2
        x = round( x+1.15,2)
        if x>=0 and x<=50:
            print (" Distance Sensor C:" , x,"cm")
        sleep(0.2)
        return x

    def sonars():
        GPIO.output(TRIG1, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)
        pulse_start=time.time()
        pulse_end=time.time()
        while GPIO.input(ECHO1)==0:
            pulse_start = time.time()  
        while GPIO.input(ECHO1)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        y = (pulse_duration * 34300)/2
        y = round( y+1.15,2)
        if y>=0 and y<=50:
            print (" Distance Sensor S:" , y,"cm")
        sleep(0.2)
        return y
    
    def sonard():
        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG2, False)
        pulse_start=time.time()
        pulse_end=time.time()
        while GPIO.input(ECHO2)==0:
            pulse_start = time.time()  
        while GPIO.input(ECHO2)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        z = (pulse_duration * 34300)/2
        z = round( z+1.15,2)
        if z>=0 and z<=50:
            print (" Distance Sensor D:" , z,"cm")
        sleep(0.2) 
        return z
    
def main():
    mod_son.sonarc()
    mod_son.sonars()
    mod_son.sonard()
    
if __name__=="__main__":
    while True:
        main()
