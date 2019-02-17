import time

from Screen import Screen

SIZE = (1, 3)
POWER_SIZE = (1, 6)
POWERUP = 1000

class Paddle(object):
    def __init__(self, screen, x, y, colour):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = colour

        self.size = SIZE

        self._moved = True

        self._power = 0


    def update(self):
        if (int(round(time.time()*1000)) - self._power > POWERUP):
            self.size = SIZE

    def draw(self):
        if (not self._moved):
            return

        self._moved = False
        # Clear old paddle from screen
        self.screen.draw_rect(self.x, self._last_y, self.size, constants.BACKGROUND)
        # Draw new paddle at new position
        self.screen.draw_rect(self.x, self.y, self.size, self.colour)
        

    def move(self, value):
        self._last_y = self.y
        self.y = (value / 2047)*(self.screen.height-self.size[1])
        if (self.y != self._last_y)
            self._moved = True

    def power_up(self):
        self.size = POWER_SIZE
        self._power = int(round(time.time()*1000))
