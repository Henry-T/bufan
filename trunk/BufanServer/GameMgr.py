import ServerChessBoard
import Global

class GameMgr:
	def __init__(self, bufanRoom):
		# ���÷���ʵ��
		self.room = bufanRoom
		# ���������Id
		self.hids = []
		self.readys = []
	
	def AddPlayer(self, hid):
		# ���ͻ�ӭ��Ϣ
		welcome = self.room.MsgMgr.sc_welcome(chid=hid)
		self.room.cghall_send(hid, welcome)
		
		# ������Id
		self.hids.append(hid)
			
		# ���¼����ߵ���Ϣ���͸�������
		p = self.room.cghall_get_player_by_hid(hid)
		Global.WriteLog("�����ߵ�hid: %s" % (hid))
		playerInfo = self.room.MsgMgr.sc_player_info(nickname=p.nickname, hid=p.hid, win=p.win_count, draw=p.draw_count, lose=p.lose_count, breakC=p.break_count)
		for i in range(0, len(self.hids)):
			self.room.cghall_send(self.hids[i], playerInfo)
		
		# ����������Ѿ����ˣ������������Ϣ���͸������
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
		# ��������: ���� 
		
		# �쳣�˳�
		pass
	
	# ֪ͨ��������������뿪
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
		
		# ֪ͨ������ҵ�׼��״̬ TODO ����
		self.room.cghall_tell_player_ready(hid, isReady)
		
		
	def StartGame(self):
		self.State = "InGame"
		# ��ʼ������
		self.chessboard = ServerChessBoard.ServerChessBoard()
		# ֪ͨ������Ϸ�ѿ�ʼ
		self.room.cghall_tell_hall_game_start()
	
	def EndGame(self):
		# ֪ͨ������Ϸ����
		self.room.cghall_tell_hall_game_end()
		
	
	