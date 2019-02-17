from Screen import Screen
from Paddle import Paddle
from Net import Net
from Ball import Ball
from Led import Led
import constants

import time
import random
import math
import smbus
import RPi.GPIO as GPIO

from PyGlow import PyGlow

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Software debounce
btns = [0, 0]

I2CADDR = 0x21
CHAN1 = 0x10
CHAN2 = 0x20
CHAN3 = 0x40
CHAN4 = 0x80

bus = smbus.SMBus(1)

score1 = 0
score2 = 0

# Player 1
server = 1

end_time = 0.0
start_time = 0.0

won = 0

effects_timer = 0
effects_count = 0
effects_colour = ''
effect = False

def main():
    score1 = 9
    score2 = 0
    server = 1
    won = 0
    effects_timer = 0
    effects_count = 0
    effects_colour = ''
    effect = False
    start_time = time.time()
    
    ## Graphics class
    screen = Screen(constants.WIDTH, constants.HEIGHT)

    player1 = Paddle(screen, 3, constants.HEIGHT/2-1, constants.PLAYER1_COLOUR)
    player2 = Paddle(screen, constants.WIDTH-4, constants.HEIGHT/2-1, constants.PLAYER2_COLOUR)

    net = Net(screen, constants.NET_COLOUR)

    ball = Ball(screen, 5, 20, constants.BALL_COLOUR)

    pyglow = PyGlow()

    led = Led(5)

    net.draw()
	
    screen.draw_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR)
    screen.draw_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR)

    # Initial value
    ball.velocity = [10.0,10.0] #Roughly 8 seconds to cross screen?

    while (True):
        end_time = time.time()
        frame_time = end_time - start_time
        start_time = end_time

	if (effect):
	    effects_timer += frame_time
	    if ((effects_timer)%0.4 > 0.2 and (effects_timer - frame_time)%0.4 <= 0.2):
	    	pyglow.all(0)
		effects_count += 1
	    elif ((effects_timer)%0.4 <= 0.2 and (effects_timer - frame_time)%0.4 > 0.2):
	    	pyglow.color(effects_colour, 150)
	    if (effects_count >= 5):
		effect = False
		effects_count = 0

	value1 = read_i2c(CHAN2)
	value2 = read_i2c(CHAN3)

	if (won == 0):
	    # Hardware debounce
	    # Player1 Serve
	    if (GPIO.input(10) == 1):
	    	if (server == 1):
	    	    ball.served = True
	    # Player1 Power up
	    if (GPIO.input(9) == 1):
	    	player1.power_up()

	    # Software debounce
	    # Player2 Serve
	    if (debounce(0, 17)):
	    	if (server == 2):
	    	    ball.served = True
	    # Player2 Power up
	    if (debounce(1, 11)):
	    	player2.power_up()
	
            # Lose condition
	if (ball.x >= screen.width-1):
            score1 += 1
            ball.served = False
            screen.draw_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR)
    	    pyglow.color('blue', 150)
	    effects_timer = 0
	    effects_colour = 'blue'
	    effect = True
	    if ((score1+score2)%10 >= 5):
		server = 2
            	ball.x = player2.x-1
            	ball.y = player2.y + player2.size[1]/2
		ball.velocity = [-10, 10]
	    else:
            	ball.x = player1.x+1
            	ball.y = player1.y + player1.size[1]/2
		ball.velocity = [10, 10]
            
	if (ball.x <= 1):
            score2 += 1
            ball.served = False
            ball.x = player1.x+1
            ball.y = player1.y + player1.size[1]/2
            screen.draw_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR)
    	    pyglow.color('red', 150)
	    effects_timer = 0
	    effects_colour = 'red'
	    effect = True
	    if ((score1+score2)%10 >= 5):
		server = 2
            	ball.x = player2.x-1
            	ball.y = player2.y + player2.size[1]/2
		ball.velocity = [-10, 10]
	    else:
            	ball.x = player1.x+1
            	ball.y = player1.y + player1.size[1]/2
		ball.velocity = [10, 10]
            
        if (score1 >= 10):
	    won = 1
	elif (score2 >= 10):
	    won = 2

	# TODO: Reduce noise; multiple reads before move?
	player1.move(value1)
	player2.move(value2)

        player1.update(frame_time)
        player2.update(frame_time)

	if (not ball.served):
	    if (server == 1):
		ball.last_pos = [ball.roundx, ball.roundy]
		ball.y = player1.y + player1.size[1] / 2
		ball.x = player1.x + 1
		ball.roundx = int(round(ball.x))
        	ball.roundy = int(round(ball.y))
		if (ball.last_pos != [ball.roundx, ball.roundy]):
		    ball._moved = True

	    if (server == 2):
		ball.last_pos = [ball.roundx, ball.roundy]
		ball.y = player2.y + player2.size[1] / 2
		ball.x = player2.x - 1
		ball.roundx = int(round(ball.x))
        	ball.roundy = int(round(ball.y))
		if (ball.last_pos != [ball.roundx, ball.roundy]):
		    ball._moved = True

        # Collision Detection
        if (ball.roundx == player1.x):
	    rx = random.randint(5,15)
	    ry = random.randint(5,15)
            if (ball.roundy >= player1.y and ball.roundy <= player1.y + player1.size[1]/3):
		ball.velocity[1] = -ry
		ball.velocity[0] = rx

	    if (ball.roundy >= player1.y + player1.size[1]/3 and ball.roundy <= player1.y + player1.size[1]/3*2):
                ball.velocity[1] = 0
		ball.velocity[0] = rx

	    if (ball.roundy >= player1.y + player1.size[1]/3*2 and ball.roundy <= player1.y + player1.size[1]):
                ball.velocity[1] = ry
		ball.velocity[0] = rx

	    # Redraw paddle
	    player1._moved = True


        if (ball.roundx == player2.x):
	    rx = random.randint(5,15)
	    ry = random.randint(5,15)
            if (ball.roundy >= player2.y and ball.roundy <= player2.y + player2.size[1]/3):
		ball.velocity[1] = -ry
		ball.velocity[0] = -rx

	    if (ball.roundy >= player2.y + player2.size[1]/3 and ball.roundy <= player2.y + player2.size[1]/3*2):
                ball.velocity[1] = 0
		ball.velocity[0] = -rx

	    if (ball.roundy >= player2.y + player2.size[1]/3*2 and ball.roundy <= player2.y + player2.size[1]):
                ball.velocity[1] = ry
		ball.velocity[0] = -rx

	    # Redraw paddle
	    player2._moved = True
                
        ball.update(frame_time)
	led.update(ball.x)
        

        ball.draw()
    
        player1.draw()
        player2.draw()

        net.spot_draw(ball.last_pos[0], ball.last_pos[1])
        screen.spot_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR, ball.last_pos[0], ball.last_pos[1])
        screen.spot_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR, ball.last_pos[0], ball.last_pos[1])
        
	if (won > 0):
	    screen.draw_num(39, 20, won, constants.WHITE)
	    screen.draw_char(29, 26, 0, constants.WHITE)
	    screen.draw_char(35, 26, 1, constants.WHITE)
	    screen.draw_char(41, 26, 2, constants.WHITE)
	    screen.draw_char(47, 26, 3, constants.WHITE)



def read_i2c(channel):
    bus.write_byte(I2CADDR, channel)
    tmp1 = bus.read_word_data(I2CADDR, 0x00)
    tmp1 = ((tmp1 & 0xff00) >> 8) | ((tmp1 & 0x00ff) << 8)
    tmp1 = tmp1 & 0x0fff
    return tmp1 >> 2


def debounce(btn, gpio):
    if (GPIO.input(gpio) == 0):
	btns[btn] += 1
    else:
	btns[btn] = 0
    # Pressed
    if (btns[btn] > 5):
	return True

if (__name__ == '__main__'):
    main()
