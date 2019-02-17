from serial import Serial
import time

serialPort = Serial("/dev/ttyAMA0", 115200)

if (serialPort.isOpen() == False):
	serialPort.open()

# Wait for character to be RX. Print ASCII value to Pi screen
# TX back RX character to remote terminal. If RX character is CR
# exit loop and close serial port.

class Pong(object):
	def __init__(self):
		self.serveCount = 0
		self.ballX = 0
		self.ballY = 0
		self.ballDirectionX=1
		self.ballDirectionY=1
		self.isOver = False
		self.playerLeft = Player()
		self.playerRight = Player()

	def reset(self):
		if (serveCount / 5) % 2 == 0
			self.ballX = 4
			self.ballY = 10
			self.ballDirectionX = 1
			self.ballDirectionY = 1
			self.serveCount += 1

		else:
			self.ballX = 76
			self.ballY = 10
			self.ballDirectionX = -1
			self.ballDirectionY = 1
			self.serveCount += 1

	def update(self):
		if (ballX < 80 and ballX > 0 and ballY < 20 and ballY > 0):
			ballX += ballDirectionX
			ballY += ballDirectionY

		if (ballX == 4):
			if (playerLeft.isHit(ballY + ballDirectionY)):
				self.ballDirectionX = 1
				self.ballDirectionY = self.ballDirectionY * -1

		if (ballX == 76):
			if (playerRight.isHit(ballY + ballDirectionY)):
				self.ballDirectionX = -1
				self.ballDirectionY = self.ballDirectionY * -1		

		if (ballX < 0):
			playerRight.setScore()
			self.reset()

		if (ballX > 80):
			playerLeft.setScore()
			self.reset()

class Player(object):
	def __init__(self):
		self.batY = 9
		self.batLength = 3
		self.boost = 3
		self.score = 0
		self.isWinner = False

	def getBoost(self):
		return self.boost

	def getScore(self):
		return self.score

	def setScore(self):
		self.score += 1

	def isWinner(self):
		return isWinner

	def useBoost(self):
		self.boost -= 1

	def isHit(self, yCoor):
		if (yCoor >= self.batY and yCoor <= self.batY + batLength):
			return True

		else:
			return False



def drawBlanks(num, colour):
	s = ""
	for i in range(0,num):
		s = s + " "
	
	if colour == 0:
		serialPort.write("\x1B[0m")

	elif colour == 1:
		serialPort.write("\x1B[40m")

	elif colour == 2:
		serialPort.write("\x1B[44m")

	serialPort.write(s)
	serialPort.write("\x1B[0m")

def drawBackground(colour):

	if colour == 0:
		serialPort.write("\x1B[0m")

	elif colour == 1:
		serialPort.write("\x1B[40m")

	elif colour == 2:
		serialPort.write("\x1B[44m")

	for i in range(0,20):	
		drawBlanks(80,colour)

	#drawing net	
	serialPort.write("\x1B[1;1H")

	serialPort.write("\x1B[40C") #move cursor to column 40
	
	for i in range(0,5):
		serialPort.write("\x1B[2B") #move cursor down 3 rows
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")#move cursor down 1 column
		serialPort.write("\x1B[1D")#move cursor backward 1 column
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")#move cursor down 1 column
		serialPort.write("\x1B[1D") #move cursor backward 1 column


	serialPort.write("\x1B[1;1H") #move cursor to origin

def drawScore(leftNum, rightNum):
	def drawZero():	
		drawBlanks(3,1)
		
		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)
		
		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)
		
		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)
		
		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

	def drawOne():
		serialPort.write("\x1B[1C")
		for i in range(0,5):
			drawBlanks(1,1)
			serialPort.write("\x1B[1B")
			serialPort.write("\x1B[1D")

	def drawTwo():
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(3,1)

	def drawThree():
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

	def drawFour():
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

	def drawFive():
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

	def drawSix():
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
	
		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

	def drawSeven():
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

	def drawEight():
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

	def drawNine():
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(1,1)
		serialPort.write("\x1B[1C")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")
		drawBlanks(1,1)

		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[3D")
		drawBlanks(3,1)
		

	serialPort.write("\x1B[2;30H")
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

	
	serialPort.write("\x1B[2;49H")
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


def drawBat(rowNumLeft, rowNumRight, isLeftPressed, isRightPressed):
	batLengthLeft = 3
	batLengthRight = 3

	if (isLeftPressed):
		batLengthLeft = 6;

	if (isRightPressed):
		batLengthRight = 6;

	s = "\x1B[" + str(rowNumLeft) +";3H"
	serialPort.write(s)
	for i in range(0,batLengthLeft):
		drawBlanks(1,1)
		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")


	s = "\x1B[" + str(rowNumRight) +";78H"
	serialPort.write(s)
	for i in range(0,batLengthRight):
		drawBlanks(1,1)
		serialPort.write("\x1B[1B")
		serialPort.write("\x1B[1D")


def drawBall(x, y):
	s = "\x1B[" + str(y) +";" + str(x) + "H"
	serialPort.write(s)

	drawBlanks(1,1)


def update():
	

isActive = True
serialPort.write("\x1B[4l") #Set insert mode

#while(isActive):
serialPort.write("\x1B[2J")
serialPort.write("\x1B[1;1H")

drawBackground(2)

drawScore(4,7)

drawBat(11, 15,False,False)

drawBall(50,10)

serialPort.close()
