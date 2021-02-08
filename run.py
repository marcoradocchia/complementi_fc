from src.simulation import runSim
from math import sqrt

if __name__ == '__main__':
	results = runSim(10000)
	mean = 0
	stDev = 0
	for result in results: mean += result
	mean /= len(results)
	for result in results: stDev += (result - mean)**2
	stDev = sqrt(stDev / (len(results) - 1)) #corrected standard deviation
	print("Distanza media percorsa: {meanVal:.3f}\nDeviazione Standard Corretta: {stDevVal:.3f}".format(meanVal = mean, stDevVal = stDev))