from math import pi, cos, sin
from random import uniform, normalvariate

def getStepLen():
	return normalvariate(mu=1, sigma=0.2)

def firstMove(): #TODO: IMPLEMENT FIRST MOVE
	length = getStepLen()
	return length

class Walker():
	def __init__(self, shapeVerts, startingPos):
		self.shapeVerts = shapeVerts
		self.pos = startingPos
		self.distance = firstMove()
		self.prevPos = None

	def move(self):
		self.prevPos = list(self.pos)
		direction = uniform(0, 2 * pi)
		length = getStepLen()
		self.pos[0] += length * cos(direction)
		self.pos[1] += length * sin(direction)
		self.distance += length

	def checkInside(self): #uses even-odd rule and returns true if the point's inside, false otherwise
		x = self.pos[0]
		y = self.pos[1]
		pts = self.shapeVerts
		j = len(self.shapeVerts) - 1
		isOut = False
		for i in range(len(pts)):
			if ((pts[i][1] > y) != (pts[j][1] > y)) and (x < pts[i][0] + (pts[j][0] - pts[i][0]) * (y - pts[i][1]) / (pts[j][1] - pts[i][1])):
				isOut = not isOut
			j = i
		return isOut

	def getIntersectionPoint(self): #working
		pts = self.shapeVerts
		x2 = self.pos[0]
		y2 = self.pos[1]
		x1 = self.prevPos[0]
		y1 = self.prevPos[1]
		for i in range(len(pts) - 1):
			x3 = pts[i][0]
			y3 = pts[i][1]
			x4 = pts[i + 1][0]
			y4 = pts[i + 1][1]
			t = ((x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)) / ((x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3))
			if t <= 1 and t >= 0:
				self.pos[0] = x1 + t * (x2 - x1)
				self.pos[1] = y1 + t * (y2 - y1)
				break