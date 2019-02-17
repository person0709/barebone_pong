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
        

    def clear(self):
        '''
        Move cursor to (0, 0), set background colour to black
        and print 80*40 spaces.
        '''
	self._port.write(ESCAPE + "?25l")

        s = self.move_cursor(0, 0)
	self._port.write(s)
	print(s)
	s = ''
        s += ESCAPE + constants.BACKGROUND
	self._port.write(s)
	print(s)
        for i in range(self.height):
	    s = ''
            for j in range(self.width):
                s += ' '

            self._port.write(s)

    def draw_rect(self, x, y, size, colour):
        '''
        Draw a filled rectangle at (x, y) of given size and colour.
        '''
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




    def drawScore(self, leftNum, rightNum):
	def drawZero():	
		self.drawBlanks(3,1)
		
		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)
		
		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)
		
		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)
		
		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

	def drawOne():
		self._port.write("\x1B[1C")
		for i in range(0,5):
			self.drawBlanks(1,1)
			self._port.write("\x1B[1B")
			self._port.write("\x1B[1D")

	def drawTwo():
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(3,1)

	def drawThree():
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

	def drawFour():
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

	def drawFive():
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

	def drawSix():
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
	
		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

	def drawSeven():
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

	def drawEight():
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

	def drawNine():
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(1,1)
		self._port.write("\x1B[1C")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[1D")
		self.drawBlanks(1,1)

		self._port.write("\x1B[1B")
		self._port.write("\x1B[3D")
		self.drawBlanks(3,1)
		

	self._port.write("\x1B[2;30H")
	if leftNum == 0:
		drawZero()

	elif leftNum == 1:
		drawOne()

	elif leftNum == 2:
		drawTwo()

	elif leftNum == 3:
		drawThree()

	elif leftNum == 4:
		drawFour()

	elif leftNum == 5:
		drawFive()

	elif leftNum == 6:
		drawSix()

	elif leftNum == 7:
		drawSeven()

	elif leftNum == 8:
		drawEight()

	elif leftNum == 9:
		drawNine()

	
	self._port.write("\x1B[2;49H")
	if rightNum == 0:
		drawZero()

	elif rightNum == 1:
		drawOne()

	elif rightNum == 2:
		drawTwo()

	elif rightNum == 3:
		drawThree()

	elif rightNum == 4:
		drawFour()

	elif rightNum == 5:
		drawFive()

	elif rightNum == 6:
		drawSix()

	elif rightNum == 7:
		drawSeven()

	elif rightNum == 8:
		drawEight()

	elif rightNum == 9:
		drawNine()

    def drawBlanks(self, num, colour):
	s = ""
	for i in range(0,num):
		s = s + " "
	
	if colour == 0:
		self._port.write("\x1B[0m")

	elif colour == 1:
		self._port.write("\x1B[40m")

	elif colour == 2:
		self._port.write("\x1B[44m")

	self._port.write(s)
	self._port.write("\x1B[0m")






























