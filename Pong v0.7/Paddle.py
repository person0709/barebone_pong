from Screen import Screen
import constants

SIZE = (1, 3)
POWER_SIZE = (1, 6)
POWERUP = 3

class Paddle(object):
    def __init__(self, screen, x, y, colour):
        self._screen = screen
        self.x = x
        self.y = y
        self.colour = colour

        self.size = SIZE
	self.last_size = SIZE

	self._last_y = 0
        self._moved = True

        self._power = 0
	self._power_count = 0


    def update(self, frame_time):
        if (self._power > POWERUP):
	    return

        self._power += frame_time
        if (self._power > POWERUP):
            self.size = SIZE
	    self._move = True

    def draw(self):
        if (not self._moved):
            return

        self._moved = False
        # Clear old paddle from screen
        self._screen.draw_rect(self.x, self._last_y, self.last_size, constants.BACKGROUND_COLOUR)
        # Draw new paddle at new position
        self._screen.draw_rect(self.x, self.y, self.size, self.colour)
	
	self.last_size = self.size
        

    def move(self, value):
        self._last_y = self.y
        self.y = int(round((float(value) / 1023)*float(self._screen.height-self.size[1]+1)))

        if (self.y != self._last_y):
            self._moved = True

    def power_up(self):
	if (self._power < POWERUP or self._power_count > 1):
	    return
        self.size = POWER_SIZE
        self._power = 0
	self._power_count += 1
	self._moved = True
