def checkInside(point, segments): #USES EVEN-ODD RULE AND RETURNS TRUE IF THE POINT'S INSIDE, FALSE OTHERWISE
	x = point[0]
	y = point[1]
	j = len(segments) - 1
	c = False
	for i in range(len(segments)):
		if ((segments[i][1] > y) != (segments[j][1] > y)) and (x < segments[i][0] + (segments[j][0] - segments[i][0]) * (y - segments[i][1]) / (segments[j][1] - segments[i][1])):
			c = not c
		j = i
	return c

def intersect():
	pass