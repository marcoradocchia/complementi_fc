from math import pi, cos, sin
from random import uniform, normalvariate

def getStepLen():
	return normalvariate(mu=1, sigma=0.2)

def firstMove(): #TODO: IMPLEMENT FIRST MOVE
	length = getStepLen()
	return length

class Walker():
	def __init__(self, startingPos):
		self.pos = startingPos
		self.distance = firstMove()
		self.prevPos = None

	def move(self):
		self.prevPos = self.pos
		direction = uniform(0, 2 * pi)
		length = getStepLen()
		self.pos[0] += length * cos(direction)
		self.pos[1] += length * sin(direction)
		self.distance += length