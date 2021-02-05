from shape import Shape
from walker import Walker
from exitShape import *

def main():
	myShape = Shape(radius=5, vertsNum=6)
	startPos = myShape.getStartingPos()
	myWalker = Walker(startingPos=startPos)

	#GET RID IN THE FINAL VERSION
	with open('shape.dat', 'w+') as outFile:
		for vert in myShape.verts:
			outFile.write('{}, {}\n'.format(vert[0], vert[1]))
		outFile.write('\n')
		while True:
			outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
			myWalker.move()
			if not checkInside(myWalker.pos, myShape.verts): break
		intersect() #TODO: IMPLEMENT INTERSECT
		outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))


if __name__ == '__main__':
	main()