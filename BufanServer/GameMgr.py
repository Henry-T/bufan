import ServerChessBoard
import Global

class GameMgr:
	def __init__(self, bufanRoom):
		# 引用房间实例
		self.room = bufanRoom
		# 房间内玩家Id
		self.hids = []
		self.readys = []
	
	def AddPlayer(self, hid):
		# 发送欢迎消息
		welcome = self.room.MsgMgr.sc_welcome(chid=hid)
		self.room.cghall_send(hid, welcome)
		
		# 添加玩家Id
		self.hids.append(hid)
			
		# 将新加入者的信息发送给所有人
		p = self.room.cghall_get_player_by_hid(hid)
		Global.WriteLog("加入者的hid: %s" % (hid))
		playerInfo = self.room.MsgMgr.sc_player_info(nickname=p.nickname, hid=p.hid, win=p.win_count, draw=p.draw_count, lose=p.lose_count, breakC=p.break_count)
		for i in range(0, len(self.hids)):
			self.room.cghall_send(self.hids[i], playerInfo)
		
		# 如果房间内已经有人，将已有玩家信息发送给新玩家
		if len(self.hids) == 2:
			host = self.room.cghall_get_player_by_hid(self.hids[0])
			playerInfo = self.room.MsgMgr.sc_player_info(nickname=host.nickname, hid=host.hid, win=host.win_count, draw=host.draw_count, lose=host.lose_count, breakC=host.break_count)
			self.room.cghall_send(self.hids[1], playerInfo)
			
	
	def InRoom(self, hid):
		for i in range(0, len(self.hids)):
			if self.hids[i] == hid:
				return 1
		return 0
		
	def RemovePlayer(self, hid):
		# 正常结束: 返回 
		
		# 异常退出
		pass
	
	# 通知房间内玩家有人离开
	def TellLeave(self, hid):
		self.hids.remove(hid)
		leaveInfo = self.room.MsgMgr.sc_playerLeft(chid = hid)
		for i in range(0, len(self.hids)):
			self.room.cghall_send(self.hids[i], leaveInfo)
		
		
	
	def SetReady(self, hid, isReady):
		if hid == hostId:
			hostReady = isReady
		elif hid == joinId:
			joinReady = isReady
		else:
			pass
		
		# 通知大厅玩家的准备状态 TODO 修正
		self.room.cghall_tell_player_ready(hid, isReady)
		
		
	def StartGame(self):
		self.State = "InGame"
		# 初始化棋盘
		self.chessboard = ServerChessBoard.ServerChessBoard()
		# 通知大厅游戏已开始
		self.room.cghall_tell_hall_game_start()
	
	def EndGame(self):
		# 通知大厅游戏结束
		self.room.cghall_tell_hall_game_end()
		
	
	