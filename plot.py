import math as m
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from math import pi, sqrt, exp

xm = 410.13
sigma = 113.80
A0 = 2.20

x = [[], []]
y = [[], []]

i = 0

with open('shape.dat','r') as inFile:
	for line in inFile:
		if line == '\n':
			i = 1
			continue
		point = line.split(', ')
		x[i].append(float(point[0]))
		y[i].append(float(point[1]))

fig, ax1 = plt.subplots(1,1)
ax1.grid(True)
ax1.plot(x[0], y[0], label='shape')
ax1.plot(x[1], y[1], label='walker')
ax1.legend()
plt.tight_layout()
plt.show()