import random
import Global
import ServerChessBoard

class BufanPlayer():
	# Error计数，达到3次判定客户端是不安全的
	def __inti__(self, hid):
		self.Hid = hid
		self.IsReady = 0
		
		self.ServerChessBoard = None
	
	def SendMsg(self, msg):
		Global.Room.cghall_send(self.hid, obj)
	
	def StartGame(self):
		self.ServerChessBoard =  ServerChessBoard.ServerChessBoard()
	
	def EndGame(self):
		self.ServerChessBoard.Destroy()
		self.ServerChessBoard = None
		self.IsReady = 0
		Global.Room.cghall_tell_player_ready(self.Hid, 0)
	
	def RemoteMove(self, points):
		ok = self.ChessBoard.TryMove(points)
		thisMoveMsg = Global.MsgMgr.sc_this_move(isOk=ok)
		sendMsg(thisMoveMsg)
		if ok == 1:
			pointsStr = ChessHelper.MoveToStr(points)
			thatMoveMsg = Global.MsgMgr.sc_that_move(pointsStr)
			Global.GameMgr.SendOppositeMsg(self.hid, thatMoveMsg)
			
	def RemoteRemove(self, removes):
		ok = self.ChessBoard.TryRemove(removes)
		thisRemoveMsg = Global.MsgMgr.sc_this_remove(isOk=ok)
		sendMsg(thisMoveMsg)
		if ok == 1:
			removesStr = ChessHelper.RemovesToStr(removes)
			thatRemoveMsg = Global.MsgMgr.sc_that_remove(removesStr)
			Global.GameMgr.SendOppositeMsg(self.hid, thatRemoveMsg)
		
		
	
	
	
	
		