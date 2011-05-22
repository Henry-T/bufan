import  hall_player
import random

class BufanPlayer(HallPlayer):
	def __inti__(self, room):
		HallPlayer.__init__(self)
		
		self.room = room
		self.WaitSlots = []
	
	def sendMsg(self, msg):
		self.room.cghall_send(self.hid, obj)
	
	def RDPrepSlot(self, num):
		colorStr = ""
		for i in range(0, num):
			typeId = random.randint(1, 7)
			self.WaitSlots.append(typeId)
			colorStr += string(typeId)
		
		msg = self.room.MsgMgr.sc_prepBubs(colors=colorStr)
		self.sendMsg(msg)
	
	def RDPutSlot(self):
		for i in range(0, len(self.WaitSlots)):
			id = random.randint(0, len(self.EmptySlots) - 1)
			x =  self.EmptySlots[id][0]
			y =  self.EmptySlots[id][1]
			self.Slots[x][y].SetType(self.WaitSlots[i])
			self.EmptySlots.remove([x, y])
		# Çå¿ÕÁÐ±í
		del self.WaitSlots[:]
		
		
		
	
	
	
	
		