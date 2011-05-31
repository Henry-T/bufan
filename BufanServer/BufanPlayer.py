import Global
import ServerChessBoard
import ChessHelper

class BufanPlayer():
	# Error计数，达到3次判定客户端是不安全的
	def __init__(self, hid):
		self.Hid = hid
		self.IsReady = 0
		
		self.ServerChessBoard = None
	
	def SendMsg(self, msg):
		Global.Room.cghall_send(self.Hid, msg)
	
	def StartGame(self):
		self.ServerChessBoard =  ServerChessBoard.ServerChessBoard(self)
	
	def EndGame(self):
		self.ServerChessBoard.Destroy()
		self.ServerChessBoard = None
		self.IsReady = 0
		Global.Room.cghall_tell_player_ready(self.Hid, 0)
	
	def RemoteMove(self, points):
		ok = self.ServerChessBoard.TryMove(points)
		if ok == 1:
			thisMoveMsg = Global.MsgMgr.sc_this_move(isOK=ok)
			self.SendMsg(thisMoveMsg)
			thatMoveMsg = Global.MsgMgr.sc_that_move(points=ChessHelper.MoveToStr(points))
			Global.GameMgr.SendOppositeMsg(self.Hid, thatMoveMsg)
			
	def ReqPut(self):
			self.ServerChessBoard.RDPutSlot();
			self.ServerChessBoard.RDPrepSlot(3);
			
	def RemoteRemove(self, removes):
		ok = self.ServerChessBoard.TryRemove(removes)
		thisRemoveMsg = Global.MsgMgr.sc_this_remove(isOK=ok, score=self.ServerChessBoard.Score)
		self.SendMsg(thisRemoveMsg)
		if ok == 1:
			thatRemoveMsg = Global.MsgMgr.sc_that_remove(lineInfo=ChessHelper.RemovesToStr(removes), score=self.ServerChessBoard.Score)
			Global.GameMgr.SendOppositeMsg(self.Hid, thatRemoveMsg)
		
		
	
	
	
	
		