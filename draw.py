from src.shape import Shape
from src.walker import Walker
from src.plot import plotSim

def main():
	walkersNum = 500
	myShape = Shape(radius=31, vertsNum=4)

	#GET RID IN THE FINAL VERSION
	with open('shape.dat', 'w+') as outFile:
		for vert in myShape.verts:
			outFile.write('{}, {}\n'.format(vert[0], vert[1]))

		for index in range(walkersNum):
			myWalker = Walker(shapeVerts=myShape.verts, startingPos=myShape.getStartingPos(), _mu=5, _sigma=2)
			outFile.write('\n')
			# print('{:.2f} %'.format(index / walkersNum * 100), end='\r')
			#walking starts
			outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
			myWalker.firstMove()
			while True: #walking looper
				outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
				myWalker.move()
				if not myWalker.checkInside():
					myWalker.getIntersection()
					print(myWalker.distance)
					outFile.write('{}, {}\n'.format(myWalker.pos[0], myWalker.pos[1]))
					break
		
		# print('Moves: ', myWalker.moves)
		# print('Length: ', myWalker.distance)

if __name__ == '__main__':
	main()
	plotSim()