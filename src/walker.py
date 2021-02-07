from math import pi, cos, sin
from random import uniform, normalvariate

tolerance = 1e-5

def getStepLen():
	return normalvariate(mu=1, sigma=0.2)

def firstMove(walker, startingPos): #TODO: IMPLEMENT FIRST MOVE
	pass

class Walker():
	def __init__(self, shapeVerts, startingPos):
		self.shapeVerts = shapeVerts
		self.pos = startingPos
		self.distance = 0
		self.moves = 0
		self.prevPos = None

	def move(self):
		self.prevPos = list(self.pos)
		direction = uniform(0, 2 * pi)
		length = getStepLen()
		self.pos[0] += length * cos(direction)
		self.pos[1] += length * sin(direction)
		self.distance += length
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
			j = i
		return isIn

	def getIntersection(self): #not working properly with high number of vertices
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
			if t > tolerance and t < 1 - tolerance and u > tolerance and u < 1 - tolerance:
				x = x1 + t * (x2 - x1)
				y = y1 + t * (y2 - y1)
				self.pos = [x, y]
				print('INTERSECTION FOUND', i+1)
				return