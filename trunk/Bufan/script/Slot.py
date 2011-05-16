import MCreator

class Slot:
	def __init__(self, x, y):
		# 0-未放置 1~7-各色棋子
		self.TypeId = 0 
		self.Image = None
		self.X = x
		self.Y = y
	
	def Destroy(self):
		if self.Image:
			self.Image.destroy()
			self.Image = None
			
	# 选择
	def CanPick(self):
		if self.TypeId != 0:
			return 1;
		else:
			return 0;
	
	# 设置棋盘格类型
	def SetType(self, typeId):
		self.TypeId = typeId
		# 清除棋子
		if self.Image:
			self.Image.destroy()
			self.Image = None
			
		if self.TypeId > 0:
			pathStr = "Bufan/res/world2d/bubs.txg|" + str(typeId)
			self.Image =  MCreator.CreateImage(pathStr, self.X, self.Y, 1, 1)
		
		
		
		