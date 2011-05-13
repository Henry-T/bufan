#-*- coding:GBK -*-

import hall_object
import hall_callback
import log

class BufanRoom(hall_object.HallRoom):
	def __init__(self, room_id=0, name='', mode=0, host=0, pwd='', max_num=0):

		super(BufanRoom, self).__init__(room_id, name, mode, host, pwd, max_num)

		self.msgmgr = hall_callback.get_game_room_msgmgr()
	
	##  ����  ########
	def cghall_on_player_enter_room(self, player, obj):
		"""
		����ҽ���˷���ʱ, ��ص��ô˺���
		"""
		self.log.info("[��Ϣ����]��ҽ��뷿�� uid:%s hid:%s" % (player.uid, player.hid))
		### send score
		newmsg = self.msgmgr.sc_get_score(score=player.score)
		self.cghall_send(player.hid, newmsg)
	
	def cghall_on_player_leave_room(self, hid):
		"""
		������뿪����ʱ, ��ص��˺���
		"""
		self.log.info("[��Ϣ����]����뿪����:%s"%hid)
		
		
	def onReqLeaveRoom(self, player, msg):
		self.log.info("[��Ϣ����]��������뿪���� uid:%s hid:%s" %(player.uid, player.hid))
		self.cghall_tell_player_leave_room(player.hid)
		
	def onSetPos(self, player, srcPosX, srcPosY, tgtPosX, tgtPosY):
		self.log.info("[��Ϣ����]��������ƶ�����: sPosX:%s sPosY:%s tPosX:%s tPosY:%s" %(srcPosX, srcPosY, tgtPosX, tgtPosY))
		
	