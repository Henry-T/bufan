# 游戏消息映射
import GameManager

EventMap = {
	"sc_welcome":GameManager.onGetWelcome,
	"sc_player_info":GameManager.onGetPlayerInfo,
}

# eventMap = {}

# def GetEventMap():
	# # 官方例子中缺少这一行
	# global eventMap
	# if not eventMap:
		# eventMap["sc_welcome"] = GameManager.onGetWelcome
		# eventMap["sc_player_info"] = GameManager.onGetPlayerInfo
	# return eventMap