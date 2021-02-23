from matplotlib.colors import to_hex

def graphWalkers(allWalkersSteps, walkerDist, maxDist, walkPath):
	def getColor(maxDist, thisWalkerDist): #returns a hex code for path drawing color (with alpha channel)
		dimValue = thisWalkerDist / maxDist
		return to_hex([ 0.6, 0.6, 0.6, dimValue ], keep_alpha = True)

	#plotting each walker path
	for walk in range(len(allWalkersSteps)):
		col = getColor(maxDist, walkerDist[walk])
		walkPath.plot(allWalkersSteps[walk][0], allWalkersSteps[walk][1], color=col)

def graphHist(results, histPlot, mean, radius):
	histPlot.hist(results, bins=100, edgecolor='#212121', color='#e28743', alpha=0.9, density=True, range=(0, 3 * radius))
	histPlot.axvline(mean, color='#212121', label='$<L> = {:.3f}$'.format(mean))
	histPlot.legend()