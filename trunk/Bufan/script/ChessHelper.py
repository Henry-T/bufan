# ÆåÅÌ¸¨ÖúÄ£¿é
def StrToMove(pointsStr):
	points = []
	for i in range(0, len(pointsStr)/2):
		points.append([])
		points[i].append(ord(pointsStr[i * 2]))
		points[i].append(ord(pointsStr[i * 2 + 1]))
	return points

def MoveToStr(points):
	pointsStr = ""
	for i in range(0, len(points)):
		pointsStr += chr(points[i][0])
		pointsStr += chr(points[i][1])
	return pointsStr

def StrToRemoves(removeStr):
	removes = []
	for i in range(0, len(removeStr)/4):
		removes.append([])
		for j in range(0, 4):
			removes[i].append(ord(removeStr[i * 4 + j]))
	return removes
	
def RemovesToStr(removes):
	removesStr = ""
	for i in range(0, len(removes)):
		for j in range(0, 4):
			removesStr += chr(removes[i][j])
	return removesStr
		
def StrToColors(colorStr):
	colors = []
	for i in range(0, len(colorStr)):
		colors.append(int(ord(colorStr[i])))
	return colors
	
def StrToPoss(posStr):
	poss = []
	for i in range(0, len(posStr) / 2):
		poss.append([])
		poss[i].append(int(ord(posStr[i * 2])))
		poss[i].append(int(ord(posStr[i * 2 + 1])))
	return poss

	