from src.shape import Shape
from src.walker import Walker

def runSim(_iterations, _rad, _verts):
	myShape = Shape(radius=_rad, vertsNum=_verts)
	results = list()
	for simNum in range(_iterations):
		if simNum % 5 == 0: print("Completamento: {percentage:.1f} %".format(percentage = simNum / _iterations * 100), end='\r')
		myWalker = Walker(shapeVerts=myShape.verts, startingPos=myShape.getStartingPos(), _mu=2, _sigma=0.5)
		myWalker.firstMove()
		while True:
			myWalker.move()
			if not myWalker.checkInside():
				myWalker.getIntersection()
				break
		results.append(myWalker.distance)
	return results, myShape.calcPerimeter(), myShape.calcArea()