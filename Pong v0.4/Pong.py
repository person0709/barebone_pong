from Screen import Screen
from Paddle import Paddle
from Net import Net
from Ball import Ball
import constants

import time
import smbus

I2CADDR = 0x21

score1 = 0
score2 = 0

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

    # Dummy values
    ball.velocity = [10.0,10.0] #Roughly 10 seconds to cross screen?
    ball._served = True

    while (True):
        end_time = time.time()
        frame_time = end_time - start_time
        start_time = end_time

        bus.write_byte( I2CADDR, 0x10 )
	tmp1 = bus.read_word_data( I2CADDR, 0x00 )
	tmp1 = ((tmp1 & 0xff00) >> 8) | ((tmp1 & 0x00ff) << 8)
	tmp1 = tmp1 & 0x0fff
	value1 = tmp1>>2

	bus.write_byte( I2CADDR, 0x80 )
	tmp2 = bus.read_word_data( I2CADDR, 0x00 )
	tmp2 = ((tmp2 & 0xff00) >> 8) | ((tmp2 & 0x00ff) << 8)
	tmp2 = tmp2 & 0x0fff
	value2 = tmp2>>2

	if (ball.x >= screen.width):
                score1 += 1
	if (ball.x <= 0):
                score2 += 1
	if (score1 > 9):
		score1 = 0
	if (score2 > 9):
		score2 = 0

	
	player1.move(value1)
	player2.move(value2)

        player1.update(frame_time)
        player2.update(frame_time)

        if (int(round(ball.x)) == int(round(player1.x))+1):
            if (int(round(ball.y)) >= int(round(player1.y)) and int(round(ball.y)) <= int(round(player1.y)) + 2):
                ball.velocity[0] *= -1

        if (int(round(ball.x)) == int(round(player2.x))-1):
            if (int(round(ball.y)) >= int(round(player2.y)) and int(round(ball.y)) <= int(round(player2.y)) + 2):
                ball.velocity[0] *= -1
        ball.update(frame_time)
    
        player1.draw()
        player2.draw()
        ball.draw()
	'''
        net.draw()
	
        screen.draw_num(constants.SCORE1[0], constants.SCORE1[1], score1, constants.SCORE_COLOUR)
        screen.draw_num(constants.SCORE2[0], constants.SCORE2[1], score2, constants.SCORE_COLOUR)
	'''

	time.sleep(0.01)



if (__name__ == '__main__'):
    main()
