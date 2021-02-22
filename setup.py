from os import system
from sys import exit as sysExit

modules = [
	'matplotlib',
	'simple_chalk'
]

try:
	for module in modules:
		system('python -m pip install {}'.format(module))
except: sysExit('Error installing additional modules')