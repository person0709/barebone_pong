from Screen import Screen
from Paddle import Paddle
from Net import Net
from Ball import Ball
import constants

import time
import random
import math
import smbus

I2CADDR = 0x21
CHAN1 = 0x10
CHAN2 = 0x20
CHAN3 = 0x40
CHAN4 = 0x80

score1 = 0
score2 = 0

# Player 1
server = 1

end_time = 0.0
start_time = 0.0

def main():
    score1 = 0
    score2 = 0
    start_time = time.time()

    bus = smbus.SMBus(1)
    
    ## Graphics class
    screen = Screen(constants.WIDTH, constants.HEIGHT)

    player1 = Paddle(screen, 3, constants.HEIGHT/2-1, constants.BLACK)
    player2 = Paddle(screen, constants.WIDTH-4, constants.HEIGHT/2-1, constants.BLACK)

    net = Net(screen, constants.BLACK)

    ball = Ball(screen, 5, 20, constants.BALL_COLOUR)

    net.draw()
	
    screen.draw_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR)
    screen.draw_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR)

    # Dummy values
    ball.velocity = [10.0,10.0] #Roughly 8 seconds to cross screen?
    ball.served = True

    while (True):
        end_time = time.time()
        frame_time = end_time - start_time
        start_time = end_time

	value1 = read_i2c(CHAN1)
	value2 = read_i2c(CHAN4)

        # Lose condition
	if (ball.x >= screen.width-3):
            score1 += 1
            ball.served = False
            ball.x = player2.x-1
            ball.y = player2.y + player2.size[1]/2
            server = 2
            
	if (ball.x <= 3):
            score2 += 1
            ball.served = False
            ball.x = player1.x+1
            ball.y = player1.y + player1.size[1]/2
            server = 1
            
        score1 %= 10
        score2 %= 10

	# TODO: Reduce noise; multiple reads before move?
	player1.move(value1)
	player2.move(value2)

        player1.update(frame_time)
        player2.update(frame_time)

        # Collision Detection
        if (ball.roundx == player1.x + 1):
            if (ball.roundy >= player1.y and ball.roundy <= player1.y + player1.size[1]):
                # TODO: Actual trajectory stuff
                v = [1, ball.velocity[1]/ball.velocity[0]]
                r = random.randint(0, 2)
                
                tmp = ((8 + 3*r)**2)/2
                tmp = math.sqrt(tmp)
                v[0] *= tmp
                v[1] *= tmp
                

        if (ball.roundx == player2.x - 1):
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
    return = tmp1 >> 2



if (__name__ == '__main__'):
    main()
