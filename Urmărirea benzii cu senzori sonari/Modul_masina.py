import cv2
from time import sleep
import Camera_Module
from LaneDetectionModule import getLaneCurve
import servomotor
from servomotor import servo
import utils
from Modul_sonar import mod_son
from Motor_modul import Motor
motor=Motor(11,13,15)

def main():
    img=Camera_Module.getImg()
    #width top,height T, Width BOT, height bott
    initialTrackbarVals = [120,120,30,214]
    utils.initializeTrackbars(initialTrackbarVals)
    curveVal= getLaneCurve(img,0)
    maxVal=0.4
    if curveVal>maxVal: curveVal=maxVal
    if curveVal<-maxVal: curveVal=-maxVal
    #print(curveVal)
    motor.move(30)
    #x=sen*curveVal+90
    if curveVal<0:
        x=curveVal*100+100
        servo.SetAngle(x)
    elif curveVal>0:
        x=curveVal*100+90
        servo.SetAngle(x)
         
    while mod_son.sonarc()<30:
        curveVal=0
        if mod_son.sonarc()<15:motor.moveb(15)
        elif mod_son.sonarc()<22 and mod_son.sonarc()>20: motor.stop();curveVal=0
        elif mod_son.sonars()>mod_son.sonard() and mod_son.sonarc()<30 and mod_son.sonarc()>20:
            curveVal=0
            servo.SetAngle(50)
            motor.move(50)
            sleep(1)
            #motor.stop()
            servo.SetAngle(180)
            sleep(1)
            motor.move(30)
        elif mod_son.sonard()>mod_son.sonars() and mod_son.sonarc()<30 and mod_son.sonarc()>20:
            servo.SetAngle(180)
            motor.move(30)
            sleep(1)
            servo.SetAngle(50)
            sleep(1)
            motor.move(15)
    #cv2.waitKey(1)

if __name__ == '__main__':
    while True:
        main()
