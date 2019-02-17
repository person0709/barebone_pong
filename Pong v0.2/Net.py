from Screen import Screen

DASH = (1, 2)
COL = 40

class Net(object):
    def __init__(self, screen, colour):
        self.screen = screen
        self.colour = colour

    def draw(self):
        screen_height = self.screen.height

        y = DASH[1]+1
        while (y < screen_height):
            self.screen.draw_rect(COL, y, DASH, self.colour)
            y += DASH[1]*2
