import Global
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
		
	def TryMove():
		# TODO
		pass
		
	def TryRemove():
		# TODO
		pass
		
		
		
		
		