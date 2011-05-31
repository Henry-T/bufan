import Slot
import Rectangle
import MathHelper

class MirrorChessBoard:
	def __init__(self, x, y, sizeX, sizeY):
		self.rect = Rectangle.Rectangle(x, y, sizeX, sizeY)
		
		self.BoardW = 9
		self.BoardH = 9
		self.SlotW = self.rect.Width / self.BoardW
		self.SlotH = self.rect.Height / self.BoardH
		
		self.Slots = []
		self.EmptySlots = []
		for i in range(0, self.BoardW):
			self.Slots.append([])
			for j in range(0, self.BoardH):
				slot = Slot.Slot(self.rect.X + i * self.SlotW, self.rect.Y + j *self.SlotH, 0.6, 0.6)
				self.Slots[i].append(slot)
				self.EmptySlots.append([i, j])
				
		self.WaitTypes = []
		
		self.Score = 0
		self.GameOver = 0
		
	def Destroy(self):
		for i in range(0, self.BoardW):
			for j in range(0, self.BoardH):
				self.Slots[i][j].Destroy()
		del self.Slots[:]
		
	def OnNetPrepSlots(self, colors):
		self.WaitTypes = colors
	
	def OnNetMove(self, points):
		sP = points[0]
		eP = points[len(points)-1]
		self.Slots[eP[0]][eP[1]].SetType( \
			self.Slots[sP[0]][sP[1]].GetType())
		self.Slots[sP[0]][sP[1]].SetType(0)
	
	def OnNetRemove(self, removes):
		for i in range(0, len(removes)):
			sX = removes[i][0]
			sY = removes[i][1]
			eX = removes[i][2]
			eY = removes[i][3]
			for x in range(	\
				MathHelper.GetSmall(sX, eX), \
				MathHelper.GetBig(sX, eX)):
				for y in range( \
					MathHelper.GetSmall(sY, eY), \
					MathHelper.GetBig(sY, eY)):
					self.Slots[x][y].SetType(0)
	
	def OnNetPutSlots(self, poss):
		for i in range(0, len(self.WaitTypes)):
			self.Slots[poss[i][0]][poss[i][1]].SetType(self.WaitTypes[i])
		del self.WaitTypes[:]
	
	
	
	
	
	
	