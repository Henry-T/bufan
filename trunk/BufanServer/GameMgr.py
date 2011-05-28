import ServerChessBoard
import Global

class GameMgr:
	def __init__(self):
		# 房间内玩家Id
		self.hids = []
		self.readys = []
		
		# 游戏状态 TODO...
	
	def AddPlayer(self, hid):
		# 发送欢迎消息
		welcome = Global.MsgMgr.sc_welcome(chid=hid)
		Global.Room.cghall_send(hid, welcome)
		
		# 添加玩家Id
		self.hids.append(hid)
			
		# 将新加入者的信息发送给所有人
		p = Global.Room.cghall_get_player_by_hid(hid)
		Global.WriteLog("加入者的hid: %s" % (hid))
		playerInfo = Global.MsgMgr.sc_player_info(nickname=p.nickname, hid=p.hid, win=p.win_count, draw=p.draw_count, lose=p.lose_count, breakC=p.break_count)
		Global.Room.cghall_broadcast(playerInfo)
		
		# 如果房间内已经有人，将已有玩家信息发送给新玩家
		if len(self.hids) == 2:
			host = Global.Room.cghall_get_player_by_hid(self.hids[0])
			playerInfo = Global.MsgMgr.sc_player_info(nickname=host.nickname, hid=host.hid, win=host.win_count, draw=host.draw_count, lose=host.lose_count, breakC=host.break_count)
			Global.Room.cghall_send(self.hids[1], playerInfo)
			
	
	def InRoom(self, hid):
		for i in range(0, len(self.hids)):
			if self.hids[i] == hid:
				return 1
		return 0
		
	
	# 通知房间内玩家有人离开
	def TellLeave(self, hid):
		self.hids.remove(hid)
		leaveInfo = Global.MsgMgr.sc_playerLeft(chid = hid)
		Global.Room.cghall_broadcast(leaveInfo)
		
	def StartGame(self):
		self.State = "InGame"
		# 初始化棋盘
		self.chessboard = ServerChessBoard.ServerChessBoard()
		# 通知大厅游戏已开始
		Global.Room.cghall_tell_hall_game_start()
	
	def EndGame(self):
		# 通知大厅游戏结束
		Global.Room.cghall_tell_hall_game_end()
		
	
	def SetReady(self, phid, pisReady):
		if phid == hostId:
			hostReady = pisReady
		elif phid == joinId:
			joinReady = pisReady
		else:
			pass
		
		readyInfo = Global.MsgMgr.sc_playerReady(hid=phid, isReady=pisReady)
		Global.MsgMgr.cghall_broadcast(readyInfo)
		
		# 通知大厅玩家的准备状态
		Global.Room.cghall_tell_player_ready(hid, pisReady)
		
		if hostReady == 1 and joinReady == 1:
			self.StartGame()
	
	def RemovePlayer(self, hid):
		# TODO 。。。
		pass
	
	def PlayerMove(self, hid, sX, sY, eX, eY):
	
	def PlayerRemove(self, hid, removes):
		
	
	