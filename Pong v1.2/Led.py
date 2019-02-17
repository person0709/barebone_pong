from Screen import Screen
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED_HEX_LIST = (
    0x05, 0x06, 0x0C, 0x0D, 0x10, 0x13, 0x14, 0x1A)
GPIO.setup(LED_HEX_LIST, GPIO.OUT)

class Led(object):
    def __init__(self, x):
	self.current_pos = int(x/10.0);
	self.prev_pos = x;
	GPIO.output(LED_HEX_LIST[self.current_pos], GPIO.HIGH)

    def update(self, x):
	self.current_pos = int(x/10.0)
	if (self.current_pos != self.prev_pos):
	    GPIO.output(LED_HEX_LIST[self.prev_pos], GPIO.LOW)
	    GPIO.output(LED_HEX_LIST[self.current_pos], GPIO.HIGH)
	    self.prev_pos = self.current_pos
