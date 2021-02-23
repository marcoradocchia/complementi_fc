from matplotlib.colors import to_hex

def graphWalkers(allWalkersSteps, walkerDist, maxDist, walkPath):
	def getColor(maxDist, thisWalkerDist): #returns a hex code for path drawing color (with alpha channel)
		dimValue = thisWalkerDist / maxDist
		return to_hex([ 0.6, 0.6, 0.6, dimValue ], keep_alpha = True)

	#plotting each walker path
	for walk in range(len(allWalkersSteps)):
		col = getColor(maxDist, walkerDist[walk])
		walkPath.plot(allWalkersSteps[walk][0], allWalkersSteps[walk][1], color=col)

def graphHist(results, histPlot, mean):
	histPlot.hist(results, bins=100, edgecolor='black', density=True)
	histPlot.axvline(mean, color='red', label='Mean Path Length')
	
#TODO: ajust "range" argument in hist