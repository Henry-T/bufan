# ÆåÅÌ¸¨ÖúÄ£¿é
def StrToMove(pointsStr):
	points = []
	for i in range(0, len(pointsStr)/2)
		points.append([])
		points[i].append(ord(removeStr[i * 2 , 1]))
		points[i].append(ord(removeStr[i * 2 + 1, 1]))
	
def StrToRemoves(removeStr):
	removes = []
	for i in range(0, len(removeStr)/4):
		removes.append([])
		for j in range(0, 4):
			removes[i].append(ord(removeStr[i * 4 + j, 1]))
	return removes
	
def TypesToStr(types):
	typesStr = ""
	for i in range(0, len(types)):
		typeStr.append(chr(types[i]))
	return typeStr
	
def PossToStr(poss):
	possStr = ""
	for i in range(0, poss):
		possStr.append(chr(poss[i]))
	