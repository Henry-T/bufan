#-*- coding:GBK -*-

import hall_object
import hall_callback
import log
import GameMgr

# ������� - ֻ����˫����Ϸ

class BufanRoom(hall_object.HallRoom):
	def __init__(self, room_id=0, name='', mode=0, host=0, pwd='', max_num=0):

		super(BufanRoom, self).__init__(room_id, name, mode, host, pwd, max_num)

		self.MsgMgr = hall_callback.get_game_room_msgmgr()
		
		# ��ҹ�����
		self.gameMgr = GameMgr.GameMgr()
			
	##  ����  ########
	def cghall_on_player_enter_room(self, player, obj):
		self.log.info("[��Ϣ����]��ҽ��뷿�� uid:%s hid:%s" % (player.uid, player.hid))
		# ��������������
		self.gameMgr.AddPlayer(player.hid)
	
	def cghall_on_player_leave_room(self, hid):
		if self.gameMgr.InRoom(hid):
			# ������ڷ����� - Hall��Ϊĳ��ԭ��ǿ������뿪
			# TODO ֪ͨ�����ڵ���������뿪
			self.gameMgr.TellLeave(hid)
			pass
		else:
			# ��Ҳ��ڷ����� - ��������뿪������Hall�Ļᷢ��Ϣ
			# ��������
			pass
			
	def onNetSetReady(self, player, msg):
		self.log.info("[��Ϣ����]��Ҹ���״̬ hid:%s ״̬:%s" %(player.hid, msg.isReady))
		self.gameMgr.SetReady(hid, msg.isReady)
		
	def onNetReqLeaveRoom(self, player, msg):
		self.log.info("[��Ϣ����]��������뿪���� uid:%s hid:%s" %(player.uid, player.hid))
		self.gameMgr.RemovePlayer(player.hid)
		self.cghall_tell_hall_player_leave_room(player.hid)
	
	def onNetMove(self, player, msg):
		self.log.info("[��Ϣ����]��������ƶ����� hid:%s" %(player.hid))
		self.gameMgr.PlayerMove(player.hid, msg.sX, msg.sY, msg.eX, msg.eY)
	
	def onNetRemove(self, player, msg):
		self.log.info("[��Ϣ����]��������������� hid:%s" %(player.hid))
		self.gameMgr.PlayerRemove(player.hid, strToRemoves(msg.lineInfo))

	def strToRemoves(removeNum,removeStr):
		removes = []
		for i in range(0, removeNum):
			removes.append([])
			for j in range(0, 4):
				removes[i].append(int(ord(removeStr[i * 4 + j, 1])))
		return removes

	
















	
	
	
	
	