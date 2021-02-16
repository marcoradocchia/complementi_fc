from math import pi, sin, cos, acos, sqrt
from random import randint, random

def getVerts(radius, vertsNum):
	angStep = 2 * pi / vertsNum
	verts = []
	for index in range(vertsNum):
		newVert = [radius * cos(index * angStep), radius * sin(index * angStep)]
		verts.append(newVert)
	verts.append([float(radius), 0.0])
	return verts

class Shape:
	def __init__(self, radius, vertsNum):
		self.rad = radius
		self.vertsNum = vertsNum
		self.verts = getVerts(radius, vertsNum)

	def calcArea(self):
		area = 0.
		for index in range(len(self.verts) - 1):
			area += self.verts[index][0] * self.verts[index + 1][1] - self.verts[index + 1][0] * self.verts[index][1]
		return area / 2

	def calcPerimeter(self):
		sideLen = sqrt((self.verts[1][0] - self.verts[0][0])**2 + (self.verts[1][1] - self.verts[0][1])**2)
		return self.vertsNum * sideLen

	def getStartingPos(self):
		startingSide = randint(0, self.vertsNum - 1)
		t = random()
		startingX = self.verts[startingSide][0] + t * (self.verts[startingSide + 1][0] - self.verts[startingSide][0])
		startingY = self.verts[startingSide][1] + t * (self.verts[startingSide + 1][1] - self.verts[startingSide][1])
		startingPos = [startingX, startingY]
		return startingPos