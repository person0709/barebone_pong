import smbus
import time

I2C_ADDR = 0x24

LED_ON = 0x00
LED_OFF = 0x00

bus = smbus.SMBus(1)

while True:
	bus.write_byte_data( 0x24, 0x03, 0x10 )
	time.sleep(1) 
	bus.write_byte_data( 0x24, 0x03, 0x00 )
	time.sleep(1) 
