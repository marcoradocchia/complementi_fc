from math import pi, cos, sin, sqrt
from random import uniform, normalvariate

class Walker():
	def __init__(self, shapeVerts, startingPos, _mu, _sigma):
		self.tolerance = 1e-5
		self.shapeVerts = shapeVerts
		self.pos = startingPos
		self.prevPos = None
		self.moveLen = None
		self.distance = 0
		self.moves = 0
		self.mu = _mu
		self.sigma = _sigma

	def getStepLen(self):
		while True: #can't accept negative values
			stepLen = normalvariate(mu=self.mu, sigma=self.sigma)
			if stepLen >= 0: return stepLen

	def getStepDirection(self):
		return uniform(0, 2 * pi)

	def firstMove(self):
		self.moveLen = self.getStepLen()
		startingPos = list(self.pos)
		while True:
			direction = uniform(0, 2 * pi)
			self.pos[0] += self.moveLen * cos(direction)
			self.pos[1] += self.moveLen * sin(direction)
			if self.checkInside():
				self.prevPos = list(self.pos)
				self.moves += 1
				return
			self.pos = list(startingPos)

	def move(self):
		self.prevPos = list(self.pos)
		direction = self.getStepDirection()
		self.moveLen = self.getStepLen()
		self.pos[0] += self.moveLen * cos(direction)
		self.pos[1] += self.moveLen * sin(direction)
		self.moves += 1

	def checkInside(self): #uses even-odd rule and returns true if the point's inside, false otherwise
		x = self.pos[0]
		y = self.pos[1]
		pts = self.shapeVerts
		j = len(pts) - 1
		isIn = False
		for i in range(len(pts)):
			if ((pts[i][1] > y) != (pts[j][1] > y)) and (x < pts[i][0] + (pts[j][0] - pts[i][0]) * (y - pts[i][1]) / (pts[j][1] - pts[i][1])):
				isIn = not isIn
				self.distance += self.moveLen
			j = i
		return isIn

	def getIntersection(self):
		pts = self.shapeVerts
		x1 = self.prevPos[0]
		y1 = self.prevPos[1]
		x2 = self.pos[0]
		y2 = self.pos[1]
		for i in range(len(pts) - 1):
			x3 = pts[i][0]
			y3 = pts[i][1]
			x4 = pts[i + 1][0]
			y4 = pts[i + 1][1]
			den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
			if den == 0: continue
			t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
			u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / den
			if t > self.tolerance and t < 1 - self.tolerance and u > self.tolerance and u < 1 - self.tolerance:
				x = x1 + t * (x2 - x1)
				y = y1 + t * (y2 - y1)
				self.pos = [x, y]
				exitingLen = sqrt((x - x1)**2 + (y - y1)**2)
				self.distance += exitingLen
				return