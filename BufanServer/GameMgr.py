import ServerChessBoard
import Global

class GameMgr:
	def __init__(self):
		# ���������Id
		self.hids = []
		self.readys = []
		
		# ��Ϸ״̬ TODO...
	
	def AddPlayer(self, hid):
		# ���ͻ�ӭ��Ϣ
		welcome = Global.MsgMgr.sc_welcome(chid=hid)
		Global.Room.cghall_send(hid, welcome)
		
		# ������Id
		self.hids.append(hid)
			
		# ���¼����ߵ���Ϣ���͸�������
		p = Global.Room.cghall_get_player_by_hid(hid)
		Global.WriteLog("�����ߵ�hid: %s" % (hid))
		playerInfo = Global.MsgMgr.sc_player_info(nickname=p.nickname, hid=p.hid, win=p.win_count, draw=p.draw_count, lose=p.lose_count, breakC=p.break_count)
		Global.Room.cghall_broadcast(playerInfo)
		
		# ����������Ѿ����ˣ������������Ϣ���͸������
		if len(self.hids) == 2:
			host = Global.Room.cghall_get_player_by_hid(self.hids[0])
			playerInfo = Global.MsgMgr.sc_player_info(nickname=host.nickname, hid=host.hid, win=host.win_count, draw=host.draw_count, lose=host.lose_count, breakC=host.break_count)
			Global.Room.cghall_send(self.hids[1], playerInfo)
			
	
	def InRoom(self, hid):
		for i in range(0, len(self.hids)):
			if self.hids[i] == hid:
				return 1
		return 0
		
	
	# ֪ͨ��������������뿪
	def TellLeave(self, hid):
		self.hids.remove(hid)
		leaveInfo = Global.MsgMgr.sc_playerLeft(chid = hid)
		Global.Room.cghall_broadcast(leaveInfo)
		
	def StartGame(self):
		self.State = "InGame"
		# ��ʼ������
		self.chessboard = ServerChessBoard.ServerChessBoard()
		# ֪ͨ������Ϸ�ѿ�ʼ
		Global.Room.cghall_tell_hall_game_start()
	
	def EndGame(self):
		# ֪ͨ������Ϸ����
		Global.Room.cghall_tell_hall_game_end()
		
	
	def SetReady(self, phid, pisReady):
		if phid == hostId:
			hostReady = pisReady
		elif phid == joinId:
			joinReady = pisReady
		else:
			pass
		
		readyInfo = Global.MsgMgr.sc_playerReady(hid=phid, isReady=pisReady)
		Global.MsgMgr.cghall_broadcast(readyInfo)
		
		# ֪ͨ������ҵ�׼��״̬
		Global.Room.cghall_tell_player_ready(hid, pisReady)
		
		if hostReady == 1 and joinReady == 1:
			self.StartGame()
	
	def RemovePlayer(self, hid):
		# TODO ������
		pass
	
	def PlayerMove(self, hid, sX, sY, eX, eY):
	
	def PlayerRemove(self, hid, removes):
		
	
	