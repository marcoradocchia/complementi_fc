from sys import exit as sysExit

def getDistributionParameters():
	try:
		#using gaussian distribution for step lenghts, here it gets mu and sigma
		print('Using gaussian distribution as step len distribution.')
		mu = float(input('Insert mean parameter [mu]: '))
		sigma = float(input('Insert standard deviation parameter [sigma]: '))
		walkersNum = int(input('Number of walkers: '))
		_radius = float(input('Shape radius: '))
		if _radius < mu: sysExit('Please, make sure that radius < mu.')
		_vertsNum = int(input('Shape vertices number: '))
		if _vertsNum < 3:
			sysExit('Vertices number cannot be less than 3')
		return mu, sigma, walkersNum, _radius, _vertsNum
	except: sysExit('Error with input parameters')