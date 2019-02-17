from Screen import Screen
from Paddle import Paddle
from Net import Net
import constants

import time


## Graphics class
screen = Screen(constants.WIDTH, constants.HEIGHT)

player1 = Paddle(screen, 3, constants.HEIGHT/2-1, constants.BLACK)
player2 = Paddle(screen, constants.WIDTH-4, constants.HEIGHT/2-1, constants.BLACK)

net = Net(screen, constants.BLACK)

screen.clear()

player1.draw()
player2.draw()
net.draw()
screen.drawScore(5, 9)


time.sleep(2)

player1.move(1500)
player1.draw()
