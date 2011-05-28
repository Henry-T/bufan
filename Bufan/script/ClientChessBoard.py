import Slot
import random
import MCreator
import PathFinder
import AStarGrid
import Global
import Rectangle

class ClientChessBoard:
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
				slot = Slot.Slot(self.X + i * self.SlotW, self.Y + j *self.SlotH)
				self.Slots[i].append(slot)
				self.EmptySlots.append([i, j])
				
		self.PickedSlot = None
		self.PickBox = None
		
		self.WaitTpyes = []
		
		self.Score = 0
		self.NetState = "Idle" # WaitRemove/WaitMove/WaitPrep/WaitPut
		self.GameOver = 0
		
		self.RDPrepSlot(3)
		self.RDPutSlot()
		self.RDPrepSlot(3)
		
		# Wait状态族临时量
		self.WaitMove = None
		self.WaitRemove = None
		
	def Restart(self):
		del self.EmptySlots[:]
		del self.WaitTpyes[:]
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
		
	def OnNetPrepSlots(self, colors):
		self.WaitTypes = colors
		
	def OnNetMove(isOk):
		if isOk:
			lastId = len(self.WaitMove)-1
			dX = self.WaitMove[lastId][0]
			dY = self.WaitMove[lastId][1]
			self.move(dX, dY)
			
	def OnNetRemove(isOk):
		if isOk:
			for i in range(0, len(removes)):
				sX = removes[i][0]
				sY = removes[i][1]
				eX = removes[i][2]
				eY = removes[i][3]
				for x in range(	/
					MathHelper.GetSmall(sX, eX), /
					MathHelper.GetBig(sX, eX)):
					for y in range( /
						MathHelper.GetSmall(sY, eY), /
						MathHelper.GetBig(sY, eY)):
						self.Slots[x][y].SetType(0)
						self.EmptySlots.append([pX, pY])
			
	def OnNetPutSlots(self, poss):
		for i in range(0, len(self.WaitTypes)):
			self.Slots[poss[i][0]][poss[i][1]].SetType(self.WaitTypes[i])
		def self.WaitTypes[:]
	
	def Click(self, mx, my):
		slotPos = self.rect.GetSubGridPos(mx, my, self.SlotW, self.SlotH)
		if slotPos == None
			return
		
		sX = slotPos[0]
		sY = slotPos[1]
		print("棋盘格被点击："+ str(sX) + ","+str(sY))
		
		if self.PickedSlot:
			if self.Slots[sX][sY].CanPick() == 0:
				aStarPath = findPath()
				if len(aStarPath) > 0:
					self.WaitMove = aStarPath2Move(aStarPath)
					Global.Sender.cs_this_move(points=ChessHelper.MoveToStr(self.WaitMove))
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
	
	def findPath(x, y):
		pFinder = PathFinder.PathFinder()
		obsList = []
		for i in range(0, 9):
			obsList.append([])
			for j in range(0, 9):
				obsList.append([i, j])
		
		for i in self.EmptySlots:
			obsList.remove(i)
		aStarGrid = AStarGrid.AStarGrid(self.BoardW, self.BoardH, self.GetSlotPos(self.PickedSlot), [sX, sY], obsList)
		pFinder.SetGrid(aStarGrid)
		return pFinder.FindPath()		
	
	def aStarPath2Move(aStarPath):
		points = []
		for i in range(0, len(aStarPath)):
			points.append("[]")
			points.append(aStarPath[i].X)
			points.append(aStarPath[i].Y)
		return points
	
	# TODO 修改这个函数可增加动画效果
	def move(self, dX, dY):
		self.Slots[dX][dY].SetType(self.PickedSlot.TypeId)
		self.EmptySlots.remove([dX, dY])
		
		sX =  int((self.PickedSlot.X - self.X) / self.SlotW )
		sY =  int((self.PickedSlot.Y - self.Y) / self.SlotH)
		self.EmptySlots.append([sX, sY])
		self.PickedSlot.SetType(0)
		self.PickedSlot = None
		self.HidePickBox()
		
		self.checkLine(dX, dY)
			
		if score == 0:
			self.RDPutSlot()
			self.RDPrepSlot(3)
		return 1
	
	# 检查得分并消除
	def checkLine(self, x, y):
		# TODO 检查消除可能，并请求服务器
		# 检查
		typeId = self.Slots[x][y].TypeId
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
		lInfo = []
		for i in range(0, 4):
			vCount = len(vLists[i])
			if vCount >= 5:
				lInfo.append([])
				lInfo[i].append(vList[i][0][0])
				lInfo[i].append(vList[i][0][1])
				lInfo[i].append(vList[i][len(vList[i])-1][0])
				lInfo[i].append(vList[i][len(vList[i])-1][1])
				for j in range(0, vCount):
					pX = int(vLists[i][j][0])
					pY = int(vLists[i][j][1])
					self.Slots[pX][pY].SetType(0)
		if len(lInfo) > 0:
			Global.Sender.cs_this_remove(lineInfo=ChessHelper.RemovesToStr(lInfo))
	
	def checkGameOver(self):
		if len(self.EmptySlots) <= 3:
			self.GameOver = 1
			return 1
		return 0
	
	def validDir(self, dX,  dY, x, y, typeId, vList):
		sX = x + dX
		sY = y + dY
		if sX >= 0 and sX <self.BoardW and sY >= 0 and sY < self.BoardH and self.Slots[sX][sY].TypeId == typeId:
			vList.append([sX, sY])
			return self.validDir(dX, dY, sX, sY, typeId, vList)
		else:
			return vList
		
	def ShowPickBox(self):
		self.PickBox = MCreator.CreateImage("Bufan/res/world2d/bubs.txg|PickBox",  self.PickedSlot.X, self.PickedSlot.Y, 1, 1)
	
	def HidePickBox(self):
		if self.PickBox:
			self.PickBox.destroy()
			self.PickBox  = None
	
	def GetSlotPos(self, slot):
		return [(slot.X - self.X) / self.SlotW, (slot.Y - self.Y)/self.SlotH]
	
		
		
	
	