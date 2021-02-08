from src.shape import Shape
from src.walker import Walker

def runSim(iterations):
	myShape = Shape(radius=5, vertsNum=4)
	results = list()
	for simNum in range(iterations):
		if simNum % 5 == 0: print("Completamento: {percentage:.1f} %".format(percentage = simNum / iterations * 100), end='\r')
		myWalker = Walker(shapeVerts=myShape.verts, startingPos=myShape.getStartingPos())
		myWalker.firstMove()
		while True:
			myWalker.move()
			if not myWalker.checkInside():
				myWalker.getIntersection()
				break
		results.append(myWalker.distance)
	return results