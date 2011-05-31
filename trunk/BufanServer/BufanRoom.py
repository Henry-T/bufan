#-*- coding:GBK -*-

import hall_object
import hall_callback
import log
import Global
import GameMgr
import ChessHelper

# ������� - ֻ����˫����Ϸ

class BufanRoom(hall_object.HallRoom):
	def __init__(self, room_id=0, name='', mode=0, host=0, pwd='', max_num=0):

		super(BufanRoom, self).__init__(room_id, name, mode, host, pwd, max_num)

		self.MsgMgr = hall_callback.get_game_room_msgmgr()
		
		# ��ҹ�����
		self.gameMgr = GameMgr.GameMgr()
		
		Global.init(self)
			
	##  ����  ########
	def cghall_on_player_enter_room(self, player, obj):
		self.log.info("[��Ϣ����]��ҽ��뷿�� uid:%s hid:%s" % (player.uid, player.hid))
		# ��������������
		self.gameMgr.AddPlayer(player.hid)
	
	def cghall_on_player_leave_room(self, hid):
		if self.gameMgr.InRoom(hid):
			# ���δ�����뿪���� - Hall��Ϊĳ��ԭ��ǿ������뿪
			self.gameMgr.RemovePlayer(hid)
		else:
			# ��Ҳ��ڷ����� - ��������뿪 ���账��
			pass
			
	def onNetSetReady(self, player, msg):
		self.log.info("[��Ϣ����]��Ҹ���״̬ hid:%s ״̬:%s" %(player.hid, msg.isReady))
		self.gameMgr.SetReady(player.hid, msg.isReady)
		
	def onNetReqLeaveRoom(self, player, msg):
		self.log.info("[��Ϣ����]��������뿪���� uid:%s hid:%s" %(player.uid, player.hid))
		self.gameMgr.RemovePlayer(player.hid)
		self.cghall_tell_hall_player_leave_room(player.hid)
	
	def onNetReqBreak(self, player, msg):
		self.log.info("[��Ϣ����]������� uid:%s hid:%s" %(player.uid, player.hid))
		self.gameMgr.Break(player.hid)
	
	def onNetMove(self, player, msg):
		self.log.info("[��Ϣ����]��������ƶ����� hid:%s" %(player.hid))
		self.gameMgr.PlayerMove(player.hid, ChessHelper.StrToMove(msg.points))
		
	def onNetReqPut(self, player,msg):
		self.log.info("[��Ϣ��¯]�������ڷ����� hid:%s" %(player.hid))
		self.gameMgr.PlayerReqPut(player.hid)
	
	def onNetRemove(self, player, msg):
		self.log.info("[��Ϣ����]��������������� hid:%s" %(player.hid))
		self.gameMgr.PlayerRemove(player.hid, ChessHelper.StrToRemoves(msg.lineInfo))

	
















	
	
	
	
	