import ServerChessBoard

class GameMgr:
	def __init__(self, bufanRoom):
		# ���÷���ʵ��
		self.room = bufanRoom
		# ���������Id
		self.hostId = None
		self.joinId = None
		self.hostReady = 0
		self.joinReady = 0
	
	def AddPlayer(self, hid):
		# ���ͻ�ӭ��Ϣ
		welcome = self.room.MsgMgr.sc_welcome(chid=hid)
		self.room.cghall_send(hid, welcome)
		
		# �������Id
		if not self.hostId:
			hostId = hid
		elif not self.joinId:
			joinId = hid
			# ��������Ϣ���͸�������
			h = self.room.cghall_get_player_by_hid(joinId)
			playerInfo = self.room.MsgMgr.sc_player_info(neckname=h.neckname, hid=h.hid, win=h.win_count, draw=h.draw_count, lose=h.lose_count, breakC=h.break_count)
			self.room.cghall_send(joinId, playerInfo)
			
		# ���¼����ߵ���Ϣ���͸�������
		p = self.room.cghall_get_player_by_hid(hid)
		playerInfo = self.room.MsgMgr.sc_player_info(neckname=p.neckname, hid=p.hid, win=p.win_count, draw=p.draw_count, lose=p.lose_count, breakC=p.break_count)
		self.room.cghall_send(hostId, playerInfo)
		self.room.cghall_send(joinId, playerInfo)
	
	def InRoom(self, hid):
		if self.hostId == hid or self.joinId == hid:
			return 1
		return 0
		
	def RemovePlayer(self, hid):
		# ��������: ���� 
		
		# �쳣�˳�
		pass
	
	# ֪ͨ��������������뿪
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
		
	
	