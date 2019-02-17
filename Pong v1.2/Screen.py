from serial import Serial

## Colour constants
import constants

## Escape character
ESCAPE = '\x1B['

class Screen(object):
    '''
    Screen graphics class; handles all serial comms to draw
    graphics to the screen.
    '''
    def __init__(self, width, height, baud_rate = 115200):
        self._port = Serial("/dev/ttyAMA0", baud_rate)

        if (self._port.isOpen() == False):
            self._port.open()

        self.width = width
        self.height = height

        self.colour = constants.NET_COLOUR

	self._port.write("\x1B[4l")
        # Hide cursor
	self._port.write(ESCAPE + "?25l")
	# Clear screen
	self.clear()
        

    def clear(self):
        '''
        Move cursor to (0, 0), set background colour to black
        and print 80*40 spaces.
        '''
        s = self.move_cursor(0, 0)
        s += ESCAPE + constants.BACKGROUND_COLOUR
        for i in range(self.height):
            for j in range(self.width):
                s += ' '

        self._port.write(s)

    def draw_rect(self, x, y, size, colour):
        '''
        Draw a filled rectangle at (x, y) of given size and colour.
        '''
        s = ''
	'''
        # Only send new colour command if it's different
        if (self.colour != colour):
            s = ESCAPE + colour
            self.colour = colour'''
	s = ESCAPE + colour
            
        for i in range(size[1]):
            s += self.move_cursor(x, y)
            for j in range(size[0]):
                s += ' '
            y += 1
	
	self._port.write(s)

    def move_cursor(self, x, y):
        '''
        Return string containing escape sequence to move cursor
        to position (x, y). *NOTE* Does NOT transmit command.
        '''
        s = ESCAPE
        s += str(y) + ';' + str(x) + 'H'
        return s


    def draw_num(self, x, y, number, colour):
	if number >= len(constants.NUMBERS):
	    return
        for row in range(len(constants.NUMBERS[number])):
            for i in range(len(constants.NUMBERS[number][row])):
                if (constants.NUMBERS[number][row][i] > 0):
                    self.draw_rect(x+i, y+row, (1, 1), colour)
                else:
                    self.draw_rect(x+i, y+row, (1, 1), constants.BACKGROUND_COLOUR)

    def draw_str(self, x, y, s, colour):
        for char in s:
            for row in range(len(constants.CHARS[char])):
                for i in range(len(constants.CHARS[char][row])):
                    if (constants.CHARS[char][row][i] > 0):
                        self.draw_rect(x+i, y+row, (1, 1), colour)
                    else:
                        self.draw_rect(x+i, y+row, (1, 1), constants.BACKGROUND_COLOUR)
            x += 6
                    

    def spot_num(self, x, y, number, colour, spotx, spoty):
        if (spotx < x or spoty < y):
            return
        if (spotx > x + 2 or spoty > y + 4):
            return
        
        if (constants.NUMBERS[number][spoty-y][spotx-x] > 0):
            self.draw_rect(spotx, spoty, (1, 1), colour)
















        
