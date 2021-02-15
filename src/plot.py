import math as m
import matplotlib.pyplot as plt
from math import pi, sqrt, exp

def plotSim():
	x = list()
	y = list()

	i = 0
	shapeLabel = 'shape'
	fig, ax1 = plt.subplots(1,1)
	with open('shape.dat','r') as inFile:
		for line in inFile:
			if line == '\n':
				if shapeLabel != None: ax1.plot(x, y, label='Shape')
				else: ax1.plot(x, y, color='ORANGE')
				i += 1
				shapeLabel = None
				x = list()
				y = list()
				continue
			point = line.split(', ')
			x.append(float(point[0]))
			y.append(float(point[1]))
		ax1.plot(x, y, color='ORANGE')

	# ax1.grid(True)
	ax1.legend()
	plt.tight_layout()
	plt.show()