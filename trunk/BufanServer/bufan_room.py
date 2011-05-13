#-*- coding:GBK -*-

import hall_object
import hall_callback
import log

class BufanRoom(hall_object.HallRoom):
	def __init__(self, room_id=0, name='', mode=0, host=0, pwd='', max_num=0):

		super(BufanRoom, self).__init__(room_id, name, mode, host, pwd, max_num)

		self.msgmgr = hall_callback.get_game_room_msgmgr()
	
	##  重载  ########
	def cghall_on_player_enter_room(self, player, obj):
		"""
		有玩家进入此房间时, 会回调用此函数
		"""
		self.log.info("[消息处理]玩家进入房间 uid:%s hid:%s" % (player.uid, player.hid))
		### send score
		newmsg = self.msgmgr.sc_get_score(score=player.score)
		self.cghall_send(player.hid, newmsg)
	
	def cghall_on_player_leave_room(self, hid):
		"""
		有玩家离开房间时, 会回调此函数
		"""
		self.log.info("[消息处理]玩家离开房间:%s"%hid)
		
		
	def onReqLeaveRoom(self, player, msg):
		self.log.info("[消息处理]玩家请求离开房间 uid:%s hid:%s" %(player.uid, player.hid))
		self.cghall_tell_player_leave_room(player.hid)
		
	def onSetPos(self, player, srcPosX, srcPosY, tgtPosX, tgtPosY):
		self.log.info("[消息处理]玩家请求移动棋子: sPosX:%s sPosY:%s tPosX:%s tPosY:%s" %(srcPosX, srcPosY, tgtPosX, tgtPosY))
		
	