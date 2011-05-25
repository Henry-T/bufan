import Slot
import random
import MCreator
import PathFinder
import AStarGrid
import Global

class LocalChessBoard:
	def __init__(self, x, y, rangeX, rangeY):
		# 棋盘尺寸
		self.SizeX = 9
		self.SizeY = 9
		self.SlotW = rangeX / self.SizeX
		self.SlotH = rangeY / self.SizeY
		# 棋盘位置
		self.X = x
		self.Y = y
		# 初始化棋盘格
		self.Slots = []
		self.EmptySlots = []
		for i in range(0, self.SizeX):
			self.Slots.append([])
			for j in range(0, self.SizeY):
				slot = Slot.Slot(self.X + i * self.SlotW, self.Y + j *self.SlotH, 1, 1)
				self.Slots[i].append(slot)
				self.EmptySlots.append([i, j])
		# 活动棋盘格
		self.PickedSlot = None
		# 选中框
		self.PickBox = None
		# 等待棋盘格
		self.WaitSlots = []
		# 上次回合得分
		self.lastScore = 0
		# 放置初始棋子
		self.RDPrepSlot(3)
		self.RDPutSlot()
	
		# 准备下一轮
		self.RDPrepSlot(3)
	
	# 重来
	def Restart(self):
		del self.EmptySlots[:]
		del self.WaitSlots[:]
		for i in range(0, self.SizeX):
			for j in range(0, self.SizeY):
				self.Slots[i][j].SetType(0)
				self.EmptySlots.append([i, j])
		self.lastScore = 0
		self.HidePickBox()
		# 放置初始棋子
		self.RDPrepSlot(3)
		self.RDPutSlot()
		# 准备下一轮
		self.RDPrepSlot(3)
		
		
	# 清理
	def Destroy(self):
		for i in range(0, self.SizeX):
			for j in range(0, self.SizeY):
				self.Slots[i][j].Destroy()
		del self.Slots[:]
		
		if self.PickedSlot:
			self.PickedSlot = None
		
		if self.PickBox:
			self.PickBox.destroy()
			self.PickBox = None
		
	# 准备N个颜色随机的棋子
	def RDPrepSlot(self, num):
		for i in range(0, num):
			typeId = random.randint(1, 7)
			self.WaitSlots.append(typeId)
	
	# 随机摆放准备棋子
	def RDPutSlot(self):
		# 根据等待棋子的颜色列表创建棋子
		for i in range(0, len(self.WaitSlots)):
			id = random.randint(0, len(self.EmptySlots) - 1)
			x =  self.EmptySlots[id][0]
			y =  self.EmptySlots[id][1]
			self.Slots[x][y].SetType(self.WaitSlots[i])
			self.EmptySlots.remove([x, y])
		# 清空列表
		del self.WaitSlots[:]
	
	# 点击棋盘
	def Click(self, mx, my):
		# 判断点击范围
		if mx < self.X or my < self.Y or mx > self.X + self.SizeX * self.SlotW or my > self.Y + self.SizeY * self.SlotH:
			return
		# 点击位置换算
		sX = (mx - self.X) / self.SlotW % self.SizeX
		sY = (my - self.Y) / self.SlotH % self.SizeY
		print("棋盘格被点击："+ str(sX) + ","+str(sY))
		
		if self.PickedSlot:
			print("当前有选中")
			if self.Slots[sX][sY].CanPick() == 0:
				# 测试移动路径
				pFinder = PathFinder.PathFinder()
				obsList = []
				for i in range(0, self.SizeX):
					obsList.append([])
					for j in range(0, self.SizeY):
						obsList.append([i, j])
				
				for i in self.EmptySlots:
					obsList.remove(i)
				aStarGrid = AStarGrid.AStarGrid(self.SizeX, self.SizeY, self.GetSlotPos(self.PickedSlot), [sX, sY], obsList)
				pFinder.SetGrid(aStarGrid)
				if len(pFinder.FindPath()) > 0:
					if self.move(sX, sY)  == 0:
						return 0
				else:
					Global.API.show_msg("目标位置不可达")
					return 1
			else:
				# 变更选中棋盘格...
				print("选中变更")
				self.HidePickBox()
				self.PickedSlot = self.Slots[sX][sY]
				self.ShowPickBox()
		else:
			print("当前无选中")
			# 选中棋盘格
			if self.Slots[sX][sY].CanPick() == 1:
				self.PickedSlot = self.Slots[sX][sY]
				self.ShowPickBox()
	
	# 移动棋子
	def move(self, dX, dY):
		self.Slots[dX][dY].SetType(self.PickedSlot.TypeId)
		self.EmptySlots.remove([dX, dY])
		
		sX =  int((self.PickedSlot.X - self.X) / self.SlotW )
		sY =  int((self.PickedSlot.Y - self.Y) / self.SlotH)
		self.EmptySlots.append([sX, sY])
		self.PickedSlot.SetType(0)
		self.PickedSlot = None
		
		self.HidePickBox()
		
		score = self.checkLine(dX, dY)
			
		
		# 检查空位是否小于3，如果是就退出
		if len(self.EmptySlots) <= 3:
			return 0
		
		# 棋子更新
		if score == 0:
			self.RDPutSlot()
			self.RDPrepSlot(3)
			
		return 1
	
	# 检查得分并消除
	def checkLine(self, x, y):
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
		# TODO 如果上次分数非0，可以抛异常
		self.lastScore =  0
		for i in range(0, 4):
			vCount = len(vLists[i])
			if vCount >= 5:
				self.lastScore += vCount
				for j in range(0, vCount):
					pX = int(vLists[i][j][0])
					pY = int(vLists[i][j][1])
					self.Slots[pX][pY].SetType(0)
					self.EmptySlots.append([pX, pY])
					
		return self.lastScore
	
	# 取走上次分数
	def GetLastScore(self):
		score = self.lastScore
		self.lastScore = 0
		return score
	
	# 验证又向临近
	def validDir(self, dX,  dY, x, y, typeId, vList):
		# 检查当前格
		sX = x + dX
		sY = y + dY
		if sX >= 0 and sX <self.SizeX and sY >= 0 and sY < self.SizeY and self.Slots[sX][sY].TypeId == typeId:
			vList.append([sX, sY])
			# 继续检查
			return self.validDir(dX, dY, sX, sY, typeId, vList)
		else:
			return vList
	
	# 显示选框
	def ShowPickBox(self):
		self.PickBox = MCreator.CreateImage("Bufan/res/world2d/bubs.txg|PickBox",  self.PickedSlot.X, self.PickedSlot.Y, 1, 1)
	
	# 隐藏选框
	def HidePickBox(self):
		if self.PickBox:
			self.PickBox.destroy()
			self.PickBox  = None
	
	def GetSlotPos(self, slot):
		return [(slot.X - self.X) / self.SlotW, (slot.Y - self.Y)/self.SlotH]
		
		
		
	
	