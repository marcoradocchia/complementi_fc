from src.shape import Shape
from src.walker import Walker
from src.statsAnalysis import getStats
from src.getInput import getDistributionParameters
from src.printGraph import graphWalkers, graphHist
from matplotlib import pyplot as plt
from matplotlib import rcParams, rc
from simple_chalk import chalk

def main(walkPath): #runs walkers and plots mapping walk length using alpha channel
	#gets input parameters for walkers and shape
	mu, sigma, walkersNum, _radius, _vertsNum = getDistributionParameters()
	myShape = Shape(radius=_radius, vertsNum=_vertsNum) #initializing shape
	
	#plotting shape and walker paths
	x = list(); y = list()
	for vert in myShape.verts:
		x.append(vert[0]); y.append(vert[1])
	walkPath.plot(x, y, color='#212121')
	#initializing data arrays
	allWalkersSteps = list(); walkerDist = list()
	maxDist = 0.0 #"longest distance recorded" variable
	for index in range(walkersNum):
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
		allWalkersSteps.append([x, y]); walkerDist.append(myWalker.distance)
		if myWalker.distance > maxDist: maxDist = myWalker.distance
		print('{index}	{moves_text} {moves}	{distance_text} {distance}'.format(index=chalk.bold.redBright(index+1)+chalk.bold.redBright(')'), moves_text=chalk.bold.greenBright('Moves:'), moves=myWalker.moves, distance_text=chalk.bold.blueBright('Distance:'), distance=myWalker.distance))

	print("\n{intro_text}\n{area_text} {area:.3f}\n{perimeter_text} {perimeter:.3f}".format(intro_text=chalk.bold.redBright('=====================SHAPE DETAILS====================='), area_text=chalk.bold.magentaBright('Area:'), area=myShape.calcArea(), perimeter_text=chalk.bold.cyanBright('Perimeter:'), perimeter=myShape.calcPerimeter()))
	graphWalkers(allWalkersSteps, walkerDist, maxDist, walkPath)
	return walkerDist

if __name__ == '__main__':
	plt.style.use('seaborn')
	# rc('font',**{'family':'serif'})
	_, (walkPath, histPlot) = plt.subplots(1,2) # matplolib pyplot axes variables
	results = main(walkPath) # main script (returns array of walkers path lengths)
	graphHist(results, histPlot, getStats(results))
	plt.tight_layout(w_pad=1)
	plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode
	plt.subplots_adjust(left=0.03, bottom = 0.05, right=0.985, top=0.97, wspace=0.06) # adjusting spacings
	plt.show()