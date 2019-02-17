import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

# bat hit is 0.15 on 17 
def startMusic():
	'''
	GPIO.output(4, True)
	GPIO.output(18, False)
	GPIO.output(17, False)
	time.sleep(2)
	GPIO.output(4, False)
	GPIO.output(18, True)
	GPIO.output(17, False)
	time.sleep(2)
	GPIO.output(4, False)
	GPIO.output(18, False)
	GPIO.output(17, True)
	time.sleep(2)'''
	for h in range(1):
		for i in range(5):
	    	    GPIO.output(4, False)
	    	    GPIO.output(18, False)
	    	    GPIO.output(17, True)
	    	    time.sleep(0.3)
	    	    GPIO.output(4, False)
	    	    GPIO.output(18, True)
	    	    GPIO.output(17, False)
	    	    time.sleep(0.1)
		for j in range(1):
		    GPIO.output(4, True)
	 	    GPIO.output(18, False)
		    GPIO.output(17, False)
		    time.sleep(0.3)
		    GPIO.output(4, False)
		    GPIO.output(18, False)
		    GPIO.output(17, False)
		    time.sleep(0.2)
 	for h in range(1):
		for i in range(5):
	    	    GPIO.output(4, False)
	    	    GPIO.output(18, False)
	    	    GPIO.output(17, True)
	    	    time.sleep(0.3)
	    	    GPIO.output(4, False)
	    	    GPIO.output(18, True)
	    	    GPIO.output(17, False)
	    	    time.sleep(0.1)
	for k in range(1):
	    GPIO.output(4, True)
	    GPIO.output(18, False)
	    GPIO.output(17, False)
	    time.sleep(0.8)
            GPIO.output(4, False)
	    GPIO.output(18, True)
	    GPIO.output(17, False)
	    time.sleep(0.3)
            GPIO.output(4, False)
	    GPIO.output(18, False)
	    GPIO.output(17, False)
	    time.sleep(0.3)
	for l in range(4):
	    GPIO.output(4, False)
	    GPIO.output(18, False)
	    GPIO.output(17, True)
	    time.sleep(0.2)
	    GPIO.output(4, False)
	    GPIO.output(18, False)
	    GPIO.output(17, False)
	    time.sleep(0.15)


def hitSound():
	GPIO.output(4, False)
	GPIO.output(18, False)
	GPIO.output(17, True)

def stopSound():
	GPIO.output(4, False)
	GPIO.output(18, False)
	GPIO.output(17, False)
