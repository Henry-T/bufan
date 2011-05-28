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
			for j in range(0, self.SizeY):
				self.SlotTypes[i].append(0)	# 0代表空位 1-7代表彩球
				
		self.WaitTypes = []
		self.Score = 0
		self.GameOver = 0
		
	def Destroy(self):
		pass
		
	def RDPrepSlot(self, num):
		for i in range(0, num):
			typeId = random.randint(1, 7)
			self.WaitTpyes.append(typeId)
		typesStr = ChessHelper.TypesToStr(self.WaitTypes)
		thisPrepBubsMsg = Global.MsgMgr.sc_this_prepBubs(typesStr)
		self.Player.SendMsg(thisPrepBubsMsg)
		thatPrepBubsMsg = Global.MsgMgr.sc_that_prepBubs(typesStr)
		Global.GameMgr.SendOppositeMsg(self.Player.Hid, thatPrepBubsMsg)
	
	def RDPutSlot(self):
		poss = []
		for i in range(0, len(self.WaitTpyes)):
			id = random.randint(0, len(self.EmptySlots) - 1)
			x =  self.EmptySlots[id][0]
			y =  self.EmptySlots[id][1]
			poss.append(x)
			poss.append(y)
			self.Slots[x][y].SetType(self.WaitTpyes[i])
			self.EmptySlots.remove([x, y])
		del self.WaitTpyes[:]

		possStr = ChessHelper.PossToStr(poss)
		thisPutBubsMsg = Global.MsgMgr.sc_this_putBubs(positons=possStr)
		self.Player.SendMsg(thisPutBubsMsg)
		thatPutBubsMsg = Global.MsgMgr.sc_that_putBubs(positons=possStr)
		Global.GameMgr.SendOppositeMsg(self.Player.Hid, thatPutBubsMsg)
		
	def TryMove(points):
		startP = points[0]
		for i in range(1, len(points)):
			midP = points[i]
			for x in range(MathHelper.GetSmall(startP[0], midP[0]), MathHelper.GetBig(startP[0], midP[0])+1):
				for y in range(MathHelper.GetSmall(startP[1], midP[1]), MathHelper.GetBig(startP[0], midP[0])+1):
					if not self.SlotTypes[x][y] == 0
						return 0
			startP = points[i]
		# 移动
		startP = points[0]
		endP = points[len(points)-1]
		SlotTypes[endP[0]][endP[1]] = SlotTypes[startP[0]][startP[1]]
		SlotTypes[startP[0]][startP[1]] = 0
		return 1
		
	def TryRemove(removes):
		addScore = 0
		for i in range(0, len(removes)):
			sX = removes[i][0]
			sY = removes[i][1]
			eX = removes[i][2]
			eY = removes[i][3]
			count = 0
			if sX == eX:
				count = abs(sY - eY) # 使用标准函数
			else:
				count = abs(sX - eX)
			if count == 0:
				return 0
			colorType = self.SlotTypes[sX][sY]
			for x in range(MathHelper.GetSmall(sX, eX), MathHelper.GetBig(sY, eY)):
				for y in range(MathHelper.GetSmall(sY, eY), MathHelper.GetBig(sY, eY)):
					if not self.SlotTypes[x][y] == colorType
						return 0
			# 确认完毕，实施消除
			for x in range(MathHelper.GetSmall(sX, eX), MathHelper.GetBig(sY, eY)):
				for y in range(MathHelper.GetSmall(sY, eY), MathHelper.GetBig(sY, eY)):
					self.SlotTypes[x][y] = 0
			addScore += count
		self.Score += addScore
		return 1
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		