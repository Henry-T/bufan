# ��Ϸ��Ϣӳ��
import GameManager

eventMap = {}

def GetEventMap():
	# �ٷ�������ȱ����һ��
	global eventMap
	if not eventMap:
		eventMap["sc_get_score"] = GameManager.onGetScore
		eventMap["sc_welcome"] = GameManager.onGetWelcome
		eventMap["sc_player_info"] = GameManager.onGetPlayerInfo
	return eventMap