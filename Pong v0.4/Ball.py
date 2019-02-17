import constants

class Ball(object):
    def __init__(self, screen, x, y, colour):
        self._screen = screen
        self.x = float(x)
        self.y = float(y)
        self.colour = colour

        self._last_pos = [0, 0]
        self._moved = True

        self._velocity = [0.0, 0.0]

        self._served = False


    def update(self, frame_time):
        if (not self._served):
            return

        self._last_pos = [int(round(self.x)), int(round(self.y))]
        # Move ball
        self.x += self.velocity[0] * frame_time
        self.y += self.velocity[1] * frame_time
        
        if (self.x > self._screen.width):
            self.x = self._screen.width
	    self.velocity[0] *= -1

        elif (self.x < 0):
            self.x = 0
            self.velocity[0] *= -1

        if (self.y > self._screen.height):
           self.y = self._screen.height
           self.velocity[1] *= -1

        elif (self.y < 0):
           self.y = 0
           self.velocity[1] *= -1

        
        if (self._last_pos != [int(round(self.x)), int(round(self.y))]):
            self._moved = True


    def draw(self, clear = True):
        
        if (not self._moved):
            return
	if (clear):
        	self._screen.draw_rect(self._last_pos[0], self._last_pos[1], (1, 1), constants.BACKGROUND_COLOUR)

        self._screen.draw_rect(int(round(self.x)), int(round(self.y)), (1, 1), self.colour)
        self._moved = False

