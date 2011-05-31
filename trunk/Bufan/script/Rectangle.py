class Rectangle:
	def __init__(self, x, y, height, width):
		self.X = x
		self.Y = y
		self.Height = height
		self.Width = width

	def InRect(self, pX, pY):
		if pX < self.X or \
		   pY < self.Y or \
		   pX > self.X + self.Width or \
		   pY > self.Y + self.Height:
			return 0
		else:
			return 1
	
	def GetSubGridPos(self, pX, pY, gWidth, gHeight):
		if not self.InRect(pX, pY):
			return None
		sGridPos = []
		sGridPos.append((pX - self.X) / gWidth)
		sGridPos.append((pY - self.Y) / gHeight)
		return sGridPos