from Screen import Screen

DASH = (1, 2)
COL = 40

class Net(object):
    def __init__(self, screen, colour):
        self._screen = screen
        self.colour = colour

    def draw(self):
        screen_height = self._screen.height

        y = DASH[1]+1
        while (y < screen_height):
            self._screen.draw_rect(COL, y, DASH, self.colour)
            y += DASH[1]*2

    def spot_draw(self, x, y):
        if (x != COL):
            return
        
        screen_height = self._screen.height

        drawy = DASH[1]+1
        while (drawy < screen_height):
            if (drawy == y or drawy == y-1):
                self._screen.draw_rect(COL, y, (1, 1), self.colour)
            drawy += DASH[1]*2
