from sys import exit as sysExit
import simple_chalk as chalk
import json

def getDistributionParameters():
	try:
		#using gaussian distribution for step lenghts, here it gets mu and sigma
		print('Using gaussian distribution as step len distribution.')
		mu = float(input('Insert mean parameter [mu]: '))
		sigma = float(input('Insert standard deviation parameter [sigma]: '))
		walkersNum = int(input('Number of walkers: '))
		_radius = float(input('Shape radius: '))
		if _radius < mu: sysExit('Please, make sure that radius < mu')
		_vertsNum = int(input('Shape vertices number: '))
		if _vertsNum < 3: sysExit('Vertices number cannot be less than 3')
		return mu, sigma, walkersNum, _radius, _vertsNum
	except: sysExit(chalk.bold.red('ERROR! ') + 'Invalid input parameters')

def readInputFile():
	with open('inputParameters.json', 'r') as inFile:
		data = inFile.read()
	try:
		data = json.loads(data)
		radius = float(data["shape"]["radius"])
		vertsNum = int(data["shape"]["vertices"])
		walkersNum = int(data["walker"]["number"])
		mu = float(data["walker"]["mu"])
		sigma = float(data["walker"]["sigma"])
	except: sysExit(chalk.bold.red('ERROR! ') + 'Invalid input parameters: check \'inputParameters.json\' file')
	if radius < mu: sysExit(chalk.bold.red('ERROR! ') + 'Please, make sure that radius < mu')
	if vertsNum < 3: sysExit(chalk.bold.red('ERROR! ') + 'Vertices number cannot be less than 3')
	return mu, sigma, walkersNum, radius, vertsNum