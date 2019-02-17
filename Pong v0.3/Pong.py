from Screen import Screen
from Paddle import Paddle
from Net import Net
from Ball import Ball
import constants

import time

score1 = 0
score2 = 0

end_time = 0.0
start_time = 0.0

def main():
    start_time = time.time()
    
    ## Graphics class
    screen = Screen(constants.WIDTH, constants.HEIGHT)

    player1 = Paddle(screen, 3, constants.HEIGHT/2-1, constants.BLACK)
    player2 = Paddle(screen, constants.WIDTH-4, constants.HEIGHT/2-1, constants.BLACK)

    net = Net(screen, constants.BLACK)

    ball = Ball(screen, 0, 0, constants.BALL_COLOUR)
    # Dummy values
    ball.velocity = [8.0,8.0] #Roughly 10 seconds to cross screen?
    ball._served = True


    while (True):
        end_time = time.time()
        frame_time = end_time - start_time
        start_time = end_time

        player1.update(frame_time)
        player2.update(frame_time)
        ball.update(frame_time)
    
        player1.draw()
        player2.draw()
        ball.draw()

        net.draw()

        screen.draw_num(*constants.SCORE1, score1, constants.SCORE_COLOUR)
        screen.draw_num(*constants.SCORE2, score2, constants.SCORE_COLOUR)




if (__name__ == '__main__'):
    main()
