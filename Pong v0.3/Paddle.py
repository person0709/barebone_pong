from Screen import Screen
import constants

SIZE = (1, 3)
POWER_SIZE = (1, 6)
POWERUP = 1000

class Paddle(object):
    def __init__(self, screen, x, y, colour):
        self._screen = screen
        self.x = x
        self.y = y
        self.colour = colour

        self.size = SIZE

	self._last_y = 0
        self._moved = True

        self._power = 0


    def update(self, frame_time):
        self._power += frame_time
        if (self._power > POWERUP):
            self.size = SIZE

    def draw(self):
        if (not self._moved):
            return

        self._moved = False
        # Clear old paddle from screen
        self._screen.draw_rect(self.x, self._last_y, self.size, constants.BACKGROUND)
        # Draw new paddle at new position
        self._screen.draw_rect(self.x, self.y, self.size, self.colour)
        

    def move(self, value):
        self._last_y = self.y
        self.y = int(round((float(value) / 2047)*float(self._screen.height-self.size[1]+1)))

        if (self.y != self._last_y):
            self._moved = True

    def power_up(self):
        self.size = POWER_SIZE
        self._power = int(round(time.time()*1000))
