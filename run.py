from src.simulation import runSim
from math import sqrt
from matplotlib import pyplot as plt

def getBins(vals, binNumber):
	minVal = min(vals)
	binDist = (max(vals) - minVal) / binNumber
	bins = list()
	for index in range(binNumber):
		bins.append(minVal + binDist * index)
	return bins

if __name__ == '__main__':
	results = runSim(_iterations=1000, _rad=31, _verts=600) #rad is expressed in micrometer
	mean = 0
	stDev = 0
	for result in results: mean += result
	mean /= len(results)
	for result in results: stDev += (result - mean)**2
	stDev = sqrt(stDev / (len(results) - 1)) #corrected standard deviation
	print("Distanza media percorsa: {meanVal:.3f}\nDeviazione Standard Corretta: {stDevVal:.3f}".format(meanVal = mean, stDevVal = stDev))
	fig,ax = plt.subplots(1,1)
	ax.hist(results, bins=getBins(vals=results, binNumber=100))
	plt.show()