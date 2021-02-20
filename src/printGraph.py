from matplotlib.colors import to_hex

#**********utils**********
def getColor(maxDist, thisWalkerDist): #returns a hex code for path drawing color (with alpha channel)
	return to_hex([ 1 - thisWalkerDist / maxDist, 0.2, thisWalkerDist / maxDist, 0.5 ], keep_alpha = True)

def getBins(vals, binNumber): #returns bins array for histogram (maptplotlib) plotting
	minVal = min(vals)
	binDist = (max(vals) - minVal) / binNumber
	bins = list()
	for index in range(binNumber):
		bins.append(minVal + binDist * index)
	return bins

#**********main functions**********
def graphWalkers(allWalkersSteps, walkerDist, maxDist, walkPath):
	#plotting each walker path
	for walk in range(len(allWalkersSteps)):
		col = getColor(maxDist, walkerDist[walk])
		walkPath.plot(allWalkersSteps[walk][0], allWalkersSteps[walk][1], color=col)

def graphHist(results, histPlot):
	histPlot.hist(results, bins=getBins(vals=results, binNumber=100))