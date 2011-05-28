import MCreator

# ���̸��࣬������ӵ�ͼƬ��λ�ú�����
class Slot:
	def __init__(self, x, y, scaleX = 1, scaleY = 1):
		# 0-δ���� 1~7-��ɫ����
		self.X = x
		self.Y = y
		
		self.typeId = 0
		self.image = None
		self.scaleX = scaleX
		self.scaleY = scaleY
	
	def Destroy(self):
		if self.image:
			self.image.destroy()
			self.image = None
			
	def CanPick(self):
		if self.TypeId != 0:
			return 1;
		else:
			return 0;
	
	def SetType(self, typeId):
		self.typeId = typeId
		if self.image:
			self.image.destroy()
			self.image = None
			
		if self.typeId > 0:
			pathStr = "Bufan/res/world2d/bubs.txg|" + str(typeId)
			self.image =  MCreator.CreateImage(pathStr, self.X, self.Y, self.scaleX, self.scaleY)
			
	def GetType(self):
		return self.typeId
		
		
		
		