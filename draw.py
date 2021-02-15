from src.shape import Shape
from src.walker import Walker
from src.plot import plotSim
from matplotlib import pyplot as plt
from matplotlib import colors

def mainUsingFile():
	walkersNum = 500
	myShape = Shape(radius=31, vertsNum=4)
	#GET RID IN THE FINAL VERSION
	with open('shape.dat', 'w+') as outFile:
		for vert in myShape.verts:
			outFile.write('{}, {}\n'.format(vert[0], vert[1]))
		for index in range(walkersNum):
			myWalker = Walker(shapeVerts=myShape.verts, startingPos=myShape.getStartingPos(), _mu=5, _sigma=0.1)
			outFile.write('\n')
			#walking starts
			outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
			myWalker.firstMove()
			while True: #walking looper
				outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
				myWalker.move()
				if not myWalker.checkInside():
					myWalker.getIntersection()
					# print('{})	Moves: {}	Distance: {}'.format(index+1, myWalker.moves, myWalker.distance))
					if myWalker.distance <= 0: print(myWalker.distance)
					outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
					break
		plotSim()

def getColor(maxDist, thisWalkerDist):
	return colors.to_hex([ 1, 0.1, 0.1, thisWalkerDist / maxDist ], keep_alpha = True)

def main(): #runs walkers and plots mapping walk length using alpha channel
	fig, ax = plt.subplots(1,1)
	walkersNum = 1000
	myShape = Shape(radius=31, vertsNum=500)
	x = list(); y = list()
	for vert in myShape.verts:
		x.append(vert[0]); y.append(vert[1])
	ax.plot(x, y)
	allWalkersSteps = list(); walkerDist = list(); walkerMoves = list()
	maxDist = 0
	for index in range(walkersNum):
		x = list(); y = list()
		myWalker = Walker(shapeVerts=myShape.verts, startingPos=myShape.getStartingPos(), _mu=5, _sigma=0.1)
		x.append(myWalker.pos[0]); y.append(myWalker.pos[1])
		myWalker.firstMove()
		while True: #walking looper
			x.append(myWalker.pos[0]); y.append(myWalker.pos[1])
			myWalker.move()
			if not myWalker.checkInside():
				myWalker.getIntersection()
				x.append(myWalker.pos[0]); y.append(myWalker.pos[1])
				break
		allWalkersSteps.append([x, y]); walkerDist.append(myWalker.distance); walkerMoves.append(myWalker.moves)
		if myWalker.distance > maxDist: maxDist = myWalker.distance
	for walk in range(len(allWalkersSteps)):
		coloralpha = getColor(maxDist, walkerDist[walk])
		ax.plot(allWalkersSteps[walk][0], allWalkersSteps[walk][1], color=coloralpha)
		# print(walkerDist[walk], maxDist, walkerDist[walk] / maxDist)
		print('{})	Moves: {}	Distance: {}	Alpha: {}'.format(walk+1, walkerMoves[walk], walkerDist[walk], coloralpha))
	plt.show()



if __name__ == '__main__':
	# mainUsingFile()
	main()