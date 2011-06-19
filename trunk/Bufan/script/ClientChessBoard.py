import Global
import MCreator
import Rectangle
import Slot
import PathFinder
import AStarGrid
import MathHelper
import ChessHelper

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
				slot = Slot.Slot(self.rect.X + i * self.SlotW, self.rect.Y + j *self.SlotH)
				self.Slots[i].append(slot)
				self.EmptySlots.append([i, j])
				
		self.PickedSlot = None
		self.PickBox = None
		
		self.WaitTpyes = []
		
		self.Score = 0
		self.State = "WaitPrep" # WaitPrep/Idle/WaitMove/WaitClear/WaitPut
		self.firstTime = 1
		self.GameOver = 0
		
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
		print("[客户端棋盘]准备棋子：颜色-"+str(colors)+"  状态-"+self.State)
		if self.State == "WaitPrep":
			self.WaitTypes = colors
			# TODO 预览准备状态的棋子
			if self.firstTime:
				self.State = "WaitPut"
				self.firstTime = 0
			else:
				self.State = "Idle"
		
	def OnNetMove(self, isOk):
		print("[客户端棋盘]移动棋子：确认-"+str(isOk)+"  状态-"+self.State)
		if self.State == "WaitMove":
			if isOk:
				lastId = len(self.WaitMove)-1
				sX = self.WaitMove[0][0]
				sY = self.WaitMove[0][1]
				dX = self.WaitMove[lastId][0]
				dY = self.WaitMove[lastId][1]
				tgtType = self.Slots[self.WaitMove[0][0]][self.WaitMove[0][1]].GetType()
				self.Slots[dX][dY].SetType(tgtType)
				self.Slots[sX][sY].SetType(0)
				self.EmptySlots.append([sX, sY])
				self.EmptySlots.remove([dX, dY])
				# 消除判定 - 这里修正了状态图
				lInfo = self.checkLine(dX, dY)
				if len(lInfo) > 0:
					self.WaitRemove = lInfo
					Global.Sender.cs_this_remove(lineInfo=ChessHelper.RemovesToStr(lInfo))
					self.State = "WaitClear"
				else:
					Global.Sender.cs_this_reqPut()
					self.State = "WaitPut"
			
		self.HidePickBox()
		self.PickedSlot = None
			
	def OnNetRemove(self, isOK):
		print("[客户端棋盘]消除棋子：确认-"+str(isOK)+"  状态-"+self.State)
		print("[客户端棋盘]消除任务："+str(self.WaitRemove))
		if isOK and self.State == "WaitClear":
			for i in range(0, len(self.WaitRemove)):
				sX = self.WaitRemove[i][0]
				sY = self.WaitRemove[i][1]
				eX = self.WaitRemove[i][2]
				eY = self.WaitRemove[i][3]
				if sX == eX:
					stepY = (-1, 1)[sY<eY]
					for y in range(sY, eY + stepY, stepY):
						self.Slots[sX][y].SetType(0)
						print("消除: "+str(sX)+"-"+str(y))
						self.EmptySlots.append([sX, y])
				elif sY == eY:
					stepX = (-1, 1)[sX<eX]
					for x in range(sX, eX + stepX, stepX):
						self.Slots[x][sY].SetType(0)
						print("消除: "+str(x)+"-"+str(sY))
						self.EmptySlots.append([x, sY])
				else:
					stepX = (-1, 1)[sX<eX]
					stepY = (-1, 1)[sY<eY]
					for i in range(0, abs(eX-sX)+1):
						self.Slots[sX + stepX * i][sY + stepY * i].SetType(0)
						print("消除: "+str(sX + stepX * i)+"-"+str(sY + stepY * i))
						self.EmptySlots.append([sX + stepX * i, sY + stepY * i])
			self.State = "Idle"
		# TODO 没有棋子剩余的超级人品奖励 Server 端也要做相应的处理
			
	def OnNetPutSlots(self, poss):
		print("[客户端棋盘]放置棋子：位置-"+str(poss)+"  状态-"+self.State)
		if self.State == "WaitPut":
			for i in range(0, len(self.WaitTypes)):
				self.Slots[poss[i][0]][poss[i][1]].SetType(self.WaitTypes[i])
				self.EmptySlots.remove([poss[i][0], poss[i][1]])
			del self.WaitTypes[:]
			self.State = "WaitPrep"
	
	def Click(self, mx, my):
		print("客户端棋盘点击：状态-"+str(self.State))
		if not (self.State == "Idle"):
			return
		slotPos = self.rect.GetSubGridPos(mx, my, self.SlotW, self.SlotH)
		if not slotPos:
			return
		sX = slotPos[0]
		sY = slotPos[1]
		
		if self.PickedSlot:
			if self.Slots[sX][sY].CanPick() == 0:
				aStarPath = self.findPath(sX, sY)
				if len(aStarPath) > 0:
					self.WaitMove = self.aStarPath2Move(aStarPath)
					Global.Sender.cs_this_move(points=ChessHelper.MoveToStr(self.WaitMove))
					self.State = "WaitMove";
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
			for j in range(0, 9):
				obsList.append([i, j])
		
		for i in range(0, len(self.EmptySlots)):
			obsList.remove(self.EmptySlots[i])
		aStarGrid = AStarGrid.AStarGrid(self.BoardW, self.BoardH, self.GetSlotPos(self.PickedSlot), [x, y], obsList)
		pFinder.SetGrid(aStarGrid)
		return pFinder.FindPath()		
	
	def aStarPath2Move(self, aStarPath):
		points = []
		for i in range(0, len(aStarPath)):
			points.append([])
			points[i].append(aStarPath[i].X)
			points[i].append(aStarPath[i].Y)
		return points
	
	def checkLine(self, x, y):
		# 检查
		typeId = self.Slots[x][y].GetType()
		vLists = []
		for i in range(0, 4):
			vLists.append([])
			vLists[i].append([x, y])
		# 横
		vLists[0] = self.validDir( 1, 0, x, y, typeId, vLists[0])
		vLists[0].reverse()
		vLists[0] = self.validDir(-1, 0, x, y, typeId, vLists[0])
		# 纵
		vLists[1] = self.validDir( 0, 1, x, y, typeId, vLists[1])
		vLists[1].reverse()
		vLists[1] = self.validDir( 0,-1, x, y, typeId, vLists[1])
		# 经
		vLists[2] = self.validDir( 1, 1, x, y, typeId, vLists[2])
		vLists[2].reverse()
		vLists[2] = self.validDir(-1,-1, x, y, typeId, vLists[2])
		# 纬
		vLists[3] = self.validDir( 1,-1, x, y, typeId, vLists[3])
		vLists[3].reverse()
		vLists[3] = self.validDir(-1, 1, x, y, typeId, vLists[3])
		
		# 消除
		lInfo = []
		for i in range(0, 4):
			vCount = len(vLists[i])
			if vCount >= 5:
				lInfo.append([])
				lInfo[len(lInfo)-1].append(vLists[i][0][0])
				lInfo[len(lInfo)-1].append(vLists[i][0][1])
				lInfo[len(lInfo)-1].append(vLists[i][len(vLists[i])-1][0])
				lInfo[len(lInfo)-1].append(vLists[i][len(vLists[i])-1][1])
		return lInfo
		
	def checkGameOver(self):
		if len(self.EmptySlots) <= 3:
			self.GameOver = 1
			return 1
		return 0
	
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
	
		
		
	
	