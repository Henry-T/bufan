#-*- coding:GBK -*-

import hall_object
import hall_callback
import log
import GameMgr

# 房间玩家 - 只允许双人游戏

class BufanRoom(hall_object.HallRoom):
	def __init__(self, room_id=0, name='', mode=0, host=0, pwd='', max_num=0):

		super(BufanRoom, self).__init__(room_id, name, mode, host, pwd, max_num)

		self.MsgMgr = hall_callback.get_game_room_msgmgr()
		
		# 玩家管理器
		self.gameMgr = GameMgr.GameMgr()
			
	##  重载  ########
	def cghall_on_player_enter_room(self, player, obj):
		self.log.info("[消息处理]玩家进入房间 uid:%s hid:%s" % (player.uid, player.hid))
		# 将新玩家纳入管理
		self.gameMgr.AddPlayer(player.hid)
	
	def cghall_on_player_leave_room(self, hid):
		if self.gameMgr.InRoom(hid):
			# 玩家仍在房间中 - Hall因为某种原因强迫玩家离开
			# TODO 通知房间内的玩家有人离开
			self.gameMgr.TellLeave(hid)
			pass
		else:
			# 玩家不在房间中 - 玩家主动离开，这是Hall的会发信息
			# 不做处理
			pass
			
	def onNetSetReady(self, player, msg):
		self.log.info("[消息处理]玩家更改状态 hid:%s 状态:%s" %(player.hid, msg.isReady))
		self.gameMgr.SetReady(hid, msg.isReady)
		
	def onNetReqLeaveRoom(self, player, msg):
		self.log.info("[消息处理]玩家请求离开房间 uid:%s hid:%s" %(player.uid, player.hid))
		self.gameMgr.RemovePlayer(player.hid)
		self.cghall_tell_hall_player_leave_room(player.hid)
	
	def onNetMove(self, player, msg):
		self.log.info("[消息处理]玩家请求移动棋子 hid:%s" %(player.hid))
		self.gameMgr.PlayerMove(player.hid, msg.sX, msg.sY, msg.eX, msg.eY)
	
	def onNetRemove(self, player, msg):
		self.log.info("[消息处理]玩家请求消除连线 hid:%s" %(player.hid))
		self.gameMgr.PlayerRemove(player.hid, strToRemoves(msg.lineInfo))

	def strToRemoves(removeNum,removeStr):
		removes = []
		for i in range(0, removeNum):
			removes.append([])
			for j in range(0, 4):
				removes[i].append(int(ord(removeStr[i * 4 + j, 1])))
		return removes

	
















	
	
	
	
	