from math import sqrt
from simple_chalk import chalk

def getStats(results):
	_mean = 0.0; _stDev = 0.0
	for result in results: _mean += result
	_mean /= len(results)
	for result in results: _stDev += (result - _mean)**2
	_stDev = sqrt(_stDev / (len(results) - 1)) #corrected standard deviation
	print("{intro_text}\n{mean_text} {mean:.3f}\n{stDev_text} {stDev:.3f}".format(intro_text=chalk.bold.redBright('SIMULATION RESULTS'), mean_text=chalk.bold.yellowBright('Mean path length:'), mean=_mean, stDev_text=chalk.bold.blueBright('Standard deviation:'), stDev=_stDev))