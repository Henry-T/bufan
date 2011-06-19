import random
import Global
import MathHelper
import ChessHelper

class ServerChessBoard:
	def __init__(self, player):
		self.Player = player
		self.BoardW = 9
		self.BoardH = 9
		self.SlotTypes = []
		self.EmptySlots = []
		
		for i in range(0, self.BoardW): 
			self.SlotTypes.append([])
			for j in range(0, self.BoardH):
				self.SlotTypes[i].append(0)	# 0�����λ 1-7�������
				self.EmptySlots.append([i, j])
				
		self.WaitTypes = []
		self.Score = 0
		
		self.RDPrepSlot(3)
		self.RDPutSlot()
		self.RDPrepSlot(3)
		
	def Destroy(self):
		pass
		
	def RDPrepSlot(self, num):
		for i in range(0, num):
			typeId = random.randint(1, 7)
			self.WaitTypes.append(typeId)
		typesStr = ChessHelper.TypesToStr(self.WaitTypes)
		thisPrepBubsMsg = Global.MsgMgr.sc_this_prepBubs(typesStr)
		self.Player.SendMsg(thisPrepBubsMsg)
		thatPrepBubsMsg = Global.MsgMgr.sc_that_prepBubs(typesStr)
		Global.GameMgr.SendOppositeMsg(self.Player.Hid, thatPrepBubsMsg)
	
	def RDPutSlot(self):
		poss = []
		for i in range(0, len(self.WaitTypes)):
			id = random.randint(0, len(self.EmptySlots) - 1)
			x =  self.EmptySlots[id][0]
			y =  self.EmptySlots[id][1]
			poss.append(x)
			poss.append(y)
			self.SlotTypes[x][y] = self.WaitTypes[i]
			self.EmptySlots.remove([x, y])
		del self.WaitTypes[:]

		possStr = ChessHelper.PossToStr(poss)
		thisPutBubsMsg = Global.MsgMgr.sc_this_putBubs(positions=possStr)
		self.Player.SendMsg(thisPutBubsMsg)
		thatPutBubsMsg = Global.MsgMgr.sc_that_putBubs(positions=possStr)
		Global.GameMgr.SendOppositeMsg(self.Player.Hid, thatPutBubsMsg)
		
	def TryMove(self, points):
		startP = points[0]
		Global.WriteLog("�ƶ�·��:"+str(points))
		for i in range(1, len(points)):
			midP = points[i]
			if startP[0] == midP[0]:
				stepY =  (-1, 1)[startP[1]<midP[1]]
				for y in range(startP[1] + stepY, midP[1] + stepY, stepY):
					if not self.SlotTypes[startP[0]][y] == 0:
						Global.WriteLog("��⵽�ϰ���:"+str(startP[0])+"-"+str(y))
						return 0
			else:
				stepX = (-1, 1)[startP[0]<midP[0]]
				for x in range(startP[0] + stepX, midP[0]+ stepX, stepX):
					if not self.SlotTypes[x][startP[1]] == 0:
						Global.WriteLog("��⵽�ϰ���:"+str(x)+"-"+str(startP[1]))
						return 0
			startP = points[i]
		# �ƶ�
		startP = points[0]
		endP = points[len(points)-1]
		self.SlotTypes[endP[0]][endP[1]] = self.SlotTypes[startP[0]][startP[1]]
		self.SlotTypes[startP[0]][startP[1]] = 0
		self.EmptySlots.remove(endP)
		self.EmptySlots.append(startP)
		return 1
		
	def TryRemove(self, removes):
		Global.WriteLog("��������"+str(removes))
		addScore = 0
		for i in range(0, len(removes)):
			sX = removes[i][0]
			sY = removes[i][1]
			eX = removes[i][2]
			eY = removes[i][3]
			count = 0
			if sX == eX:
				count = abs(sY - eY)  + 1
			else:
				count = abs(sX - eX) + 1
			if count < 5:
				Global.WriteLog("������������ʧ��")
				return 0
			colorType = self.SlotTypes[sX][sY]
			if sX == eX:
				stepY = (-1, 1)[sY<eY]
				for y in range(sY, eY+stepY, stepY):
					if not self.SlotTypes[sX][y] == colorType:
						Global.WriteLog("��ɫ��ƥ������ʧ��: "+str(sX)+"-"+str(y))
						return 0
			elif sY == eY:
				stepX = (-1, 1)[sY<eY]
				for x in range(sX, eX + stepX, stepX):
					if not self.SlotTypes[x][sY] == colorType:
						Global.WriteLog("��ɫ��ƥ������ʧ��: "+str(x)+"-"+str(sY))
						return 0
			else:
				stepX = (-1, 1)[sX<eX]
				stepY = (-1, 1)[sY<eY]
				for i in range(0, count):
					if not self.SlotTypes[sX + stepX * i][sY + stepY * i] == colorType:
						Global.WriteLog("��ɫ��ƥ������ʧ��: "+str(sX + stepX * i)+"-"+str(sY + stepY * i))
						return 0
						
		# ȷ����ϣ�ʵʩ����
		for i in range(0, len(removes)):
			sX = removes[i][0]
			sY = removes[i][1]
			eX = removes[i][2]
			eY = removes[i][3]
			count = 0
			if sX == eX:
				count = abs(sY - eY)  + 1
			else:
				count = abs(sX - eX) + 1
			if sX == eX:
				stepY = (-1, 1)[sY<eY]
				for y in range(sY, eY + stepY, stepY):
					self.SlotTypes[sX][y] = 0
					Global.WriteLog("����: "+str(sX)+"-"+str(y))
					self.EmptySlots.append([sX, y])
			elif sY == eY:
				stepX = (-1, 1)[sX<eX]
				for x in range(sX, eX + stepX, stepX):
					self.SlotTypes[x][sY] = 0
					Global.WriteLog("����: "+str(x)+"-"+str(sY))
					self.EmptySlots.append([x, sY])
			else:
				stepX = (-1, 1)[sX<eX]
				stepY = (-1, 1)[sY<eY]
				for i in range(0, abs(eX-sX)+1):
					self.SlotTypes[sX + stepX * i][sY + stepY * i] = 0
					Global.WriteLog("����: "+str(sX + stepX * i)+"-"+str(sY + stepY * i))
					self.EmptySlots.append([sX + stepX * i, sY + stepY * i])
			addScore += count
			
		self.Score += addScore
		return 1
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		