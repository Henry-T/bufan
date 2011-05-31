import Slot
import random
import MCreator
import PathFinder
import AStarGrid
import Global
import Rectangle

class LocalChessBoard:
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
				slot = Slot.Slot(self.rect.X + i * self.SlotW, self.rect.Y + j *self.SlotH)
				self.Slots[i].append(slot)
				self.EmptySlots.append([i, j])
				
		self.PickedSlot = None
		self.PickBox = None
		
		self.WaitTypes = []
		
		self.Score = 0
		self.GameOver = 0
		
		self.RDPrepSlot(3)
		self.RDPutSlot()
		self.RDPrepSlot(3)
		
	def Restart(self):
		del self.EmptySlots[:]
		del self.WaitTypes[:]
		for i in range(0, self.BoardW):
			for j in range(0, self.BoardH):
				self.Slots[i][j].SetType(0)
				self.EmptySlots.append([i, j])
		self.Score = 0
		self.GameOver = 0
		self.HidePickBox()
		self.RDPrepSlot(3)
		self.RDPutSlot()
		self.RDPrepSlot(3)
		
	def Destroy(self):
		for i in range(0, self.BoardW):
			for j in range(0, self.BoardH):
				self.Slots[i][j].Destroy()
		del self.Slots[:]
		
		if self.PickedSlot:
			self.PickedSlot = None
		
		if self.PickBox:
			self.PickBox.destroy()
			self.PickBox = None
		
	def RDPrepSlot(self, num):
		for i in range(0, num):
			typeId = random.randint(1, 7)
			self.WaitTypes.append(typeId)
	
	def RDPutSlot(self):
		for i in range(0, len(self.WaitTypes)):
			id = random.randint(0, len(self.EmptySlots) - 1)
			x =  self.EmptySlots[id][0]
			y =  self.EmptySlots[id][1]
			self.Slots[x][y].SetType(self.WaitTypes[i])
			self.EmptySlots.remove([x, y])
		del self.WaitTypes[:]
	
	def Click(self, mx, my):
		slotPos = self.rect.GetSubGridPos(mx, my, self.SlotW, self.SlotH)
		if slotPos == None:
			return
		
		sX = slotPos[0]
		sY = slotPos[1]
		print("棋盘格被点击："+ str(sX) + ","+str(sY))
		
		if self.PickedSlot:
			if self.Slots[sX][sY].CanPick() == 0:
				if len(self.findPath(sX, sY)) > 0:
					if self.move(sX, sY)  == 0:
						return 0
				else:
					Global.API.show_msg("目标位置不可达")
					return 1
			else:
				self.HidePickBox()
				self.PickedSlot = self.Slots[sX][sY]
				self.ShowPickBox()
		else:
			if self.Slots[sX][sY].CanPick() == 1:
				self.PickedSlot = self.Slots[sX][sY]
				self.ShowPickBox()
	
	def findPath(self, x, y):
		pFinder = PathFinder.PathFinder()
		obsList = []
		for i in range(0, 9):
			obsList.append([])
			for j in range(0, 9):
				obsList.append([i, j])
		
		for i in self.EmptySlots:
			obsList.remove(i)
		aStarGrid = AStarGrid.AStarGrid(self.BoardW, self.BoardH, self.GetSlotPos(self.PickedSlot), [x, y], obsList)
		pFinder.SetGrid(aStarGrid)
		return pFinder.FindPath()		
	
	def move(self, dX, dY):
		self.Slots[dX][dY].SetType(self.PickedSlot.GetType())
		self.EmptySlots.remove([dX, dY])
		
		sX =  int((self.PickedSlot.X - self.rect.X) / self.SlotW )
		sY =  int((self.PickedSlot.Y - self.rect.Y) / self.SlotH)
		self.EmptySlots.append([sX, sY])
		self.PickedSlot.SetType(0)
		self.PickedSlot = None
		self.HidePickBox()
		
		self.checkLine(dX, dY)
		
		return 1
	
	# 检查得分并消除
	def checkLine(self, x, y):
		# 检查
		typeId = self.Slots[x][y].GetType()
		vLists = []
		for i in range(0, 4):
			vLists.append([])
			vLists[i].append([x, y])
		# 横
		vLists[0] = self.validDir( 1, 0, x, y, typeId, vLists[0])
		vLists[0] = self.validDir(-1, 0, x, y, typeId, vLists[0])
		# 纵
		vLists[1] = self.validDir( 0, 1, x, y, typeId, vLists[1])
		vLists[1] = self.validDir( 0,-1, x, y, typeId, vLists[1])
		# 经
		vLists[2] = self.validDir( 1, 1, x, y, typeId, vLists[2])
		vLists[2] = self.validDir(-1,-1, x, y, typeId, vLists[2])
		# 纬
		vLists[3] = self.validDir( 1,-1, x, y, typeId, vLists[3])
		vLists[3] = self.validDir(-1, 1, x, y, typeId, vLists[3])
		
		# 计分消除
		addScore =  0
		for i in range(0, 4):
			vCount = len(vLists[i])
			if vCount >= 5:
				addScore += vCount
				for j in range(0, vCount):
					pX = int(vLists[i][j][0])
					pY = int(vLists[i][j][1])
					self.Slots[pX][pY].SetType(0)
					self.EmptySlots.append([pX, pY])
		self.Score += addScore
		
		if addScore == 0:
			self.RDPutSlot()
			self.RDPrepSlot(3)
	
	def checkGameOver(self):
		if len(self.EmptySlots) <= 3:
			self.GameOver = 1
			return 1
		return 0
	
	# 验证有向临近
	def validDir(self, dX,  dY, x, y, typeId, vList):
		sX = x + dX
		sY = y + dY
		if sX >= 0 and sX <self.BoardW and sY >= 0 and sY < self.BoardH and self.Slots[sX][sY].GetType() == typeId:
			vList.append([sX, sY])
			return self.validDir(dX, dY, sX, sY, typeId, vList)
		else:
			return vList
	
	def ShowPickBox(self):
		self.PickBox = MCreator.CreateImage("Bufan/res/world2d/bubs.txg|PickBox",  self.PickedSlot.X, self.PickedSlot.Y, 1, 1, MCreator.SlotLayer)
	
	def HidePickBox(self):
		if self.PickBox:
			self.PickBox.destroy()
			self.PickBox  = None
	
	def GetSlotPos(self, slot):
		return [(slot.X - self.rect.X) / self.SlotW, (slot.Y - self.rect.Y)/self.SlotH]
		
		
		
	
	