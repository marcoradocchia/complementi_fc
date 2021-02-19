from src.shape import Shape
from src.walker import Walker
from src.hist import getBins
from matplotlib import pyplot as plt
from matplotlib import colors, rcParams, rc
from sys import exit as sysExit
from simple_chalk import chalk

def getDistributionParameters():
	try:
		#using gaussian distribution for step lenghts, here it gets mu and sigma
		print('Using gaussian distribution as step len distribution.')
		mu = float(input('Insert mean parameter [mu]: '))
		sigma = float(input('Insert standard deviation parameter [sigma]: '))
		walkersNum = int(input('Number of walkers: '))
		_radius = float(input('Shape radius: '))
		_vertsNum = int(input('Shape vertices number: '))
		if _vertsNum < 3:
			sysExit('Vertices number cannot be less than 3')
		return mu, sigma, walkersNum, _radius, _vertsNum
	except: sysExit('Error with input parameters')

def getColor(maxDist, thisWalkerDist):
	return colors.to_hex([ 1 - thisWalkerDist / maxDist, 0.2, thisWalkerDist / maxDist, 0.8 ], keep_alpha = True)

def main(): #runs walkers and plots mapping walk length using alpha channel
	#matplolib pyplot axes variables
	_, (walkPath, hist) = plt.subplots(1,2)

	#gets input parameters for walkers and shape
	mu, sigma, walkersNum, _radius, _vertsNum = getDistributionParameters()
	myShape = Shape(radius=_radius, vertsNum=_vertsNum) #initializing shape
	
	#plotting shape and walker paths
	x = list(); y = list()
	for vert in myShape.verts:
		x.append(vert[0]); y.append(vert[1])
	walkPath.plot(x, y, color='BLACK')
	#initializing data arrays
	allWalkersSteps = list(); walkerDist = list(); walkerMoves = list()
	maxDist = 0. #"longest distance recorded" variable
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

	#plotting each walker path
	for walk in range(len(allWalkersSteps)):
		col = getColor(maxDist, walkerDist[walk])
		walkPath.plot(allWalkersSteps[walk][0], allWalkersSteps[walk][1], color=col)
		print('{})	{}: {}	{}: {}'.format(chalk.bold.red(walk+1), chalk.bold.green('Moves'), walkerMoves[walk], chalk.bold.blue('Distance'), walkerDist[walk]))


if __name__ == '__main__':
	plt.style.use('seaborn')
	rc('font',**{'family':'serif'})
	# params = { 'figure.figsize': (10, 9) }
	# plt.rcParams.update(params)
	main() #main script
	plt.tight_layout()
	plt.show()