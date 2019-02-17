from serial import Serial
import time

serialPort = Serial("/dev/ttyAMA0", 115200)

if (serialPort.isOpen() == False):
	serialPort.open()

class Pong(object):
	
	def __init__(self, screenWidth, screenHeight):
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight
		self.tickCount = 0.0
		self.serveCount = 0
		self.ballX = 0
		self.ballY = 0
		self.ballDirectionX = 1
		self.ballDirectionY = 1
		self.ballSpeed = 1
		self.isActive = True
		self.isServing = True
		self.playerLeft = Player()
		self.playerRight = Player()	

	def isActive(self):
		return self.isActive

	def readyServe(self):
		if ((self.serveCount / 5) % 2 == 0):
			self.ballX = 4
			self.ballY = self.playerLeft.getBatY
			self.ballDirectionX = 1
			self.ballDirectionY = 1

		else:
			self.ballX = 76
			self.ballY = playerRight.getBatY
			self.ballDirectionX = -1
			self.ballDirectionY = 1
			
	def serve(self):
		self.serveCount += 1
		self.isServing = False

	def update(self, delta):
		if (self.isServing):
			self.readyServe()
			return
	
	
		tickCount += delta
		if (self.tickCount < 0.1 / self.speed):
			return
			
		else:
			self.tickCount = 0

	
		if (self.playerLeft.isBoost):
			if (self.playerLeft.boostTimer > 15.0):
				self.playerLeft.disableBoost
		
		
		if (ballX < screenWidth and ballX > 0 and ballY < screenHeight and ballY > 0):
			self.ballX += self.ballDirectionX
			self.ballY += self.ballDirectionY

		if (ballX == 4):
			if (playerLeft.isHit(ballY)):
				self.ballDirectionX = 1
				self.ballDirectionY = self.ballDirectionY * -1

		elif (ballX == screenWidth - 4):
			if (playerRight.isHit(ballY)):
				self.ballDirectionX = -1
				self.ballDirectionY = self.ballDirectionY * -1		

		elif (self.ballX < 0):
			self.playerRight.setScore()
			if (self.playerRight.getScore() == 10):
				self.playerRight.setWinner()
				self.isActive = False
				return
			isServing = True

		elif (self.ballX > self.screenWidth):
			playerLeft.setScore()
			if (playerLeft.getScore() == 10):
				playerLeft.setWinner()
				isActive = False
				return
			isServing = True
			
		if (ballY == 0 or ballY == screenHeight):
			self.ballDirectionY * -1

class Player(object):
	def __init__(self):
		self.batY = 9
		self.batLength = 3
		self.boost = 2
		self.score = 0
		self.isWinner = False
		self.isBoost = False
		self.boostTimer = 0.0
		
	def setBatY(self, y):
                batY = y
				
	def getBatY(self):
		return batY

	def getBoost(self):
		return boost

	def getScore(self):
		return score

	def setScore(self):
		score += 1

	def isWinner(self):
		return isWinner
		
	def setWinner(self):
		isWinner = True

	def useBoost(self):
                if (boost <= 0):
                        boost -= 1
                        batLength = 6
                        isBoost = True
                else:
                        return

        def disableBoost(self):
                batLength = 3
                isBoost = false
		boostTimer = 0.0
		

	def isHit(self, yCoor):
		if (yCoor >= batY - batLength / 3 and yCoor <= batY + batLength / 3):
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


def drawBat(rowNumLeft, rowNumRight):
	batLengthLeft = 3
	batLengthRight = 3

	s = "\x1B[" + str(rowNumLeft) +";3H"
	serialPort.write(s)
	for i in range(0, batLengthLeft):
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

pongGame = Pong(80,20)
serialPort.write("\x1B[4l") #Set insert mode

delta = 0.0
#while(Pong.isActive):
serialPort.write("\x1B[2J") #Clear screen
serialPort.write("\x1B[0;0H") #Move cursor to origin

pongGame.update(delta)

drawBackground(2)

drawScore(5, 3)

drawBat(6, 5)

drawBall(30, 10)

delta = time.time() - delta

serialPort.close()
