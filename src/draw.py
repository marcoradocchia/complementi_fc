from shape import Shape
from walker import Walker

def main():
	myShape = Shape(radius=5, vertsNum=4)
	myWalker = Walker(shapeVerts=myShape.verts, startingPos=myShape.getStartingPos())

	#GET RID IN THE FINAL VERSION
	with open('shape.dat', 'w+') as outFile:
		for vert in myShape.verts:
			outFile.write('{}, {}\n'.format(vert[0], vert[1]))
		outFile.write('\n')

		#walking starts
		outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
		myWalker.firstMove()
		while True: #walking looper
			outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
			myWalker.move()
			if not myWalker.checkInside():
				myWalker.getIntersection()
				outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
				break
		
		print('Moves: ', myWalker.moves)
		print('Length: ', myWalker.distance)

if __name__ == '__main__':
	main()