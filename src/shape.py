from math import pi, sin, cos, acos
from random import randint, random

def getVerts(radius, vertsNum):
	angStep = 2 * pi / vertsNum
	verts = []
	for index in range(vertsNum):
		newVert = [radius * cos(index * angStep), radius * sin(index * angStep)]
		verts.append(newVert)
	verts.append([radius, 0])
	with open('shape.dat', 'w+') as shapeFile:
		for point in verts:
			shapeFile.write('{}, {}\n'.format(point[0], point[1]))
	return verts

class Shape:
	def __init__(self, radius, vertsNum):
		self.rad = radius
		self.vertsNum = vertsNum
		self.verts = getVerts(radius, vertsNum)

	def getStartingPos(self):
		startingSide = randint(0, self.vertsNum - 1)
		t = random()
		startingX = self.verts[startingSide][0] + t * (self.verts[startingSide + 1][0] - self.verts[startingSide][0])
		startingY = self.verts[startingSide][1] + t * (self.verts[startingSide + 1][1] - self.verts[startingSide][1])
		startingPos = [startingX, startingY]
		return startingPos