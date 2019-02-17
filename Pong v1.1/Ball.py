import constants

class Ball(object):
    def __init__(self, screen, x, y, colour):
        self._screen = screen
        self.x = float(x)
        self.y = float(y)
        self.roundx = int(round(x))
        self.roundy = int(round(y))
        self.colour = colour

        self.last_pos = [0, 0]
        self._moved = True

        self.velocity = [0.0, 0.0]

        self.served = False


    def update(self, frame_time):
        if (not self.served):
            return

        self.last_pos = [int(round(self.x)), int(round(self.y))]
        # Move ball
        self.x += self.velocity[0] * frame_time
        self.y += self.velocity[1] * frame_time

        if (self.y > self._screen.height):
           self.y = self._screen.height
           self.velocity[1] *= -1

        elif (self.y < 0):
           self.y = 0
           self.velocity[1] *= -1

        self.roundx = int(round(self.x))
        self.roundy = int(round(self.y))
        
        if (self.last_pos != [self.roundx, self.roundy]):
            self._moved = True


    def draw(self):
        
        if (not self._moved):
            return

        self._screen.draw_rect(self.last_pos[0], self.last_pos[1], (1, 1), constants.BACKGROUND_COLOUR)

        self._screen.draw_rect(self.roundx, self.roundy, (1, 1), self.colour)
        self._moved = False

