from src.shape import Shape
from src.walker import Walker
from matplotlib import pyplot as plt
from matplotlib import colors, rcParams, rc

def getDistributionParameters():
	try:
		inputMuSigma = input('Insert mu and sigma [mu, sigma]: ').split(', ')
		return float(inputMuSigma[0]), float(inputMuSigma[1])
	except:
		print('Error occoured')
		quit()

def getColor(maxDist, thisWalkerDist):
	return colors.to_hex([ 1 - thisWalkerDist / maxDist, 0.2, thisWalkerDist / maxDist, 0.8 ], keep_alpha = True)

def main(): #runs walkers and plots mapping walk length using alpha channel
	mu, sigma = getDistributionParameters()
	_, walkPath = plt.subplots(1,1)
	walkersNum = int(input('Number of walkers: '))
	myShape = Shape(radius=30, vertsNum=400)
	x = list(); y = list()
	for vert in myShape.verts:
		x.append(vert[0]); y.append(vert[1])
	walkPath.plot(x, y, color='BLACK')
	allWalkersSteps = list(); walkerDist = list(); walkerMoves = list()
	maxDist = 0
	for _ in range(walkersNum):
		x = list(); y = list()
		myWalker = Walker(shapeVerts=myShape.verts, startingPos=myShape.getStartingPos(), _mu=mu, _sigma=sigma)
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
		col = getColor(maxDist, walkerDist[walk])
		walkPath.plot(allWalkersSteps[walk][0], allWalkersSteps[walk][1], color=col)
		print('{})	Moves: {}	Distance: {}'.format(walk+1, walkerMoves[walk], walkerDist[walk]))


if __name__ == '__main__':
	plt.style.use('seaborn')
	rc('font',**{'family':'serif'})
	params = { 'figure.figsize': (10, 9) }
	plt.rcParams.update(params)
	main()
	plt.tight_layout()
	plt.show()