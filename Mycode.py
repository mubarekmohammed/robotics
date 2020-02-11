import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.cleanup()

#Identify the pin layout between the driver and RPi pins
#Driver 1
DIR = 23
STEP = 24
CW = 1
CCW = 0
SPR = 200


#Driver 2
DIR2 = 20
STEP2 = 21
CW2 = 1
CCW2 = 0
SPR2 = 200

#Driver 3
DIR3 = 19
STEP3 = 26
CW3 = 1
CCW3 = 0
SPR3 = 200

#Set the GPIO setmode, setup, and output
GPIO.setmode(GPIO.BCM)

#Driver 1
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

#Driver 2
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(DIR2, CW)

#Driver 3
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)
GPIO.output(DIR3, CW)

#Define step count and delay
step_count = SPR
step_count2 = SPR2
step_count3 = SPR3
delay = 0.001

#motor 1
# for i in range(500):
#     for x in range(step_count):
#         GPIO.output(STEP, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP, GPIO.LOW)
#         sleep(delay)
#         
# #motor 2        
# for j in range(500):
#     for y in range(step_count2):
#         GPIO.output(STEP2, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP2, GPIO.LOW)
#         sleep(delay)
#  
# #motor 3
# for k in range(500):
#     for z in range(step_count3):
#         GPIO.output(STEP3, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP3, GPIO.LOW)
#         sleep(delay)
            
#GPIO.cleanup()

##Run all motor individually
#motor 1
# for i in range(500):
#     for x in range(step_count):
#         GPIO.output(STEP, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP, GPIO.LOW)
#         sleep(delay)
        
#motor 2        
# for j in range(500):
#     for y in range(step_count2):
#         GPIO.output(STEP2, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP2, GPIO.LOW)
#         sleep(delay)
#  
#motor 3
# for k in range(500):
#     for z in range(step_count3):
#         GPIO.output(STEP3, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP3, GPIO.LOW)
#         sleep(delay)
#
##Run all motor simutaneously
val =input("Please input value 0 for m#1 1 for m#2 2 for m#3")
print("val ",format(val))
val = int(val)
while(val >=0):
    if (val == 0):
        print("Running motor 1")
        for i in range(10):
            for x in range(step_count):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
        #val =input("Please input value 0 for m#1 1 for m#2 2 for m#3")
        
    elif(val == 1):
        print("Running motor 2")
        for j in range(10):
            for y in range(step_count2):
                GPIO.output(STEP2, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP2, GPIO.LOW)
                sleep(delay)
        #val =input("Please input value 0 for m#1 1 for m#2 2 for m#3")
        
    elif(val == 2):
        print("Running motor 3")
        for k in range(10):
           for z in range(step_count3):
               GPIO.output(STEP3, GPIO.HIGH)
               sleep(delay)
               GPIO.output(STEP3, GPIO.LOW)
               sleep(delay)
        #val =input("Please input value 0 for m#1 1 for m#2 2 for m#3")
    else:
        print("Running all motors simultaneously")
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        
                
        
        for y in range(step_count2):
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay) 
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)
                
        
        for z in range(step_count3):
            GPIO.output(STEP3, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(delay)
            
    val =input("Please input value 0 for m#1 1 for m#2 2 for m#3")
    val = int(val)



















GPIO.cleanup()

