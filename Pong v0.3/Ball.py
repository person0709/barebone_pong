

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
        
        # Top and bottom of screen collision
        if (self.y <= 0 || self.y >= self._screen.height):
            self.velocity[1] *= -1

        self._last_pos = [int(round(self.x)), int(round(self.y))]
        
        # Move ball
        self.x = self.velocity[0] * frame_time
        self.y = self.velocity[1] * frame_time

        if (self._last_pos != [int(round(self.x)), int(round(self.y))]):
            self._moved = True


    def draw(self):
        if (not self._moved):
            return

        self._screen.draw_rect(*self._last_pos, (1, 1), constants.BACKGROUND_COLOUR)
        self._screen.draw_rect(int(round(self.x)), int(round(self.y)), (1, 1), self.colour)
        self._moved = False
