import random
import Global
import MCreator
import Rectangle
import Slot
import PathFinder
import AStarGrid

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
		self.State = "WaitPrep" # WaitPrep/Idle/WaitMove/WaitClear/WaitPut
		self.firstTime = 1
		self.GameOver = 0
		
		self.RDPrepSlot(3)
		self.RDPutSlot()
		self.RDPrepSlot(3)
		
		# Wait״̬����ʱ��
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
		if self.State == "WaitPrep":
			self.WaitTypes = colors
			# TODO Ԥ��׼��״̬������
			if self.firstTime:
				self.State = "WaitPut"
			else:
				self.State = "Idle"
		
	def OnNetMove(isOk):
		if self.State == "WaitMove":
			if isOk:
				lastId = len(self.WaitMove)-1
				dX = self.WaitMove[lastId][0]
				dY = self.WaitMove[lastId][1]
				self.move(dX, dY)
				if not self.checkLine(dX, dY):
					self.State = "WaitPut"
			
		if score == 0:
			self.RDPutSlot()
			self.RDPrepSlot(3)
			else:
				print("�ƶ�����ʧ�ܣ����ӿ��ܴ����쳣")
				self.HidePickBox()
				self.PickedSlot = None
			
	def OnNetRemove(isOk):
		if isOK and self.State == "WaitClear":
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
			self.State = "Idle"
		# û������ʣ��ĳ�����Ʒ���� Server ��ҲҪ����Ӧ�Ĵ���
			
	def OnNetPutSlots(self, poss):
		if self.State == "WaitPut":
			for i in range(0, len(self.WaitTypes)):
				self.Slots[poss[i][0]][poss[i][1]].SetType(self.WaitTypes[i])
			del self.WaitTypes[:]
			self.State = "WaitPrep"
	
	def Click(self, mx, my):
		if not (self.State == "Idle")
			return
		slotPos = self.rect.GetSubGridPos(mx, my, self.SlotW, self.SlotH)
		if slotPos == None
			return
		sX = slotPos[0]
		sY = slotPos[1]
		
		if self.PickedSlot:
			if self.Slots[sX][sY].CanPick() == 0:
				aStarPath = findPath()
				if len(aStarPath) > 0:
					self.WaitMove = aStarPath2Move(aStarPath)
					Global.Sender.cs_this_move(points=ChessHelper.MoveToStr(self.WaitMove))
					self.State = "WaitMove";
				else:
					Global.API.show_msg("Ŀ��λ�ò��ɴ�")
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
	
	def move(self, dX, dY):
		self.Slots[dX][dY].SetType(self.PickedSlot.TypeId)
		self.EmptySlots.remove([dX, dY])
		
		sX =  int((self.PickedSlot.X - self.X) / self.SlotW )
		sY =  int((self.PickedSlot.Y - self.Y) / self.SlotH)
		self.EmptySlots.append([sX, sY])
		self.PickedSlot.SetType(0)
		self.PickedSlot = None
		self.HidePickBox()
		# TODO �޸�������������Ӷ���Ч��
	
	def checkLine(self, x, y):
		# ���
		typeId = self.Slots[x][y].TypeId
		vLists = []
		for i in range(0, 4):
			vLists.append([])
			vLists[i].append([x, y])
		# ��
		vLists[0] = self.validDir( 1, 0, x, y, typeId, vLists[0])
		vLists[0] = self.validDir(-1, 0, x, y, typeId, vLists[0])
		# ��
		vLists[1] = self.validDir( 0, 1, x, y, typeId, vLists[1])
		vLists[1] = self.validDir( 0,-1, x, y, typeId, vLists[1])
		# ��
		vLists[2] = self.validDir( 1, 1, x, y, typeId, vLists[2])
		vLists[2] = self.validDir(-1,-1, x, y, typeId, vLists[2])
		# γ
		vLists[3] = self.validDir( 1,-1, x, y, typeId, vLists[3])
		vLists[3] = self.validDir(-1, 1, x, y, typeId, vLists[3])
		
		# ����
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
			self.State = "WaitClear"
			
	
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
	
		
		
	
	