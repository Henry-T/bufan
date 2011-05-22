class ChessBoard:
	def __init__(self):
		self.SizeX = 9
		self.SizeY = 9
		
		self.data = []
		for i in range(0, self.SizeX): # Hard Code
			self.data.append([])
			for j in range(0, self.SizeY):
				self.data[i].append(0)	# 0´ú±í¿ÕÎ»
	