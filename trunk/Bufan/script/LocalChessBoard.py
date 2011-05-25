import Slot
import random
import MCreator
import PathFinder
import AStarGrid
import Global

class LocalChessBoard:
	def __init__(self, x, y, rangeX, rangeY):
		# ���̳ߴ�
		self.SizeX = 9
		self.SizeY = 9
		self.SlotW = rangeX / self.SizeX
		self.SlotH = rangeY / self.SizeY
		# ����λ��
		self.X = x
		self.Y = y
		# ��ʼ�����̸�
		self.Slots = []
		self.EmptySlots = []
		for i in range(0, self.SizeX):
			self.Slots.append([])
			for j in range(0, self.SizeY):
				slot = Slot.Slot(self.X + i * self.SlotW, self.Y + j *self.SlotH, 1, 1)
				self.Slots[i].append(slot)
				self.EmptySlots.append([i, j])
		# ����̸�
		self.PickedSlot = None
		# ѡ�п�
		self.PickBox = None
		# �ȴ����̸�
		self.WaitSlots = []
		# �ϴλغϵ÷�
		self.lastScore = 0
		# ���ó�ʼ����
		self.RDPrepSlot(3)
		self.RDPutSlot()
	
		# ׼����һ��
		self.RDPrepSlot(3)
	
	# ����
	def Restart(self):
		del self.EmptySlots[:]
		del self.WaitSlots[:]
		for i in range(0, self.SizeX):
			for j in range(0, self.SizeY):
				self.Slots[i][j].SetType(0)
				self.EmptySlots.append([i, j])
		self.lastScore = 0
		self.HidePickBox()
		# ���ó�ʼ����
		self.RDPrepSlot(3)
		self.RDPutSlot()
		# ׼����һ��
		self.RDPrepSlot(3)
		
		
	# ����
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
		
	# ׼��N����ɫ���������
	def RDPrepSlot(self, num):
		for i in range(0, num):
			typeId = random.randint(1, 7)
			self.WaitSlots.append(typeId)
	
	# ����ڷ�׼������
	def RDPutSlot(self):
		# ���ݵȴ����ӵ���ɫ�б�������
		for i in range(0, len(self.WaitSlots)):
			id = random.randint(0, len(self.EmptySlots) - 1)
			x =  self.EmptySlots[id][0]
			y =  self.EmptySlots[id][1]
			self.Slots[x][y].SetType(self.WaitSlots[i])
			self.EmptySlots.remove([x, y])
		# ����б�
		del self.WaitSlots[:]
	
	# �������
	def Click(self, mx, my):
		# �жϵ����Χ
		if mx < self.X or my < self.Y or mx > self.X + self.SizeX * self.SlotW or my > self.Y + self.SizeY * self.SlotH:
			return
		# ���λ�û���
		sX = (mx - self.X) / self.SlotW % self.SizeX
		sY = (my - self.Y) / self.SlotH % self.SizeY
		print("���̸񱻵����"+ str(sX) + ","+str(sY))
		
		if self.PickedSlot:
			print("��ǰ��ѡ��")
			if self.Slots[sX][sY].CanPick() == 0:
				# �����ƶ�·��
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
					Global.API.show_msg("Ŀ��λ�ò��ɴ�")
					return 1
			else:
				# ���ѡ�����̸�...
				print("ѡ�б��")
				self.HidePickBox()
				self.PickedSlot = self.Slots[sX][sY]
				self.ShowPickBox()
		else:
			print("��ǰ��ѡ��")
			# ѡ�����̸�
			if self.Slots[sX][sY].CanPick() == 1:
				self.PickedSlot = self.Slots[sX][sY]
				self.ShowPickBox()
	
	# �ƶ�����
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
			
		
		# ����λ�Ƿ�С��3������Ǿ��˳�
		if len(self.EmptySlots) <= 3:
			return 0
		
		# ���Ӹ���
		if score == 0:
			self.RDPutSlot()
			self.RDPrepSlot(3)
			
		return 1
	
	# ���÷ֲ�����
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
		
		# �Ʒ�����
		# TODO ����ϴη�����0���������쳣
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
	
	# ȡ���ϴη���
	def GetLastScore(self):
		score = self.lastScore
		self.lastScore = 0
		return score
	
	# ��֤�����ٽ�
	def validDir(self, dX,  dY, x, y, typeId, vList):
		# ��鵱ǰ��
		sX = x + dX
		sY = y + dY
		if sX >= 0 and sX <self.SizeX and sY >= 0 and sY < self.SizeY and self.Slots[sX][sY].TypeId == typeId:
			vList.append([sX, sY])
			# �������
			return self.validDir(dX, dY, sX, sY, typeId, vList)
		else:
			return vList
	
	# ��ʾѡ��
	def ShowPickBox(self):
		self.PickBox = MCreator.CreateImage("Bufan/res/world2d/bubs.txg|PickBox",  self.PickedSlot.X, self.PickedSlot.Y, 1, 1)
	
	# ����ѡ��
	def HidePickBox(self):
		if self.PickBox:
			self.PickBox.destroy()
			self.PickBox  = None
	
	def GetSlotPos(self, slot):
		return [(slot.X - self.X) / self.SlotW, (slot.Y - self.Y)/self.SlotH]
		
		
		
	
	