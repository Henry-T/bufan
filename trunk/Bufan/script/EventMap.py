# ��Ϸ��Ϣӳ��
import GameManager

EventMap = {
	"sc_welcome":GameManager.onGetWelcome,
	"sc_player_info":GameManager.onGetPlayerInfo,
}

# eventMap = {}

# def GetEventMap():
	# # �ٷ�������ȱ����һ��
	# global eventMap
	# if not eventMap:
		# eventMap["sc_welcome"] = GameManager.onGetWelcome
		# eventMap["sc_player_info"] = GameManager.onGetPlayerInfo
	# return eventMap