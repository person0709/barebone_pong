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
    gameover = False
    effects_timer = 0
    effects_count = 0
    effects_colour = ''
    effect = False

    start = True
    
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
    
    screen.draw_str(25, 20, 'START', constants.WHITE)
    screen.draw_str(25, 26, 'GAME!', constants.WHITE)

    while (True):
	# Calculate time since last frame
        end_time = time.time()
        frame_time = end_time - start_time
        start_time = end_time

	# Pyglow effects
	if (effect):
	    effects_timer += frame_time
	    if (won == 0):
	    	if ((effects_timer)%0.4 > 0.2 and (effects_timer - frame_time)%0.4 <= 0.2):
	    	    pyglow.all(0)
		    effects_count += 1
	    	elif ((effects_timer)%0.4 <= 0.2 and (effects_timer - frame_time)%0.4 > 0.2):
	    	    pyglow.color(effects_colour, 150)
	    	if (effects_count >= 5):
		    effect = False
		    effects_count = 0
	    else:
		if (effects_timer < 0.2):
		    pyglow.color('white', 150)
		elif (effects_timer < 0.4):
		    pyglow.color('blue', 150)
		elif (effects_timer < 0.6):
		    pyglow.color('green', 150)
		elif (effects_timer < 0.8):
		    pyglow.color('yellow', 150)
		elif (effects_timer < 1.0):
		    pyglow.color('orange', 150)
		elif (effects_timer < 1.2):
		    pyglow.color('red', 150)
		elif (effects_timer < 1.4):
		    pyglow.all(0)
		    pyglow.color('white', 150)
		    effects_timer = 0

	# Noise reduction for ADC
	value1 = 0
	value2 = 0
	for i in range(20):	
	    value1 += read_adc(CHAN2)
	    value2 += read_adc(CHAN3)
	value1 /= 20
	value2 /= 20

	# Button inputs
	if (won == 0):
	    # Hardware debounce
	    # Player1 Serve
	    if (GPIO.input(10) == 1):
                if (start):
                    start = False
    		    screen.draw_str(25, 20, 'START', constants.BACKGROUND_COLOUR)
    		    screen.draw_str(25, 26, 'GAME!', constants.BACKGROUND_COLOUR)
                    net.draw()
		    time.sleep(0.2)
	    	    ball.served = True
		    start_time = time.time()-0.01
		    continue
	    	if (server == 1):
	    	    ball.served = True
	    # Player1 Power up
	    if (GPIO.input(9) == 1 and not start):
	    	player1.power_up()

	    # Software debounce
	    # Player2 Serve
	    if (debounce(0, 17)):
	    	if (server == 2):
	    	    ball.served = True
	    # Player2 Power up
	    if (debounce(1, 11) and not start):
	    	player2.power_up()
	
        # Lose condition
	if (ball.x >= screen.width-1):
            score1 += 1
            ball.served = False
	    # Draw new score
            screen.draw_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR)
    	    pyglow.color('blue', 150)
	    effects_timer = 0
	    effects_colour = 'blue'
	    effect = True
	    # Work out who's turn to serve
	    if ((score1+score2)%10 >= 5):
		server = 2
            	ball.x = player2.x-1
            	ball.y = player2.y + player2.size[1]/2
		ball.velocity = [-10, 10]
	    else:
            	ball.x = player1.x+1
            	ball.y = player1.y + player1.size[1]/2
		ball.velocity = [10, 10]
            
        # Lose condition
	if (ball.x <= 1):
            score2 += 1
            ball.served = False
	    # Draw new score
            screen.draw_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR)
    	    pyglow.color('red', 150)
	    effects_timer = 0
	    effects_colour = 'red'
	    effect = True
	    # Work out who's turn to serve
	    if ((score1+score2)%10 >= 5):
		server = 2
            	ball.x = player2.x-1
            	ball.y = player2.y + player2.size[1]/2
		ball.velocity = [-10, 10]
	    else:
            	ball.x = player1.x+1
            	ball.y = player1.y + player1.size[1]/2
		ball.velocity = [10, 10]
        
	# Has someone won?
        if (score1 >= 10):
	    won = 1
	elif (score2 >= 10):
	    won = 2

	# Move player paddles
	player1.move(value1)
	player2.move(value2)

	# Update paddles; if powerup
        player1.update(frame_time)
        player2.update(frame_time)

	# Move ball with paddle if not served
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
	    # Random speed
	    rx = random.randint(5,15)
	    ry = random.randint(5,15)
	    # Different trajectories, depending on where the paddle was hit
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
                
	# Update ball's position
        ball.update(frame_time)
	led.update(ball.x)
        
	# Draw ball
        ball.draw()
    
	# Draw player paddles
        player1.draw()
        player2.draw()

	# Draw net and score if ball was over them
	if (ball. last_pos != [ball.roundx, ball.roundy]):
            net.spot_draw(ball.last_pos[0], ball.last_pos[1])
            screen.spot_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR, ball.last_pos[0], ball.last_pos[1])
            screen.spot_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR, ball.last_pos[0], ball.last_pos[1])
        
	# Print winner once
	if (won > 0 and not gameover):
            screen.draw_str(17, 20, 'PLAYER ' + str(won), constants.WHITE)
	    screen.draw_str(25, 26, 'WINS!', constants.WHITE)
	    gameover = True



def read_adc(channel):
    '''
    Return bitshifted value of ADC channel
    '''
    bus.write_byte(I2CADDR, channel)
    tmp1 = bus.read_word_data(I2CADDR, 0x00)
    tmp1 = ((tmp1 & 0xff00) >> 8) | ((tmp1 & 0x00ff) << 8)
    tmp1 = tmp1 & 0x0fff
    return tmp1 >> 2


def debounce(btn, gpio):
    '''
    Software debounce function
    '''
    if (GPIO.input(gpio) == 0):
	btns[btn] += 1
    else:
	btns[btn] = 0
    # Pressed
    if (btns[btn] > 5):
	return True

if (__name__ == '__main__'):
    main()
