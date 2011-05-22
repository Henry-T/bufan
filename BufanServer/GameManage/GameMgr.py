import ServerChessBoard

class GameMgr:
	def __init__(self, bufanRoom):
		# 引用房间实例
		self.room = bufanRoom
		# 房间内玩家Id
		self.hostId = None
		self.joinId = None
		self.hostReady = 0
		self.joinReady = 0
	
	def AddPlayer(self, hid):
		# 发送欢迎消息
		welcome = self.room.MsgMgr.sc_welcome(chid=hid)
		self.room.cghall_send(hid, welcome)
		
		# 保存玩家Id
		if not self.hostId:
			hostId = hid
		elif not self.joinId:
			joinId = hid
			# 将房主信息发送给加入者
			h = self.room.cghall_get_player_by_hid(joinId)
			playerInfo = self.room.MsgMgr.sc_player_info(neckname=h.neckname, hid=h.hid, win=h.win_count, draw=h.draw_count, lose=h.lose_count, breakC=h.break_count)
			self.room.cghall_send(joinId, playerInfo)
			
		# 将新加入者的信息发送给所有人
		p = self.room.cghall_get_player_by_hid(hid)
		playerInfo = self.room.MsgMgr.sc_player_info(neckname=p.neckname, hid=p.hid, win=p.win_count, draw=p.draw_count, lose=p.lose_count, breakC=p.break_count)
		self.room.cghall_send(hostId, playerInfo)
		self.room.cghall_send(joinId, playerInfo)
	
	def InRoom(self, hid):
		if self.hostId == hid or self.joinId == hid:
			return 1
		return 0
		
	def RemovePlayer(self, hid):
		# 正常结束: 返回 
		
		# 异常退出
		pass
	
	# 通知房间内玩家有人离开
	def TellLeave(self, hid):
		leaveInfo = self.room.MsgMgr.sc_playerLeft(chid = hid)
		self.room.cghall_send(hostId, leaveInfo)
		self.room.cghall_send(joinId, leaveInfo)
		
		
	
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
		
	
	