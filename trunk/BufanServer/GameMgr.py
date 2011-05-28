import Global
import BufanPlayer

class GameMgr:
	def __init__(self):
		Global.GameMgr = self
		# 房间内玩家Id
		self.players = []
		self.hids = []
		
		# 游戏状态 TODO
		self.State = "Wait"
		
	def GetPlayerByHid(self, hid):
		for i in range(0, len(self.players)):
			if self.players[i].Hid == hid:
				return hid
		return None
		
	def SendOppositeMsg(self, hid, msg):
		if not len(self.players) == 2
			return
		if hid == self.players[0].Hid:
			self.player[1].SendMsg(msg)
		else:
			self.player[0].SendMsg(msg)
		
	def AddPlayer(self, hid):
		# 发送欢迎消息
		welcome = Global.MsgMgr.sc_welcome(chid=hid)
		Global.Room.cghall_send(hid, welcome)
		
		# 添加玩家
		player = BufanPlayer.BufanPlayer(hid)
		self.players.append(player)
			
		# 将新加入者的信息发送给所有人
		p = Global.Room.cghall_get_player_by_hid(hid)
		playerInfo = Global.MsgMgr.sc_player_info(nickname=p.nickname, hid=p.hid, win=p.win_count, draw=p.draw_count, lose=p.lose_count, breakC=p.break_count)
		Global.Room.cghall_broadcast(playerInfo)
		
		# 如果房间内已经有人，将已有玩家信息发送给新玩家
		if len(self.players) == 2:
			host = Global.Room.cghall_get_player_by_hid(self.players[0].Hid)
			playerInfo = Global.MsgMgr.sc_player_info(nickname=host.nickname, hid=host.hid, win=host.win_count, draw=host.draw_count, lose=host.lose_count, breakC=host.break_count)
			self.players[1].SendMsg(playerInfo)
	
	def InRoom(self, hid):
		for i in range(0, len(self.players)):
			if self.players[i].Hid == hid:
				return 1
		return 0
	
	def RemovePlayer(self, hid):
		for i in range(0, len(self.players)):
			if self.players[i].Hid == hid:
				self.hids.remove(self.players[i])
				
		leaveInfo = Global.MsgMgr.sc_playerLeft(chid = hid)
		Global.Room.cghall_broadcast(leaveInfo)
		
	def SetReady(self, phid, pisReady):
		player = GetPlayerByHid(phid)
		if player:
			player.IsReady = pisReady
		readyInfo = Global.MsgMgr.sc_playerReady(hid=phid, isReady=pisReady)
		Global.MsgMgr.cghall_broadcast(readyInfo)
		
		Global.Room.cghall_tell_player_ready(hid, pisReady)
		
		for i in range(0, len(self.players)):
			if self.players[i].IsReady == 0:
				return
		self.StartGame()
	
	def StartGame(self):
		self.State = "InGame"
		self.players[0].StartGame()
		self.players[1].StartGame()
		Global.Room.cghall_tell_hall_game_start()
	
	def EndGame(self):
		self.State = "Wait"
		self.players[0].EndGame()
		self.players[1].EndGame()
		Global.Room.cghall_tell_hall_game_end()
	
	def PlayerMove(self, hid, sX, sY, eX, eY):
		player = self.GetPlayerByHid(hid)
		player.RemoteMove(points)
	
	def PlayerRemove(self, hid, removes):
		player = self.GetPlayerByHid(hid)
		player.RemoteRemove(removes)
		
	
	