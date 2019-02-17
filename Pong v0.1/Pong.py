from Screen import Screen
from Paddle import Paddle
from Net import Net
import constants

import time


def main():
    ## Graphics class
    screen = Screen(constants.WDITH, constants.HEIGHT)
    
    player1 = Paddle(screen, 3, constants.HEIGHT/2-1, constants.BLUE)
    player2 = Paddle(screen, constants.WDITH-4, constants.HEIGHT/2-1, constants.BLUE)

    net = Net(screen, constants.BLACK)

    sceen.clear()

    player1.draw()
    player2.draw()
    net.draw()





if __name__=='__main__':
    main()
