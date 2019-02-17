from Screen import Screen
from Paddle import Paddle
from Net import Net
from Ball import Ball
import constants

import time
import random
import math
import smbus
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

def main():
    score1 = 0
    score2 = 0
    server = 1
    start_time = time.time()
    
    ## Graphics class
    screen = Screen(constants.WIDTH, constants.HEIGHT)

    player1 = Paddle(screen, 3, constants.HEIGHT/2-1, constants.PADDLE_COLOUR)
    player2 = Paddle(screen, constants.WIDTH-4, constants.HEIGHT/2-1, constants.PADDLE_COLOUR)

    net = Net(screen, constants.NET_COLOUR)

    ball = Ball(screen, 5, 20, constants.BALL_COLOUR)

    net.draw()
	
    screen.draw_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR)
    screen.draw_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR)

    # Dummy values
    ball.velocity = [10.0,10.0] #Roughly 8 seconds to cross screen?

    while (True):
        end_time = time.time()
        frame_time = end_time - start_time
        start_time = end_time

	value1 = read_i2c(CHAN2)
	value2 = read_i2c(CHAN3)

	if (GPIO.input(10) == 1):
	    ball.served = True

	if (GPIO.input(9) == 1):
	    player1.power_up()

	if (GPIO.input(8) == 0):
	    print("pin3")
	    #ball.served = True

	if (GPIO.input(11) == 0):
	    player2.power_up()

        # Lose condition
	if (ball.x >= screen.width-3):
            score1 += 1
            ball.served = False
            ball.x = player2.x-1
            ball.y = player2.y + player2.size[1]/2
            server = 2
            screen.draw_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR)
            
	if (ball.x <= 3):
            score2 += 1
            ball.served = False
            ball.x = player1.x+1
            ball.y = player1.y + player1.size[1]/2
            server = 1
            screen.draw_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR)
            
        score1 %= 10
        score2 %= 10

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
            if (ball.roundy >= player1.y and ball.roundy <= player1.y + player1.size[1]):
                # TODO: Actual trajectory stuff
		ball.velocity[0] *= -1
		
		r = random.randint(0,2)
		#if (r == 0):
		#    ball.velocity[0] = 
                

        if (ball.roundx == player2.x):
            if (ball.roundy >= player2.y and ball.roundy <= player2.y + player2.size[1]):
                ball.velocity[0] *= -1
                
        ball.update(frame_time)
    
        player1.draw()
        player2.draw()


        
        ball.draw()

        net.spot_draw(ball.last_pos[0], ball.last_pos[1])
        screen.spot_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR, ball.last_pos[0], ball.last_pos[1])
        screen.spot_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR, ball.last_pos[0], ball.last_pos[1])
        
	#time.sleep(0.01)



def read_i2c(channel):
    bus.write_byte(I2CADDR, channel)
    tmp1 = bus.read_word_data(I2CADDR, 0x00)
    tmp1 = ((tmp1 & 0xff00) >> 8) | ((tmp1 & 0x00ff) << 8)
    tmp1 = tmp1 & 0x0fff
    return tmp1 >> 2



if (__name__ == '__main__'):
    main()
