from Screen import Screen

DASH = (1, 2)
COL = 40

class Net(object):
    def __init__(self, screen, colour):
        self.screen = screen
        self.colour = colour

    def draw(self):
        screen_height = self.screen.height

        y = DASH[1]
        while (y < screen_height-2):
            self.screen.draw(COL, y, DASH, self.colour)
            y += DASH[1]*2
